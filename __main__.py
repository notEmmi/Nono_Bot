import os
from dotenv import load_dotenv
import random

import discord
from discord.ext import commands

# Load the environment variables from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with the necessary intents
intents = discord.Intents.default()
intents.message_content = True

# Define the bot and the command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Load the cogs
bot.load_extension("cogs.test")

# Run the bot with the specified token
bot.run(TOKEN)
