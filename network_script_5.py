#WRITING FILE
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
commands = ["show ip int brief", "show run", "show ver"]
for device in devices:
    #open file
    write = open('outputs/output.txt','w')
    net_connect = ConnectHandler(**device)
    print(f"Current Device Ip Address : {device['host']}")
    #write ip address to file
    write.write(f"Current Device Ip Address : {device['host']}\n")
    for command in commands:
        output = net_connect.send_command(command)
        print()
        print(command)
        #write command to file
        write.write(command+'\n')
        print()
        print(output)
        #write show output to file
        write.write(output)
        print()
    #close file
    write.close()
    net_connect.disconnect()
