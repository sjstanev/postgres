from netmiko import ConnectHandler
import ntc_templates
import textfsm
from ntc_templates.parse import parse_output
from pprint import pprint
import json 

vios3 = {
    "device_type": "cisco_ios",
    "host": "10.60.0.236",
    "username": "admin",
    "password": "cisco",
}

# Show command that we execute.
commands = ["show ip arp", "show interface status", "show version", "show cdp neighbor detail"]


with ConnectHandler(**vios3) as net_connect:

    for command in commands:
        output = net_connect.send_command(command, use_textfsm=True)
        print(type(output))
        print(json.dumps(output, indent=2))
