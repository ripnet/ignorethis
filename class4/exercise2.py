'''
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
'''

import paramiko, time

host = '184.105.247.71'
user = 'pyclass'
password = '88newclass'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password, look_for_keys=False)
shell = ssh.invoke_shell()
def c(s): #{
    b = ''
    shell.send(s + "\n")
    time.sleep(1)
    while not b.endswith('#'): #{
        b += shell.recv(1024)
    #}
    return b
#}

c('conf t')
c('logging buffered 31337')
c('end')
print c('show run | i logging buffered')

