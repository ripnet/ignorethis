from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco_ipsec.txt')
maps = config.find_objects_w_child(parentspec='^crypto map CRYPTO', childspec='pfs group2')
for map in maps: #{
    print map.text
#}
