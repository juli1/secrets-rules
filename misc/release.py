import os
import yaml

# Read all the rules and add them to the list
files = os.listdir('rules')
rules = {}
for file in files:
    with open('rules/' + file, 'r') as f:
        # parse yaml file and get the content
        content = yaml.safe_load(f)
        rules[content['id']] = content


# write file
with open('rules.yml', 'w') as f:
    yaml.dump(rules, f)
    print('rules.yaml has been created')
