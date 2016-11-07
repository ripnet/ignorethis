'''
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 
'''

import paramiko

host = '184.105.247.71'
user = 'pyclass'
password = '88newclass'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password, look_for_keys=False)

stdin, stdout, stderr = ssh.exec_command('show version')
for line in stdout.readlines(): #{
    print line.strip()
#}

