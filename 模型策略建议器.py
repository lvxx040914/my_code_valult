import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="工业产值与碳排放分析", layout="wide")

st.title("📊 工业行业产值数据分析系统")

# --- 1. 数据上传 ---
uploaded_file = st.sidebar.file_uploader("上传《按行业分工业总产值》CSV/Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    @st.cache_data
    def load_data(file):
        # 尝试读取数据，跳过统计年鉴常见的说明行
        try:
            # 针对 CSV 格式
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
            
            # --- 自动清洗：统计年鉴通常第一列是行业名称 ---
            # 去除全空行和全空列
            df = df.dropna(how='all').dropna(axis=1, how='all')
            return df
        except Exception as e:
            st.error(f"读取文件失败: {e}")
            return None

    data = load_data(uploaded_file)

    if data is not None:
        st.success(f"成功加载文件：{uploaded_file.name}")
        
        # 让用户指定“维度列”（比如是哪一列包含行业名称，通常是第一列）
        columns = data.columns.tolist()
        index_col = st.sidebar.selectbox("选择包含‘行业’或‘年份’的列", columns, index=0)
        
        # --- 2. 数据处理：将行业名称设为索引 ---
        plot_df = data.copy()
        # 排除非数值列用于绘图
        numeric_cols = plot_df.select_dtypes(include=['number']).columns.tolist()
        
        # --- 3. 可视化布局 ---
        tab1, tab2 = st.tabs(["📉 行业产值对比", "🧩 数据探索"])

        with tab1:
            st.subheader("行业产值横向对比")
            # 选择要展示的指标（比如：总产值、增加值等）
            if numeric_cols:
                target_metric = st.selectbox("选择产值指标", numeric_cols)
                
                # 排序并取 Top N 防止图表太挤
                top_n = st.slider("显示行业数量", 5, len(plot_df), 15)
                chart_data = plot_df.sort_values(by=target_metric, ascending=False).head(top_n)

                fig_bar = px.bar(
                    chart_data, 
                    x=index_col, 
                    y=target_metric,
                    color=target_metric,
                    title=f"各行业 {target_metric} 排名",
                    color_continuous_scale='Sunset'
                )
                fig_bar.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig_bar, use_container_width=True)
                
                # 饼图展示结构占比
                st.subheader("产值构成占比")
                fig_pie = px.pie(chart_data, names=index_col, values=target_metric)
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.warning("未在文件中找到数值型数据，请检查数据格式。")

        with tab2:
            st.write("原始数据预览：")
            st.dataframe(data, use_container_width=True)
            
            # 提供数据下载，方便建模使用
            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button("导出清洗后的数据", csv, "cleaned_industrial_data.csv", "text/csv")

else:
    st.info("💡 请在侧边栏上传《按行业分的规模以上工业企业总产值》文件。")
    st.markdown("""
    ### 建模提示：
    1. **问题1关联**：利用此数据识别哪些是“高产值、高排放”行业，构建分类分级指标。
    2. **问题2关联**：将行业总产值作为自变量引入 STIRPAT 模型，分析产业结构对碳排放的影响。
    """)