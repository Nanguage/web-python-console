from imjoy_rpc import api


class Plugin:
    async def setup(self):
        print("setup")

    async def run(self, ctx):
        print("run")
        print(ctx)

api.export(Plugin())
