from ciscoconfparse import CiscoConfParse
import re

config = CiscoConfParse('cisco_ipsec.txt')
maps = config.find_objects_wo_child(parentspec='^crypto map CRYPTO', childspec='AES')
for map in maps: #{
    for child in map.children: #{
        '''
        Why the HELL can't python do this?

        if match = re.search("set transform-set (.*)", child.text):
            do something

        Absurd

        '''
        match = re.search("set transform-set (.*)", child.text)
        if match: #{
            print '%s is using %s' % (map.text, match.group(1))
            break
        #}
    #}
#}
