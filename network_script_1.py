#COPY PASTE FROM NETMIKO
#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "172.28.100.32",
    "username": "username",
    "password": getpass(),
}

# Show command that we execute
command = "show ip int brief"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()