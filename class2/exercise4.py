import snmp_helper

hosts = ['184.105.247.70', #pynet-rtr1
        '184.105.247.71']  #pynet-rtr2

oids = ['.1.3.6.1.2.1.1.1.0', #sysDescr
        '.1.3.6.1.2.1.1.5.0'] #sysName

community = 'galileo'

for host in hosts: #{
    print "Host: ", host
    for oid in oids: #{
        print snmp_helper.snmp_extract(snmp_helper.snmp_get_oid((host, community, 161), oid))
    #}
    print
#}
