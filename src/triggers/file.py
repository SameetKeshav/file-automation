import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

class FileTrigger:
    def __init__(self, path):
        self.path = Path(path).expanduser()

    async def start(self, emit):
        loop = asyncio.get_event_loop()

        class Handler(FileSystemEventHandler):
            def on_created(self, event):
                loop.call_soon_threadsafe(
                    lambda: asyncio.create_task(
                        emit({"type": "file", "path": event.src_path})
                    )
                )

        observer = Observer()
        observer.schedule(Handler(), str(self.path), recursive=False)
        observer.start()
