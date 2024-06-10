from discord.ext.commands import Cog, hybrid_command, Context

from utils.bot import MyBot


class HelloCog(Cog):
    def __init__(self, bot: MyBot) -> None:
        self.bot = bot
        self.db = bot.db

    @hybrid_command()
    async def helloworld(self, ctx: Context) -> None:
        """Says hi!"""
        await ctx.send(self.db.get("hello", "hi"))

    @hybrid_command()
    async def sethello(self, ctx: Context, *, message: str) -> None:
        """Sets the hello message"""
        self.db["hello"] = message
        await ctx.send(f"Hello message set to: {message}")


async def setup(bot: MyBot) -> None:
    await bot.add_cog(HelloCog(bot))


async def teardown(bot: MyBot) -> None:
    await bot.remove_cog("HelloCog")
