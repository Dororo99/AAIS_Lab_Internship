import os
import glob

def rename_files_with_numbering(folder_path, prefix='', start_num=1, num_digits=3, extension_filter=['*.png', '*.jpg', '*.jpeg']):
    """
    지정된 폴더 내의 이미지 파일 이름 앞에 순차적인 번호를 추가하여 변경합니다.
    
    :param folder_path: 파일이 위치한 폴더의 경로
    :param prefix: 파일 이름의 접두사 (기본값: 빈 문자열)
    :param start_num: 번호 매기기의 시작 번호 (기본값: 1)
    :param num_digits: 번호의 자릿수 (기본값: 3, 예: 001)
    :param extension_filter: 필터링할 파일 확장자 목록 (기본값: ['*.png', '*.jpg', '*.jpeg'])
    """
    # 필터에 맞는 모든 파일 경로 가져오기
    image_files = []
    for ext in extension_filter:
        image_files.extend(glob.glob(os.path.join(folder_path, ext)))
    
    # 파일이 존재하는지 확인
    if not image_files:
        print("해당 확장자의 파일이 폴더에 존재하지 않습니다.")
        return
    
    # 파일 정렬 (선택 사항: 파일 이름 기준으로 정렬)
    image_files.sort()
    
    # 번호 매기기
    current_num = start_num
    for file_path in image_files:
        # 파일의 디렉토리와 파일 이름 분리
        dir_name, original_filename = os.path.split(file_path)
        file_root, file_ext = os.path.splitext(original_filename)
        
        # 새 파일 이름 생성 (예: 001_originalFilename.png)
        new_filename = f"{prefix}{current_num:0{num_digits}d}_{original_filename}"
        new_file_path = os.path.join(dir_name, new_filename)
        
        # 파일 이름 충돌 방지
        if os.path.exists(new_file_path):
            print(f"이미 존재하는 파일 이름입니다: {new_filename}. 건너뜁니다.")
            current_num += 1
            continue
        
        # 파일 이름 변경
        os.rename(file_path, new_file_path)
        print(f"파일 이름 변경: {original_filename} -> {new_filename}")
        
        current_num += 1
    
    print("파일 이름 변경 완료.")

# 사용 예시
if __name__ == "__main__":
    # 이미지 파일들이 있는 폴더 경로
    image_folder = '/home/dororo99/patch-extractor-dororo/patch'
    
    # 파일 이름 앞에 넘버링 추가
    rename_files_with_numbering(
        folder_path=image_folder,
        prefix='',              # 원하는 접두사로 변경 가능. 예: 'img_'를 원하면 prefix='img_'
        start_num=1,            # 번호 시작 번호
        num_digits=3,           # 번호의 자릿수 (예: 001, 002, ...)
        extension_filter=['*.png', '*.jpg', '*.jpeg']  # 처리할 파일 확장자
    )
