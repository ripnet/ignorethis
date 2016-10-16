import yaml
import json
from pprint import pprint


pprint(yaml.load(open('exercise6.yml')))
print "\n"
pprint(json.load(open('exercise6.json')))
