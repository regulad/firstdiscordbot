from discord import Intents
from discord.ext.commands import Bot, Context
from dotenv import dotenv_values

# Load the configuration from the .env file
config = dotenv_values()

# Create the Bot
command_prefix = "?"
intents = Intents.default()
bot = Bot(
    command_prefix=command_prefix,
    intents=intents
)


# Add some commands
@bot.hybrid_command()
async def helloworld(ctx: Context) -> None:
    """Says hi!"""
    await ctx.send("Hi!")


# Run the bot
discord_token = config["DISCORD_TOKEN"]
guild_id = int(config["GUILD_ID"])


@bot.event
async def on_ready() -> None:
    """Tell Discord about our slash commands"""
    guild = bot.get_guild(guild_id)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)


bot.run(discord_token)
