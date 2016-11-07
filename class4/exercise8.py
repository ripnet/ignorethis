'''
Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).
'''

import netmiko

configFile = 'exercise8.txt'
hosts = [
    {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.70',
        'username': 'pyclass',
        'password': '88newclass',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': '88newclass',
    },
]

for host in hosts: #{
    print "Host: %s" % host['ip']
    ssh = netmiko.ConnectHandler(**host)
    ssh.send_config_from_file(config_file=configFile)
    print ssh.send_command('show run | i logging')
    print
#}
