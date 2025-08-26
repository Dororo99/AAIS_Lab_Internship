## 주요 기능

### 1. 이미지 특성 분석 및 시각화 (plt.ipynb)
- RGB 채널의 공분산 행렬 계산
- 고유값과 고유벡터 분석
- 이미지 특성을 기반으로 한 산점도 생성
- 결과를 CSV 파일로 저장

### 2. 고유벡터 기반 투영 분석 (project.ipynb)
- 첫 번째, 두 번째, 세 번째 고유벡터를 기준으로 하는 평면에 데이터 투영
- 각 투영에 대한 2D 시각화 제공
- RGB 색상 정보를 유지한 산점도 생성

### 3. 3D RGB 산점도 (3d_scatter_plot.py)
- 이미지의 RGB 픽셀값을 3차원 공간에 시각화
- 대용량 이미지 처리를 위한 샘플링 기능
- Plotly를 사용한 인터랙티브 3D 시각화

## 사용 방법

1. 필요한 라이브러리 설치: 
bash pip install numpy pandas matplotlib opencv-python pillow plotly

2. 이미지 경로 설정:
- 각 스크립트의 `image_path` 변수를 분석하고자 하는 이미지 경로로 수정

3. 스크립트 실행:
- Jupyter Notebook: `plt.ipynb`, `project.ipynb` 실행
- Python 스크립트: `python 3d_scatter_plot.py` 실행

## 주요 라이브러리
- NumPy: 행렬 연산 및 데이터 처리
- Pandas: 데이터 프레임 처리 및 CSV 저장
- Matplotlib: 2D 시각화
- OpenCV: 이미지 처리
- Plotly: 3D 시각화
- PIL: 이미지 로딩 및 처리

## 출력 결과
- 이미지 특성 데이터 (CSV)
- 2D 산점도 (고유벡터 투영)
- 3D RGB 산점도 (인터랙티브)