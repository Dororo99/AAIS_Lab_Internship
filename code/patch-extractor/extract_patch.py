import openslide
from PIL import Image, ImageFilter
import numpy as np
import cv2
import os
import torch
import matplotlib.pyplot as plt
from openslide import open_slide
from openslide import OpenSlide

'''
원하는 저장소 위치 지정
    - target_path
'''
target_path = r'/home/dororo99/patch-extractor-dororo/patch2/'
save_path = os.path.join(target_path)

# 저장 디렉토리가 없으면 생성
if not os.path.exists(save_path):
    os.makedirs(save_path)
    print(f"저장 디렉토리 생성됨: {save_path}")

# 경로가 '/'로 끝나는지 확인
if not save_path.endswith('/'):
    save_path += '/'
'''
svs 저장소 root 위치
    - svs_root
'''
svs_root = '/home/dororo99/data'
svs_file_path = svs_root +'/TCGA-DQ-7591-01Z-00-DX1.8304B939-542C-4D30-8C77-F705DE1311FF.svs'

# OpenSlide로 SVS 파일 열기
slide = openslide.OpenSlide(svs_file_path)

# 전체 이미지의 고유치 평균 계산을 위한 썸네일 생성
thumbnail = slide.get_thumbnail(slide.level_dimensions[-1])
thumbnail = thumbnail.convert('RGB')

# 썸네일의 픽셀 데이터를 (h*w, 3) 형태로 변환
pixels_thumb = np.array(thumbnail).reshape(-1, 3)

# 썸네일의 공분산 행렬 계산
cov_matrix_thumb = np.cov(pixels_thumb.T)

# 썸네일의 고유값 계산
eigvals_thumb, eigvecs_thumb = np.linalg.eig(cov_matrix_thumb)

# 전체 이미지의 고유치 평균 계산
"""
전체 이미지 고유치와 고유벡터를 다음과 같이 선언합니다.

first_mean_eigval: 전체 이미지의 첫 번째 고유치
sec_mean_eigval: 전체 이미지의 두 번째 고유치
"""
first_mean_eigval = np.mean(eigvals_thumb[0])
sec_mean_eigval = np.mean(eigvals_thumb[1])

# 타일 크기 설정
tile_size = 1024  # 필요에 따라 조정

# 선택한 레벨 (0은 가장 높은 해상도)
level = 0

# 선택한 레벨의 이미지 크기
width, height = slide.level_dimensions[level]

cnt_1 = 0
cnt_2 = 0
# 타일 단위로 이미지 순회
for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        # 현재 타일의 실제 크기 계산
        tile_width = min(tile_size, width - x)
        tile_height = min(tile_size, height - y)

        # 타일 영역 읽기
        tile = slide.read_region((x, y), level, (tile_width, tile_height))
        tile = tile.convert('RGB')

        # 타일의 픽셀 데이터를 (h*w, 3) 형태로 변환
        pixels_tile = np.array(tile).reshape(-1, 3)

        # 타일의 공분산 행렬 계산
        cov_matrix_tile = np.cov(pixels_tile.T)

        # 타일의 고유값 계산
        eigvals_tile, eigvecs_tile = np.linalg.eig(cov_matrix_tile)
        
        # 내림차순 정렬
        sorted_indices = np.argsort(eigvals_tile)[::-1]
        sorted_eigvals = eigvals_tile[sorted_indices]
        sorted_eigvecs = eigvecs_tile[:,sorted_indices]

        # 타일의 가장 큰 고유치 가져오기
        """
        패치 이미지의 고유치와 고유벡터를 다음과 같이 선언합니다.
        
        first_eigval: 첫 번째 고유치
        first_eigvec: 첫 번째 고유벡터
        sec_eigval: 두 번째 고유치
        sec_eigvec: 두 번째 고유벡터
        """
        first_eigval = sorted_eigvals[0]
        first_eigvec = sorted_eigvecs[0]
        sec_eigval = sorted_eigvals[1]

        # 조건 비교
        if (first_eigval > first_mean_eigval) & (sec_eigval > sec_mean_eigval):
            # 조건을 만족하는 타일 처리 (예: 저장)
            tile_filename = f"tile_tissue_{x}_{y}.png"
            full_path = os.path.join(save_path, tile_filename)
            tile.save(full_path)
            print(f"조직 저장: {tile_filename}, 평균값: {first_eigval:.2f}, 고유값1: {sorted_eigvals[0]:.2f}, 고유값2: {sorted_eigvals[1]:.2f}")
            cnt_1 = cnt_1 + 1
        else:
            # 조건을 만족하지 않는 타일은 무시
            tile_filename = f"tile_back_{x}_{y}.png"
            if (np.abs(first_eigvec[1]) < (np.maximum(np.abs(first_eigvec[0]),np.abs(first_eigvec[2])))):
                if (cnt_1 >= cnt_2):
                    tile_filename = f"tile_back_{x}_{y}.png"
                    full_path = os.path.join(save_path, tile_filename)
                    tile.save(full_path)
                    print(f"배경 저장: {tile_filename}, 최대 고유치: {first_eigval}")                
                    cnt_2 = cnt_2 + 1
                else:
                    print(f"배경 무시: 위치 ({x}, {y}), 최대 고유치: {first_eigval}")
            else:
                print(f"배경 무시: 위치 ({x}, {y}), 최대 고유치: {first_eigval}")