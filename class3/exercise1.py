import snmp_helper
import yaml
import os
import email_helper
from datetime import datetime

hosts = ['184.105.247.70', #pynet-rtr1
        '184.105.247.71']  #pynet-rtr2

recipient = 'ripnet@gmail.com'

username = 'pysnmp'
auth_key = 'galileo1'          
encrypt_key = 'galileo1'

dataFile = 'iMissCurlyBraces.yml'

oids = {'ccmHistoryRunningLastChanged': '1.3.6.1.4.1.9.9.43.1.1.1.0',   
    'ccmHistoryRunningLastSaved': '1.3.6.1.4.1.9.9.43.1.1.2.0',   
    'ccmHistoryStartupLastChanged': '1.3.6.1.4.1.9.9.43.1.1.3.0',
    'sysUptime': '1.3.6.1.2.1.1.3.0'}

reloadWindow = 30000 # from example solution



if not os.path.isfile(dataFile): #{
    data = {}
#}
else: #{
    with open(dataFile, 'r') as f: #{
        data = yaml.load(f)
    #}
#}


for host in hosts: #{
    hostData = []
    for name, oid in oids.iteritems(): #{
        hostData.append(snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3((host, 161), (username, auth_key, encrypt_key), oid=oid)))
    #}
    
    if host in data: #{
        lastData = data[host]
        if (lastData[0] != hostData[0]) or (hostData[3] < lastData[3] and hostData[0] < reloadWindow): #{
            print "%s changed" % host
            email_helper.send_mail(recipient, "Device %s Changed" % host, "Device %s changed at %s" % (host, datetime.now()), "ripnet@gmail.com")
        #}        

        data[host] = hostData        
    #}
    else: #{
        data[host] = hostData
    #}

#}  

with open(dataFile, 'w') as f: #{
    f.write(yaml.dump(data))
#}

