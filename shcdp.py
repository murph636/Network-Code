from netmiko import ConnectHandler
import getpass
import subprocess

username = ""
password = ""
#DEVICE_TYPE = 'cisco_nxos'
#DEVICE_TYPE = 'cisco_asa'
DEVICE_TYPE = 'cisco_ios'
#DEVICE_TYPE = 'cisco_xe'
ip = '10.81.0.1'

net_connect = ConnectHandler(ip=ip, username=username,
                                     password=password,
                                     device_type=DEVICE_TYPE)
device_info = net_connect.send_command('sh cdp neighbors detail | inc Device')

print(device_info)
 
