'''
Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change by examining the output of 'show run'.
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
c('conf t')
c('logging buffered 31337')
c('end')
c('sh run | i logging buffered')
print d(ssh.before)

