import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as py

# 读取数据
df_commits = pd.read_csv('commits_data.csv')

# 确保数据的日期列和login列存在
assert 'date' in df_commits.columns, "数据中必须包含'date'列"
assert 'login' in df_commits.columns, "数据中必须包含'login'列"

# 将日期列转换为 datetime 类型，并去除时区信息
df_commits['date'] = pd.to_datetime(df_commits['date']).dt.tz_localize(None)

# 跟踪贡献者的贡献路径
df_commits['year_month'] = df_commits['date'].dt.to_period('M')
contribution_paths = df_commits.groupby(['login', 'year_month']).size().unstack().fillna(0).cumsum(axis=1)

# 创建交互式图表
fig = make_subplots()

for contributor in contribution_paths.index:
    fig.add_trace(go.Scatter(x=contribution_paths.columns.astype(str),
                             y=contribution_paths.loc[contributor],
                             mode='lines',
                             name=contributor,
                             visible='legendonly'))  # 默认隐藏所有贡献者的数据

# 设置图表标题和标签
fig.update_layout(title='贡献者的贡献积累路径',
                  xaxis_title='时间',
                  yaxis_title='累计贡献次数',
                  xaxis_tickangle=-45,
                  showlegend=True)

# 保存图表为本地 HTML 文件
fig.write_html('贡献者的贡献积累路径.html')

print("图表已保存为 '贡献者的贡献积累路径.html'")


