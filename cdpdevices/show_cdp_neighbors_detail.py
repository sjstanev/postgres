from netmiko import ConnectHandler
import textfsm
import json
from insert_cdpneighbor_module import insert_cdpneihbor

#from ntc_templates.parse import parse_output


vios3 = {
    "device_type": "cisco_ios",
    "host": "10.60.0.236",
    "username": "admin",
    "password": "cisco",
}

# Show command that we execute.
show_cdp_neighbour = "show cdp neighbor detail"
show_hostname = "show run | s hostname"


with ConnectHandler(**vios3) as net_connect:

    devices = net_connect.send_command(show_cdp_neighbour, use_textfsm=True)
    hostname = net_connect.send_command(show_hostname)
    device_hostname = hostname.split(" ")


    #print(json.dumps(output, indent=2))

    for device in devices:
        device["hostname"] = device_hostname[1]
        insert_cdpneihbor([
            (
        	device["hostname"],
            device["destination_host"],
            device["management_ip"],
            device["platform"],
            device["remote_port"],
            device["local_port"],
            device["software_version"],
            device["capabilities"],
            ),
        ])
        print(json.dumps(device, indent=2))

net_connect.disconnect()
