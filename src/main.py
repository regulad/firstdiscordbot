from discord import Intents
from discord.ext.commands import Bot
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


# Run the bot
discord_token = config["DISCORD_TOKEN"]
bot.run(discord_token)
