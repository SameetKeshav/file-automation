import asyncio

class TimeTrigger:
    def __init__(self, every: int):
        self.every = every

    async def start(self, emit):
        while True:
            await asyncio.sleep(self.every)
            await emit({"type": "time"})
