from netmiko import ConnectHandler
import datetime
from datetime import datetime
import getpass
import ipaddress
t = datetime.now()

#devices = []
ip_addr = ""

username = "tcsadmin"
pwd = "tcsadmin9400"
"""
username = "admin"
pwd = "P@ssw0rd"
username = input("user: ")
pwd = getpass.getpass(prompt="password: ", stream=None)

with open('ip list.txt') as file:
    lines = file.read().splitlines()
    print(lines)
"""

def ssh_mc(cmd, ip_addr):
    # Establish SSH connection
    try:
        #for device in devices:
        aruba_device = {
            'device_type': 'aruba_os',
            'ip': ip_addr,
            'username': username,
            'password': pwd,
        }
        ssh_connection = ConnectHandler(**aruba_device)
        print("SSH connection successful.\n")

        # You can now send commands using ssh_connection.send_command() or enter an interactive shell with ssh_connection.send_interactive()
        # Example:
        ssh_connection.send_command('no paging')
        output = ssh_connection.send_command(cmd)
        return output

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the SSH connection
        ssh_connection.disconnect()
        print("SSH connection closed.")