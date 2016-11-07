'''
Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).
'''

import netmiko

host = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

ssh = netmiko.ConnectHandler(**host)
ssh.config_mode()
print "Config Mode: %s" % ssh.check_config_mode()

