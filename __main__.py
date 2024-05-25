import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load the environment variables from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and file != "__init__.py":
            try:
                cog = f"cogs.{file[:-3]}"
                await bot.load_extension(cog)
                print(f"Successfully loaded extension '{cog}'")
            except Exception as e:
                print(f"Failed to load extension '{cog}'. Error: {e}")

@bot.event
async def on_ready():
    await load_cogs()
    print(f"We have logged in as {bot.user}!")

bot.run(TOKEN)
