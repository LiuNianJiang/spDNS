import os  
import requests  
import shutil  
  
def request_admin():  
    # 请求管理员权限  
    if os.name == 'nt':  
        if not os.getuid() == 0:  
            print("请使用管理员权限运行此程序")  
            os.system('pause')  
            exit(1)  
  
def get_url_content(url):  
    # 从URL获取内容  
    response = requests.get(url)  
    return response.text  
  
def check_hosts_file(content):  
    # 检查hosts文件是否存在以及是否包含特定内容  
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r") as file:  
        hosts_content = file.read()  
        if content in hosts_content:  
            return True  
    return False  
  
def update_hosts_file(content):  
    # 更新hosts文件  
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r") as file:  
        hosts_content = file.read()  
      
    # 查找版本号  
    version_pattern = re.compile(r"# ver:(\d+\.\d+\.\d+)")  
    version_match = version_pattern.search(content)  
    if version_match:  
        version = version_match.group(1)  
        # 检查版本号是否一致  
        if "# ver:{}".format(version) in hosts_content:  
            return False  
        else:  
            # 不一致，覆盖原先的内容  
            with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w") as file:  
                file.write(content)  
            return True  
    else:  
        # 没有找到版本号，直接添加内容到hosts文件末尾  
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "a") as file:  
            file.write("\n" + content)  
        return True  
  
def main():  
    # 请求管理员权限  
    request_admin()  
    # 获取URL内容  
    url_content = get_url_content("https://www.huang1111.cn/hosts.txt")  
    # 检查hosts文件是否存在以及是否包含特定内容  
    if not check_hosts_file(url_content):  
        # 如果不存在，更新hosts文件  
        update_hosts_file(url_content)  
        print("Hosts文件已成功更新！")  
    else:  
        print("Hosts文件无需更新！")  
  
if __name__ == "__main__":  
    main()
