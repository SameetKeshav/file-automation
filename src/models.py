from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TriggerConfig:
    type: str
    config: Dict[str, Any]

@dataclass
class ActionConfig:
    type: str
    config: Dict[str, Any]

@dataclass
class Rule:
    name: str
    trigger: TriggerConfig
    action: ActionConfig
