import requests



def compare_versions(version1, version2):
    if version1.startswith("v"):
        version1 = version1[1:]
    if version2.startswith("v"):
        version2 = version2[1:]
    print(version1, version2)
    v1 = list(map(int, version1.split(".")))
    v2 = list(map(int, version2.split(".")))
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        return 0

class updater():
    VERSION = 'v2.0.2'
    UPDATE_LOG = '修复进度条bug，修复图标显示bug，优化部分图标。服务端重新维护路径，目前可保证unix兼容性'
    github_url = 'https://api.github.com/repos/izumidonabe/MCEasySync/releases/latest'
    kkgithub_url = 'https://api.kkgithub.com/repos/izumidonabe/MCEasySync/releases/latest'
    use_kkgithub = False # 使用 kkgithub 代替 github来尝试加速



    def update(self):
        try:
            response = requests.get(self.github_url)
            response.raise_for_status()  # 检查请求是否成功
            json_data = response.json()  # 解析 JSON 数据
        except requests.exceptions.RequestException as e:
            print("请求失败:", e)
            print("尝试使用 kkgithub")
            try:
                response = requests.get(self.kkgithub_url)
                response.raise_for_status()  # 检查请求是否成功
                json_data = response.json()  # 解析 JSON 数据
                self.use_kkgithub = True
            except requests.exceptions.RequestException as e:
                print("kkgithub 请求失败:", e)
                return None

        download_url = json_data['assets'][0]["browser_download_url"]
        if self.use_kkgithub:
            download_url = download_url.replace("github", "kkgithub")


        if compare_versions(self.VERSION, json_data['tag_name']) == -1:
            return json_data['tag_name'], json_data['body'],download_url # 返回最新版本号和更新日志和下载链接

        return None