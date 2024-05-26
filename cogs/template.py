
from discord.ext import commands

"""
    template.py
    Serves as a template for building cogs.

"""


class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # Write Functions here


async def setup(bot):
    await bot.add_cog(Template(bot))