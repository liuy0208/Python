import requests
import pandas as pd

# GitHub API URL
repo_url = 'https://api.github.com/repos/tensorflow/tensorflow'
contributors_url = f'{repo_url}/contributors'

# 你的GitHub个人访问令牌
token = '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'

# 设置请求头
headers = {'Authorization': f'token {token}'}

# 获取贡献者信息
response = requests.get(contributors_url, headers=headers)
if response.status_code != 200:
    raise Exception('无法获取贡献者信息')
contributors = response.json()

# 存储贡献者提交记录
commits_data = []

# 获取每个贡献者的提交记录
for contributor in contributors:
    login = contributor['login']
    page = 1
    while True:
        commits_url = f'{repo_url}/commits?author={login}&page={page}&per_page=100'
        response = requests.get(commits_url, headers=headers)
        if response.status_code != 200:
            print(f'无法获取贡献者 {login} 的提交记录，状态码: {response.status_code}')
            break
        commits = response.json()
        if not commits:  # 如果没有更多提交记录，则停止分页
            break
        for commit in commits:
            commit_date = commit['commit']['committer']['date']
            commits_data.append({'login': login, 'date': commit_date})
        page += 1  # 进入下一页

# 保存数据
df_commits = pd.DataFrame(commits_data)
df_commits.to_csv('commits_data_all.csv', index=False)

print('数据已成功保存到 commits_data.csv')
