import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df_commits = pd.read_csv('commits_data.csv')

# 将日期列转换为 datetime 类型
df_commits['date'] = pd.to_datetime(df_commits['date'])

# 按月统计贡献数
df_commits['month'] = df_commits['date'].dt.to_period('M')
monthly_activity = df_commits.groupby('month').size()

# 绘制时间趋势图
plt.rcParams['font.family'] = 'SimHei'
plt.figure(figsize=(12, 6))

# 绘制数据
plt.plot(monthly_activity.index.astype(str), monthly_activity.values, marker='o')

# 设置标题和标签
plt.title('项目活跃趋势')
plt.xlabel('月份')
plt.ylabel('贡献次数')

# 简化 x 轴标签显示数量
xticks = [str(date) for date in monthly_activity.index][::3]  # 每隔三个月显示一次标签
plt.xticks(ticks=xticks, labels=xticks, rotation=45, fontsize=8)  # 调整标签字体大小

plt.grid(True)
plt.tight_layout()
plt.show()

