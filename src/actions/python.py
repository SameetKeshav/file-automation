import importlib

class PythonAction:
    def __init__(self, module, function):
        self.module = module
        self.function = function

    async def run(self, context):
        print(f'Running python script {context}')
        mod = importlib.import_module(self.module)
        fn = getattr(mod, self.function)
        result = fn(context)
        if hasattr(result, "__await__"):
            await result
