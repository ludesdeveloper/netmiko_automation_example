#WRITING MORE THAN 1 FILE
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
    try:
        #concate string with device ip address
        write = open('outputs/'+device['host']+'.txt','w')
        net_connect = ConnectHandler(**device)
        print(f"Current Device Ip Address : {device['host']}")
        write.write(f"Current Device Ip Address : {device['host']}\n")
        for command in commands:
            output = net_connect.send_command(command)
            print()
            print(command)
            write.write(command+'\n')
            print()
            print(output)
            write.write(output)
            print()
        write.close()
        net_connect.disconnect()
    except:
        pass
