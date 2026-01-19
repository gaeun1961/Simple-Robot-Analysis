# Simple-Robot-Analysis

PyBullet 시뮬레이션을 활용하여 로봇 관절의 움직임 데이터를 수집
Streamlit 대시보드를 통해 명령값과 실제 센서값 사이의 오차를 분석

## Tech Stack
- **Language**: Python
- **Simulation**: PyBullet
- **Data Analysis**: Pandas, Matplotlib
- **Dashboard**: Streamlit, Plotly

## 주요 기능
1. **Data Collection**: 가상 로봇 팔의 관절 궤적 데이터 추출
2. **Analysis**: 목표 궤적 대비 실제 추종 오차(Tracking Error) 계산
3. **Visualization**: 인터랙티브 웹 대시보드를 통한 실시간 데이터 시각화