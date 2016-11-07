'''
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
'''

import pexpect, time

host = '184.105.247.71'
user = 'pyclass'
password = '88newclass'

ssh = pexpect.spawn('ssh %s@%s' % (user, host))

ssh.expect('d:')

def c(s): #{
    ssh.sendline(s)
    ssh.expect('#')
#}
def d(s): #{
    return s[s.find("\n")+1:s.rfind("\n")]
#}
c(password)
c('term len 0')
c('sh ip int br')
print d(ssh.before)

