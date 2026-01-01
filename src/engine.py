import asyncio
from .triggers.file import FileTrigger
from .triggers.time import TimeTrigger
from .actions.shell import ShellAction
from .actions.python import PythonAction

async def run_rule(rule):
    print(f'Rule: {rule}')
    async def emit(event):
        await action.run({"event": event, "rule": rule.name})

    if rule.trigger.type == "file":
        trigger = FileTrigger(rule.trigger.config["path"])
    elif rule.trigger.type == "time":
        trigger = TimeTrigger(rule.trigger.config["every"])
    else:
        raise ValueError("Unknown trigger")

    if rule.action.type == "shell":
        action = ShellAction(rule.action.config["command"])
    elif rule.action.type == "python":
        action = PythonAction(
            rule.action.config["module"],
            rule.action.config["function"],
        )
    else:
        raise ValueError("Unknown action")

    await trigger.start(emit)
