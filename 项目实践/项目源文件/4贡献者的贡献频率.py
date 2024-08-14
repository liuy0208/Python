import pandas as pd
import plotly.express as px

# 读取数据
df_commits = pd.read_csv('commits_data.csv')

# 确保数据的日期列和login列存在
assert 'date' in df_commits.columns, "数据中必须包含'date'列"
assert 'login' in df_commits.columns, "数据中必须包含'login'列"

# 将日期列转换为 datetime 类型并设置时区为 UTC
df_commits['date'] = pd.to_datetime(df_commits['date']).dt.tz_convert('UTC')

# 设置日期为索引
df_commits.set_index('date', inplace=True)

# 计算每日贡献者数量
daily_contributions = df_commits.groupby(['login']).resample('D').size().reset_index(name='contributions')

# 计算每月的总贡献次数
monthly_contributions = daily_contributions.set_index('date').groupby(['login']).resample('M')['contributions'].sum().reset_index()

print(daily_contributions.head())
print(monthly_contributions.head())

# 汇总每个贡献者的总贡献次数
total_contributions = daily_contributions.groupby('login')['contributions'].sum()

print(total_contributions.head())

# 使用Plotly绘制交互式图表
fig = px.line(monthly_contributions, x='date', y='contributions', color='login',
              title='贡献者的贡献频率',
              labels={'date': '时间', 'contributions': '贡献次数', 'login': '贡献者'})

fig.update_layout(legend_title_text='贡献者')

# 保存图表为本地 HTML 文件
fig.write_html('贡献者的贡献频率.html')

print("图表已保存为 '贡献者的贡献频率.html'")

