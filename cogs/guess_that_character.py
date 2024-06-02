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
        self.scoreboard = None

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
        if self.scoreboard != None and self.current_game != None:
            embed = discord.Embed(
                title = "Current Game Running",
                description= "A game is currently running, type !endgame to end it or !next to continue it.",
                
            )
        else:
            self.current_game = {
                "character": "",
                "possible_names": [],
                "image_url": "",
                "zoom_level": 0,
                "zoomout_count": 0
            }
            rules = """
                **Game Rules:**

                **Guessing the Character:**
                - The bot will send a zoomed-in picture of a character.
                - Your goal is to guess the name of the character using the image.

                **Spelling Counts:**
                - Make sure to spell the character's name correctly.

                **Zooming Out:**
                - Type `!zoomout` for a clearer view.
                - Each use deducts 0.25 points.
                - If your score hits 0, you can still guess, but no points are awarded.

                **To Receive a Character:**
                - Type `!next` when you're ready to move on.
            """ 
            embed = discord.Embed(title = "Rules", description = rules)
            await ctx.send(embed=embed)


    @commands.command()
    async def next(self, ctx):

        character = random.choice(list(self.characters.keys()))
        character_data = self.characters[character]

        self.current_game = {
            "character": character,
            "possible_names": character_data["possible_names"],
            "image_url": character_data["url"],
            "zoom_level": 8,
            "zoomout_count": 0
        }

        file = await self.crop_image(self.current_game["image_url"], self.current_game["zoom_level"])
        embed = discord.Embed(title="Who is this?", color=discord.Color.blue())
        embed.set_image(url="attachment://cropped_image.png")

        await ctx.send(embed=embed, file=file)

    @commands.command(name='zoomout')
    async def zoom_out(self, ctx):
        if self.current_game==None:
            await ctx.send("There is no game in progress!")
            return
        else:
            self.current_game["zoomout_count"] += 1
            self.current_game["zoom_level"] = max(1, self.current_game["zoom_level"] - 1)

            file = await self.crop_image(self.current_game["image_url"], self.current_game["zoom_level"])
            await ctx.send(file=file)

    @commands.Cog.listener()
    async def check(self, message):
        if not self.current_game or message.author.bot:
            return

        guess = message.content.lower()
        if guess in self.current_game["possible_names"]:
            await message.channel.send(f"Correct! The character is {self.current_game['character']}.")
            await message.channel.send(self.current_game["image_url"])
            

    
    async def scoreboard(self, winner):
        


    @commands.command(name="endgame")
    async def endgame(self, ctx):
        if self.current_game or self.scoreboard:
            self.current_game = None
            self.scoreboard = None
            embed = discord.Embed(
                title="Game Ended",
                description="The game has ended.",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = "No Active Game",
                description= "No game is currently running",
                color=discord.Color.red()
            )

        #clear score bored also

async def setup(bot):
    await bot.add_cog(GuessThatCharacter(bot))
