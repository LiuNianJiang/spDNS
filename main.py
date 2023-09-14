import requests

# Define the URL for remote version.
version_url = "https://www.huang1111.cn/test.txt"
# Define the hosts file path
hosts_file_path = "C:\Windows\System32\drivers\etc\hosts"

# Get the remote version
def get_remote_version():
    try:
        response = requests.get(version_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve remote version: {e}")
        return None

# Get the local version
def get_local_version():
    try:
        with open(hosts_file_path, "r") as hosts_file:
            for line in hosts_file:
                if line.startswith("# Version:"):
                    return line.strip()[10:]
        return None
    except FileNotFoundError:
        return None

# Sync and override the parsing rules
def sync_hosts():
    remote_version = get_remote_version()
    local_version = get_local_version()

    if remote_version and local_version != remote_version:
        try:
            with open(hosts_file_path, "w") as hosts_file:
                hosts_file.write("# Version: " + remote_version + "\n")
                hosts_file.write("# Start of the section\n")
                hosts_file.write("# Add your custom host rules here\n")
                hosts_file.write("# End of the section\n")

            print("Hosts file updated")
        except PermissionError:
            print("Failed to write to the hosts file, ensure you have administrator privileges")
    else:
        print("Hosts file is up to date")

if __name__ == "__main__":
    sync_hosts()
