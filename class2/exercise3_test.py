from exercise3 import CiscoTelnet

t = CiscoTelnet('184.105.247.70', 'pyclass', '88newclass')
t.login()
t.send_command('show version')


