import snmp_helper
import time
import pygal

ifIndex = 5
oids = ['1.3.6.1.2.1.2.2.1.10.',
    '1.3.6.1.2.1.2.2.1.11.',
    '1.3.6.1.2.1.2.2.1.16.',
    '1.3.6.1.2.1.2.2.1.17.']

username = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

host = '184.105.247.70'

outputPackets = 'exercise2_packets.svg'
outputOctets = 'exercise2_octets.svg'

stats = [[],[],[],[]]
xAxis = []
baseStat = [0, 0, 0, 0]
iteration = 0

def gatherData(iteration): #{
    xAxis.append(time.strftime('%l:%M%p'))
    for idx, oid in enumerate(oids): #{
        oid = oid + str(ifIndex)
        data = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3((host, 161), (username, auth_key, encrypt_key), oid=oid))
        data = int(data)
        if iteration == 0: #{
            baseStat[idx] = data
        #}
        elif iteration >= 1: #{
            stats[idx].append(data - baseStat[idx])
            baseStat[idx] = data
        #}
    #}
    
    #iteration++ FU python 
    iteration += 1
    return iteration
#}

while iteration <= 13:
    iteration = gatherData(iteration)
    time.sleep(300)

chart = pygal.Line(include_x_axis=True)
chart.x_labels = xAxis
chart.add('ifInOctets', stats[0])
chart.add('ifOutOctets', stats[2])
chart.render_to_file(outputOctets)

chart = pygal.Line(include_x_axis=True)
chart.x_labels = xAxis
chart.add('ifInUcastPkts', stats[1])
chart.add('ifOutUcastPkts', stats[3])
chart.render_to_file(outputPackets)
