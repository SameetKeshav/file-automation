import asyncio
from .loader import load_rules
from .engine import run_rule

async def main():
    print('Starting System...')
    rules = load_rules()
    tasks = [asyncio.create_task(run_rule(r)) for r in rules]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
