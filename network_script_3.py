#MORE THAN 1 DEVICE
from netmiko import ConnectHandler
#adding devices data in dictionary format inside list/array
devices = [
        {
    "device_type": "cisco_ios",
    "host": "172.28.100.32",
    "username": "username",
    "password": "password",
    },
        {
    "device_type": "cisco_ios",
    "host": "172.28.100.33",
    "username": "username",
    "password": "password",
    },
        {
    "device_type": "cisco_ios",
    "host": "172.28.100.34",
    "username": "username",
    "password": "password",
    },
        {
    "device_type": "cisco_ios",
    "host": "172.28.100.35",
    "username": "username",
    "password": "password",
    },
        {
    "device_type": "cisco_ios",
    "host": "172.28.100.36",
    "username": "username",
    "password": "password",
    },
        {
    "device_type": "cisco_ios",
    "host": "172.28.100.83",
    "username": "username",
    "password": "password",
    },
]

command = "show ip int brief"

#adding loop
for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(command)
    net_connect.disconnect()
    #move print inside loop
    print()
    #adding device ip address
    print(device['host'])
    print(output)
    print()

