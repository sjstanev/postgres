from netmiko import ConnectHandler
import textfsm
import json
from insert_cdpneighbor_module import insert_cdpneihbor
from insert_checked_devices_module import insert_checked_devices
from insert_device_info_module import insert_device_info
from insert_to_check_module import to_check_device


#from ntc_templates.parse import parse_output


vios3 = {
    "device_type": "cisco_ios",
    "host": "10.60.0.236",
    "username": "admin",
    "password": "cisco",
}

device_info = {}

# Show command that we execute.
show_cdp_neighbour = "show cdp neighbor detail"
show_hostname = "show run | s hostname"
show_ip_interface_brief = "show ip interface brief | exclude unassigned"
show_version = "show version"


with ConnectHandler(**vios3) as net_connect:

    # gather common information about connected device
    management_ip_addr = net_connect.send_command(show_ip_interface_brief, use_textfsm=True)
    show_ios_version = net_connect.send_command(show_version, use_textfsm=True)

    # get information about neighbours
    devices = net_connect.send_command(show_cdp_neighbour, use_textfsm=True)

    device_info = {
        "hostname" : show_ios_version[0]["hostname"],
        "uptime" : show_ios_version[0]["uptime"],
        "version" : show_ios_version[0]["version"],
        "software_image" : show_ios_version[0]["software_image"],
        "hardware" : show_ios_version[0]["hardware"][0],
        "serial" : show_ios_version[0]["serial"][0],
        "management_ip" : management_ip_addr[0]["ip_address"],
        "management_intif" : management_ip_addr[0]["interface"]
    }

    # insert gather common information into devices_info table
    insert_device_info(
        hostname = device_info["hostname"],
        uptime = device_info["uptime"],
        version = device_info["version"],
        software_image = device_info["software_image"],
        hardware = device_info["hardware"],
        serial = device_info["serial"],
        management_ip = device_info["management_ip"],
        management_intif = device_info["management_intif"],          
        )

    # insert records into checked_devices
    insert_checked_devices(
        hostname = device_info["hostname"], 
        management_ip = device_info["management_ip"],
        serial = device_info["serial"]
        )

    # loop through all neighbour and records into to_check and cdpneighbors tables
    for device in devices:
        device["hostname"] = device_info["hostname"]

        flag_boolen = "No"


        # insert records into to_check_device
        to_check_device(
            hostname = device["destination_host"], 
            management_ip = device["management_ip"],
            flag = flag_boolen
        )

        # insert records int cdpneighbors talbes
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

        #print(json.dumps(device, indent=2))
print()
net_connect.disconnect()
