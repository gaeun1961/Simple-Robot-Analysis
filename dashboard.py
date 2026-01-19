import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="로봇 데이터 분석 대시보드", layout="wide")
st.title("Robot AI 실시간 데이터 분석 대시보드")

try:
    df = pd.read_csv('robot_trajectory_log.csv')
    df['error'] = df['target_pos'] - df['actual_pos']
    df['abs_error'] = df['error'].abs()
except FileNotFoundError:
    st.error("데이터 파일(robot_trajectory_log.csv)을 찾을 수 없습니다. 먼저 로봇 시뮬레이션을 실행해 주세요.")
    st.stop()

st.sidebar.header("📊 데이터 요약")
avg_err = df['abs_error'].mean()
max_err = df['abs_error'].max()

st.sidebar.metric("평균 오차 (rad)", f"{avg_err:.4f}")
st.sidebar.metric("최대 오차 (rad)", f"{max_err:.4f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("명령값 vs 실제 움직임")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(y=df['target_pos'], name='Target (명령)', line=dict(color='blue', width=2)))
    fig1.add_trace(go.Scatter(y=df['actual_pos'], name='Actual (실제)', line=dict(color='orange', dash='dash')))
    fig1.update_layout(xaxis_title="Time Step", yaxis_title="Position (Radians)")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("시간별 추종 오차 (Error)")
    fig2 = px.line(df, y='error', color_discrete_sequence=['red'])
    fig2.update_layout(xaxis_title="Time Step", yaxis_title="Error (Radians)")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("로봇 관절 속도 변화")
fig3 = px.area(df, y='velocity', color_discrete_sequence=['green'])
st.plotly_chart(fig3, use_container_width=True)

if st.checkbox("Raw Data 확인하기"):
    st.write(df)