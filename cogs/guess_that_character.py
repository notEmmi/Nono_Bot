import io
import json
import random
import discord
import requests
from discord.ext import commands
from PIL import Image
from io import BytesIO

"""
Rules

!gtc to start game

the bot will send a zoomed in picture of a [character]
the players must guess the name of the character using the image
the bot ignores letter cases, but name must be spelled correctly!! 
different names for the character will be accepted if the character has different names, but not always!!

!zoomout to get a less zoomed in picture



for later: possibly add a point system?? maybe idk


"""


class GuessThatCharacter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_game = None

        # Load characters from JSON file
        with open('data/characters.json', 'r') as f:
            self.characters = json.load(f)
            # {character: {character: [names], url: "image"}}

    @staticmethod
    async def crop_image(image_url, zoom_level):
        response = requests.get(image_url)
        image_bytes = io.BytesIO(response.content)
        original_image = Image.open(image_bytes)

        width, height = original_image.size
        zoom_width, zoom_height = width // zoom_level, height // zoom_level
        x = (width - zoom_width) // 2
        y = (height - zoom_height) // 2

        cropped_image = original_image.crop((x, y, x + zoom_width, y + zoom_height))

        with BytesIO() as image_bytes:
            cropped_image.save(image_bytes, format='PNG')
            image_bytes.seek(0)
            return discord.File(image_bytes, filename='partial_image.png')

    @commands.command(name='gtc')
    async def start_game(self, ctx):
        if self.current_game:
            await ctx.send("A game is already in progress!")
            return

        character = random.choice(list(self.characters.keys()))
        character_data = self.characters[character]

        self.current_game = {
            "character": character,
            "possible_names": character_data["possible_names"],
            "image_url": character_data["url"],
            "zoom_level": 7
        }

        await ctx.send("Who is this?")
        file = await self.crop_image(self.current_game["image_url"], self.current_game["zoom_level"])
        await ctx.send(file=file)

    @commands.command(name='zoomout')
    async def zoom_out(self, ctx):
        if not self.current_game:
            await ctx.send("There is no game in progress!")
            return

        self.current_game["zoom_level"] = max(1, self.current_game["zoom_level"] - 1)

        file = await self.crop_image(self.current_game["image_url"], self.current_game["zoom_level"])
        await ctx.send(file=file)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not self.current_game or message.author.bot:
            return

        guess = message.content.lower()
        if guess in self.current_game["possible_names"]:
            await message.channel.send(f"Correct! The character is {self.current_game['character']}.")
            await message.channel.send(self.current_game["image_url"])
            self.current_game = None

async def setup(bot):
    await bot.add_cog(GuessThatCharacter(bot))
