# secrets-rules

## Download rules

To download rules, use
https://github.com/juli1/secrets-rules/releases/latest/download/rules.yml


## Validating rules

To validate a rule, install pajv (`npm install -g pajv`) and then:

```shell
pajv test -s schema.json -d rules/rule.yml --valid

```
