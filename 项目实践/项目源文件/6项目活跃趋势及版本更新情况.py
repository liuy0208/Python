import requests
import pandas as pd

# GitHub API URL
repo_url = 'https://api.github.com/repos/tensorflow/tensorflow'
releases_url = f'{repo_url}/releases'

# 你的GitHub个人访问令牌
token = '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'

# 设置请求头
headers = {'Authorization': f'token {token}'}

# 存储版本号和发布时间
release_data = []
page = 1
while True:
    response = requests.get(f'{releases_url}?page={page}&per_page=100', headers=headers)
    if response.status_code != 200:
        raise Exception('无法获取版本信息')
    releases = response.json()
    if not releases:  # 如果没有更多数据，停止循环
        break
    for release in releases:
        version = release['tag_name']
        publish_date = release['published_at']
        release_data.append({'version': version, 'publish_date': publish_date})
    page += 1  # 进入下一页

# 保存数据
df_releases = pd.DataFrame(release_data)
df_releases['publish_date'] = pd.to_datetime(df_releases['publish_date'])
df_releases.to_csv('tensorflow_releases.csv', index=False)

print('数据已成功保存到 tensorflow_releases.csv')

import pandas as pd
import matplotlib.pyplot as plt

# 读取项目活跃度数据
df_commits = pd.read_csv('commits_data.csv')
df_commits['date'] = pd.to_datetime(df_commits['date'])
df_commits['month'] = df_commits['date'].dt.to_period('M')
monthly_activity = df_commits.groupby('month').size()

# 读取版本更新数据
df_releases = pd.read_csv('tensorflow_releases.csv')
df_releases['publish_date'] = pd.to_datetime(df_releases['publish_date'])
df_releases['month'] = df_releases['publish_date'].dt.to_period('M')

# 绘制项目活跃度图表
plt.rcParams['font.family'] = 'SimHei'
plt.figure(figsize=(12, 6))
plt.plot(monthly_activity.index.astype(str), monthly_activity.values, marker='o', label='项目活跃度')

# 在图表上添加版本更新的散点
for index, row in df_releases.iterrows():
    plt.scatter(row['month'].strftime('%Y-%m'), 0, color='red', label='版本更新情况' if index == 0 else "")

# 设置标题和标签
plt.title('项目活跃趋势及版本更新情况')
plt.xlabel('月份')
plt.ylabel('贡献次数')
plt.legend()

# 简化 x 轴标签显示数量
xticks = [str(date) for date in monthly_activity.index][::3]
plt.xticks(ticks=xticks, labels=xticks, rotation=45, fontsize=8)

plt.grid(True)
plt.tight_layout()
plt.show()



