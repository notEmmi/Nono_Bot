import io
import json
import random
import discord
import requests
from discord.ext import commands
from PIL import Image, ImageFilter
from io import BytesIO

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
        super().__init__()

        #load character from JSON file
        with open('data/characters.json', 'r') as f:
            self.characters = json.load(f)
            #{character: {character: [names], url: "image"}}

    @staticmethod
    async def crop_image(ctx, image_url, x, y, width, height):
        
        response = requests.get(image_url)
        image_bytes = io.BytesIO(response.content)

        original_image = Image.open(image_bytes)

        # Determine the region of interest and crop the image
        cropped_image = original_image.crop((x, y, x + width, y + height))

        # Convert the image to bytes
        with BytesIO() as image_bytes:
            cropped_image.save(image_bytes, format='PNG')
            image_bytes.seek(0)

            # Create a Discord file object from the image bytes
            file = discord.File(image_bytes, filename='partial_image.png')

            # Send the partial image to Discord
            await ctx.send(file=file)

    @commands.command(name='gtc')
    async def start_game(self, ctx):
        
        character = random.choice(list(self.characters.keys()))
        character_data =self.characters[character]
        possible_names = character_data["possible_names"]
        image_url = character_data["url"]

        await ctx.send("Who is this?")
        await GuessThatCharacter.crop_image(ctx, image_url,  x=100, y=100, width=100, height=100)






async def setup(bot):
    await bot.add_cog(GuessThatCharacter(bot))