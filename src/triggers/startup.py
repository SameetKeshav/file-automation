class StartupTrigger:
    async def start(self, emit):
        # Fire once immediately
        await emit({"event": "startup"})
