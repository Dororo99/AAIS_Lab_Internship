## 파일 설명
### extract_patch.py

- **기능**: SVS 파일에서 이미지 패치를 추출하고, 고유치 분석을 통해 조직과 배경을 구분하여 패치를 저장합니다.
- **주요 라이브러리**: `openslide`, `numpy`, `PIL`, `os`
- **주요 특징**:
  - 썸네일의 고유치를 기준으로 전체 이미지의 특성을 분석
  - 각 패치의 고유치를 계산하여 조직/배경 영역 구분
  - 조직과 배경 패치의 균형을 맞추어 저장
- **사용법**: 
  ```python
  # 저장 경로 설정
  target_path = r'/path/to/save/patches/'
  
  # SVS 파일 경로 설정
  svs_root = '/path/to/svs/files'
  ```

### naming.py

- **기능**: 추출된 패치 이미지 파일들의 이름을 순차적으로 변경합니다.
- **주요 라이브러리**: `os`, `glob`
- **주요 특징**:
  - 파일 이름에 순차적 번호 부여
  - 접두사 추가 옵션
  - 다양한 이미지 확장자 지원
- **사용법**:
  ```python
  rename_files_with_numbering(
      folder_path='/path/to/images',
      prefix='',              # 예: 'patch_'
      start_num=1,
      num_digits=3,          # 결과: 001, 002, ...
      extension_filter=['*.png', '*.jpg', '*.jpeg']
  )
  ```

### region_extract.py

- **기능**: 지정된 좌표에서 특정 크기의 패치를 추출합니다.
- **주요 라이브러리**: `openslide`, `PIL`
- **주요 특징**:
  - 특정 좌표 기반 패치 추출
  - 사용자 지정 패치 크기 지원
- **사용법**:
  - `extract_patch` 함수를 사용하여 패치를 추출합니다.
  - `slide_path`, `x`, `y`, `tile_size`를 설정하여 원하는 위치와 크기의 패치를 추출합니다.
  - 추출된 패치는 `patch.save("output_patch.png")`를 통해 저장할 수 있습니다.

## 설치 및 실행

1. 필요한 라이브러리를 설치합니다:
   ```bash
   pip install openslide-python pillow numpy opencv-python matplotlib
   ```

2. 각 스크립트를 실행하여 원하는 기능을 수행합니다.

## 주의사항

- OpenSlide 라이브러리를 사용하기 위해서는 시스템에 OpenSlide가 설치되어 있어야 합니다.
- SVS 파일의 경로와 이미지 저장 경로를 정확히 설정해야 합니다.