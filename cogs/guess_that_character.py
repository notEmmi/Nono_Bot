import json
import random
from discord.ext import commands


"""
Rules

!guessthatcharacter to start game

the bot will send a zoomed in picture of a [character]
the players must guess the name of the character using the image
the bot ignores letter cases

possibly add a point system?? maybe idk

!zoomout to get a less zoomed in image

"""

class GuessThatCharacter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #load character from JSON file
        with open('data/characters.json', 'r') as f:
            self.caracters = json.load(f)

    
    @commands.command(name='guessthatcharacter')
    async def start_game(self, ctx):
        
        character, image = random.choice(list(self.characters.items()))

        await ctx.send("Who is this character? ")
        await ctx.send(image)


def setup(bot):
    bot.add_cog(GuessThatCharacter(bot))