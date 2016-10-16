from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco_ipsec.txt')
maps = config.find_objects("^crypto map CRYPTO")
for map in maps: #{
    print map.text
    for child in map.children: #{
        print child.text
    #}
#}
