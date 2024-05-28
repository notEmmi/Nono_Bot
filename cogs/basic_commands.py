
from discord.ext import commands

"""
    basic_commands.py
    Contains basic commands such as

"""


class Basic_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # Write Functions here
    @commands.command()
    async def games(self, ctx):
        pass
    
        



async def setup(bot):
    await bot.add_cog(Basic_Commands(bot))