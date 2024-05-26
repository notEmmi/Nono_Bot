
from discord.ext import commands

"""
    test.py
    File intended for testing and learning functionality only.

"""

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # Write Test functionality here


async def setup(bot):
    await bot.add_cog(Test(bot))