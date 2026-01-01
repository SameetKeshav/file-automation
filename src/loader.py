import yaml
from .models import Rule, TriggerConfig, ActionConfig

def load_rules(path="rules.yaml"):
    with open(path) as f:
        data = yaml.safe_load(f)

    rules = []
    for rule in data["rules"]:
        rules.append(
            Rule(
                name=rule["name"],
                trigger=TriggerConfig(
                    type=rule["trigger"]["type"],
                    config=rule["trigger"]
                ),
                action=ActionConfig(
                    type=rule["action"]["type"],
                    config=rule["action"]
                ),
            )
        )
    print(f'Rules {rules}')
    return rules
