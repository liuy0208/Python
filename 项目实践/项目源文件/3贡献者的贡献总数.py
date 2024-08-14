import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'

# 读取数据
df_commits = pd.read_csv('commits_data.csv')

# 确保数据的日期列和login列存在
assert 'date' in df_commits.columns, "数据中必须包含'date'列"
assert 'login' in df_commits.columns, "数据中必须包含'login'列"

# 将日期列转换为 datetime 类型
df_commits['date'] = pd.to_datetime(df_commits['date'])

# 计算每个贡献者的总贡献数
contributor_activity = df_commits.groupby('login').size().sort_values(ascending=False)

# 绘制贡献频率图
plt.figure(figsize=(14, 7))
contributor_activity.plot(kind='bar')
plt.title('贡献者的贡献总数')
plt.xlabel('贡献者')
plt.ylabel('贡献总数')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()




