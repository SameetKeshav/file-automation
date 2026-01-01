import asyncio

class ShellAction:
    def __init__(self, command: str):
        self.command = command

    async def run(self, context):
        print(f'Shell script {context}')
        proc = await asyncio.create_subprocess_shell(
            self.command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        print(stdout.decode(), stderr.decode())
