#WITHOUT ENTER PASSWORD
from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_ios",
    "host": "172.28.100.32",
    "username": "username",
    #remove manual password
    "password": "password",
}

command = "show ip int brief"
#change code flavor
net_connect = ConnectHandler(**cisco1)
output = net_connect.send_command(command)
net_connect.disconnect()

print()
print(output)
print()