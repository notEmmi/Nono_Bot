import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load the environment variables from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())


async def main():

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}!')
        print("─────────────────────")

    for file in os.listdir("./cogs"):
        if file.endswith(".py") and file!="__init__.py":
            try:
                cog = f"cogs.{file[:-3]}"
                await bot.load_extension(cog)
                print(f"Sucessfully loaded extension '{cog}'")
                print("─────────────────────")
            except Exception as e:
                print(f"Failed to load etension '{cog}'. Error: {e}")
                print("─────────────────────")


    # Run bot
    try:
        print("Running bot")
        print("─────────────────────")
        await bot.start(TOKEN)
        print("Bot Run successfully.")
        print("─────────────────────")
    except discord.LoginFailure:
        print("Invalid token")
        print("─────────────────────")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("─────────────────────")

asyncio.run(main())
