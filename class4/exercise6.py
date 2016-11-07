'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''

import netmiko

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
    {
        'device_type': 'juniper',
        'ip': '184.105.247.76',
        'username': 'pyclass',
        'password': '88newclass',
    }
]

for host in hosts: #{
    print "Host: %s" % host['ip']
    print netmiko.ConnectHandler(**host).send_command('show arp')
    print
#}
