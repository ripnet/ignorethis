import telnetlib

'''
Shouldn't be using telnet anyway, so why not just hardcode the IP:
'''
hostname = '184.105.247.70'
username = 'pyclass'
password = '88newclass'
t = telnetlib.Telnet(hostname)
t.read_until('sername: ')
t.write(username + "\n")
t.read_until('assword: ')
t.write(password + "\n")
t.read_until('#')
t.write("show ip interface brief\n")
print t.read_until('#')
