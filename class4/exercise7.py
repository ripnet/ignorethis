'''
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
'''

import netmiko

host = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

ssh = netmiko.ConnectHandler(**host)
ssh.send_config_set(['logging buffered 31337'])
print netmiko.ConnectHandler(**host).send_command('show run | i logging buffered')
