
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
    @commands.hybrid_commands(name="games")
    async def games():
        



async def setup(bot):
    await bot.add_cog(Basic_Commands(bot))