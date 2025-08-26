"""
<To Do>
1. patch의 pixel들의 RGB 추출
2. pixel들로 3차원 scatter plot 만들기
"""

import numpy as np
from PIL import Image
import plotly.graph_objs as go
import plotly.offline as pyo

# 이미지 경로 설정
image_path = '/home/dororo99/prof_task/analyze3/low/low_tissue_15360_14336.png' # 이미지의 경로를 입력하세요.

# 이미지 로드
image = Image.open(image_path)

'''
샘플링 사이즈 설정
    - 픽셀 수가 너무 많을 경우 샘플링 수행
'''
sample_size = 10000


# RGB 모드로 변환 (이미지가 RGB가 아닌 경우)
image = image.convert('RGB')

# 이미지를 numpy 배열로 변환
data = np.array(image)
print(data.shape)
print(data.size)
print(data[:,:,0].shape)
# RGB 채널 분리 및 1차원으로 변환
r = data[:, :, 0].flatten()
g = data[:, :, 1].flatten()
b = data[:, :, 2].flatten()
print(r.size)
print(r.shape)

total_pixels = len(r)

# 총 픽셀 수가 샘플 크기보다 크면 샘플링 수행
if total_pixels > sample_size:
    indices = np.random.choice(total_pixels, size=sample_size, replace=False)
    r = r[indices]
    g = g[indices]
    b = b[indices]

# 점의 색상을 실제 RGB 값으로 설정
colors = ['rgb({}, {}, {})'.format(r[i], g[i], b[i]) for i in range(len(r))]

# 3D 산점도 생성
trace = go.Scatter3d(
    x=r,
    y=g,
    z=b,
    mode='markers',
    marker=dict(
        size=2,
        color=colors,
        opacity=0.5,
    )
)

data = [trace]

layout = go.Layout(
    scene=dict(
        xaxis_title='Red Channel',
        yaxis_title='Green Channel',
        zaxis_title='Blue Channel',
        xaxis=dict(range=[0, 255]),
        yaxis=dict(range=[0, 255]),
        zaxis=dict(range=[0, 255]),
    ),
    title='RGB Color Space Scatter Plot',
)

fig = go.Figure(data=data, layout=layout)

# 플롯 표시
pyo.plot(fig)