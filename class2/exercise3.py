import telnetlib

class CiscoTelnet: #{
    def __init__(self, hostname, username, password): #{
        self.hostname = hostname
        self.username = username
        self.password = password
        self.t = telnetlib.Telnet(self.hostname)
    #}
    
    def login(self): #{
        self.t.read_until('sername: ')
        self.t.write(self.username + "\n")
        self.t.read_until('assword: ')
        self.t.write(self.password + "\n")
        self.t.read_until('#')
        self.t.write("term len 0\n")
        self.t.read_until('#')
        return self
    #}

    def send_command(self,command): #{
        self.t.write(command + "\n")
        print self.t.read_until('#')
        return self
    #}
#}
