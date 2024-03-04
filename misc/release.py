# list files in the rules directory

import os
import sys
import yaml


files = os.listdir('rules')
rules = []
for file in files:
    with open('rules/' + file, 'r') as f:
        # parse yaml file and get the content
        content = yaml.safe_load(f)
        rules.append(content)

content = {
    "rules": rules
}

# write file
with open('rules.yaml', 'w') as f:
    yaml.dump(content, f)
    print('rules.yaml has been created')
