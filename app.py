import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 页面配置：设置为宽屏模式
st.set_page_config(layout="wide", page_title="工程数据仿真中心")

st.title("🚀 工业信号仿真与建模分析平台")
st.markdown("---")

# --- 侧边栏：参数配置 ---
with st.sidebar:
    st.header("🎛️ 模型参数设置")
    # 基础正弦波参数
    freq = st.slider("信号频率 (Hz)", 1, 50, 10)
    amp = st.slider("振幅", 0.1, 5.0, 1.0)
    
    # 噪声控制
    noise_level = st.select_slider("环境噪声水平", options=['无', '低', '中', '高'])
    noise_map = {'无': 0, '低': 0.1, '中': 0.3, '高': 0.6}
    
    st.header("📈 数学建模选项")
    show_trend = st.checkbox("显示拟合趋势线", value=True)
    forecast_days = st.number_input("预测未来步数", 10, 100, 20)

# --- 主界面布局 ---
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("实时信号仿真图")
    
    # 生成数据
    t = np.linspace(0, 1, 500)
    clean_signal = amp * np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, noise_map[noise_level], size=len(t))
    raw_data = clean_signal + noise
    
    # 使用 Plotly 绘制高颜值交互图
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=raw_data, name='原始信号', line=dict(color='#1f77b4', width=1)))
    
    if show_trend:
        # 简单的滑动平均模拟趋势
        trend = pd.Series(raw_data).rolling(window=20).mean()
        fig.add_trace(go.Scatter(x=t, y=trend, name='平滑趋势', line=dict(color='red', width=2)))
    
    fig.update_layout(template="plotly_white", margin=dict(l=0, r=0, t=0, b=0), height=500)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("数据统计指标")
    # 计算一些工程常用指标
    rms = np.sqrt(np.mean(raw_data**2))
    p2p = np.max(raw_data) - np.min(raw_data)
    
    st.metric("均方根 (RMS)", f"{rms:.3f}")
    st.metric("峰峰值 (P2P)", f"{p2p:.3f}")
    
    st.markdown("---")
    st.write("📝 **分析结论**")
    if rms > 2.0:
        st.error("警告：信号能量超过安全阈值！")
    else:
        st.success("信号运行状态正常。")

# --- 底部：文件上传与数据分析 ---
st.markdown("---")
tab1, tab2 = st.tabs(["📂 数据导出", "🧬 频谱分析 (FFT)"])

with tab1:
    # 允许用户下载生成的数据
    df = pd.DataFrame({'Time': t, 'Signal': raw_data})
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("下载模拟数据为 CSV", csv, "sim_data.csv", "text/csv")
    st.dataframe(df.head(10), use_container_width=True)

with tab2:
    # 快速傅里叶变换，展示建模深度
    fft_vals = np.abs(np.fft.fft(raw_data))[:250]
    fft_freq = np.fft.fftfreq(len(t), t[1]-t[0])[:250]
    
    fig_fft = go.Figure(go.Bar(x=fft_freq, y=fft_vals, marker_color='#2ca02c'))
    fig_fft.update_layout(height=300, title="频谱图 (Frequency Domain)")
    st.plotly_chart(fig_fft, use_container_width=True)