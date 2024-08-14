import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

# 读取数据
df_commits = pd.read_csv('commits_data.csv')

# 将日期列转换为 datetime 类型
df_commits['date'] = pd.to_datetime(df_commits['date'])

# 提取日期的点钟和星期
df_commits['hour'] = df_commits['date'].dt.hour
df_commits['day_of_week'] = df_commits['date'].dt.day_name()

# 按小时统计贡献数
hourly_activity = df_commits.groupby('hour').size()

# 绘制活跃周期图
plt.figure(figsize=(12, 6))
plt.bar(hourly_activity.index, hourly_activity.values)
plt.title('按小时统计项目活跃情况')
plt.xlabel('小时')
plt.ylabel('贡献次数')
plt.grid(True)
plt.tight_layout()
plt.show()

# 按星期统计贡献数
weekly_activity = df_commits.groupby('day_of_week').size()
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# 将星期英文标签映射到中文
week_mapping = {
    'Monday': '星期一',
    'Tuesday': '星期二',
    'Wednesday': '星期三',
    'Thursday': '星期四',
    'Friday': '星期五',
    'Saturday': '星期六',
    'Sunday': '星期天'
}
weekly_activity.index = weekly_activity.index.map(week_mapping)
# 按星期顺序重新排序
order = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
weekly_activity = weekly_activity.reindex(order)

# 绘制活跃周期图
plt.figure(figsize=(12, 6))
plt.bar(weekly_activity.index, weekly_activity.values)
plt.title('按星期统计项目活跃情况')
plt.xlabel('星期')
plt.ylabel('贡献次数')
plt.grid(True)
plt.tight_layout()
plt.show()
