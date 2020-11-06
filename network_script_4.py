#MORE THAN 1 COMMAND
from netmiko import ConnectHandler
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
#convert command to list of commands
commands = ["show ip int brief", "show run", "show ver"]
for device in devices:
    net_connect = ConnectHandler(**device)
    #for easier read output, put print host outside commands loop
    print(f"Current Device Ip Address : {device['host']}")
    #create loop for commands
    for command in commands:
        output = net_connect.send_command(command)
        print()
        #we print command for easier output readability
        print(command)
        print()
        print(output)
        print()
    #we will disconnect after all commands send to device
    net_connect.disconnect()
