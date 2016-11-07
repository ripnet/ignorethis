'''
Bonus Question - Redo exercise6 but have the SSH connections happen concurrently using either threads or processes (see example). What main issue is there with using threads in Python?
'''

import netmiko, multiprocessing

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

def worker(host, queue): #{
    queue.put("Host: %s\n%s" % (host['ip'], netmiko.ConnectHandler(**host).send_command('show arp')))
#}

queue = multiprocessing.Queue()
processes = []
for host in hosts: #{
    p = multiprocessing.Process(target=worker, args=(host, queue))
    processes.append(p)
    p.start()
#}
for p in processes: #{
    p.join()
    print queue.get()
    print
#}

