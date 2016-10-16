import yaml
import json

myLanguages = [
    'PHP',
    'C',
    'C++',
    'Java',
    'JavaScript',
    {
        'name': 'Python',
        'leastFavorite': True,
    },
    'asm',
]

with open('exercise6.yml', 'w') as y: #{
    y.write(yaml.dump(myLanguages, default_flow_style=False))
#}


with open('exercise6.json', 'w') as j: #{
    json.dump(myLanguages, j)
#}
