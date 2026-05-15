import plotly.express as px
import seaborn as sns

# 加载经典数据集
df = sns.load_dataset('iris')

# 创建一个带趋势线和边际分布的高级图表
fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                 color="species",
                 marginal_y="violin",           # 侧边显示小提琴图
                 marginal_x="box",             # 底部显示箱线图
                 trendline="ols",              # 自动拟合回归线
                 template="plotly_white",      # 使用纯白干净背景
                 color_discrete_sequence=px.colors.qualitative.Prism) # 使用 Prism 高级配色

fig.update_layout(title_font_size=24, font_family="Arial")
fig.show()