from logging import config
import os
import sys
import traceback
from venv import logger
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

# class NonoBot(commands.Bot):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

    
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')
#         for filename in os.listdir('./cogs'):
#             if filename.endswith('.py'):
#                 cog_name = f'cogs.{filename[:-3]}'
#                 try:
#                     self.load_extension(cog_name)
#                     print(f'{cog_name} successfully loaded')
#                 except Exception as e:
#                     print(f'{cog_name} failed to load.', file=sys.stderr)
#                     traceback.print_exc()


# bot = NonoBot(command_prefix="!", intents=intents)
# bot.run(TOKEN)



class DiscordBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger
        self.config = config


    async def load_cogs(self):
        """
        The code in this function is executed whenever the bot will start.
        """
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                    self.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    self.logger.error(
                        f"Failed to load extension {extension}\n{exception}"
                    )




bot = DiscordBot(command_prefix="!", intents=intents)
bot.run(TOKEN)