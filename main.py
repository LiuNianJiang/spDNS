import requests

# 定义远程版本号的URL
version_url = "https://example.com/version.txt"
# 定义hosts文件路径（Windows系统可能是 C:\Windows\System32\drivers\etc\hosts）
hosts_file_path = "/etc/hosts"

# 获取远程版本号
def get_remote_version():
    try:
        response = requests.get(version_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"无法获取远程版本号: {e}")
        return None

# 获取本地版本号
def get_local_version():
    try:
        with open(hosts_file_path, "r") as hosts_file:
            for line in hosts_file:
                if line.startswith("# 版本号:"):
                    return line.strip()[10:]
        return None
    except FileNotFoundError:
        return None

# 同步覆盖解析规则
def sync_hosts():
    remote_version = get_remote_version()
    local_version = get_local_version()

    if remote_version and local_version != remote_version:
        try:
            with open(hosts_file_path, "w") as hosts_file:
                hosts_file.write("# 版本号: " + remote_version + "\n")
                hosts_file.write("# 区域开始\n")
                hosts_file.write("# 在这里添加你的自定义hosts规则\n")
                hosts_file.write("# 区域结束\n")

            print("已更新hosts文件")
        except PermissionError:
            print("无法写入hosts文件，请确保具有管理员权限")
    else:
        print("hosts文件已是最新版本")

if __name__ == "__main__":
    sync_hosts()
