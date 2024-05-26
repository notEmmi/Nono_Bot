
import json
import random
from discord.ext import commands

"""
    on_message.py
    Bot responses to messages in chat

"""


print("test.py")
class On_Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # Write Functions here
    @commands.Cog.listener()
    async def on_message(self, message):
        
        with open("yes_no_questions.json") as json_file:
            questions = json.load(json_file)
        
        with open("yes_no_anwers.json") as json_file:
            answers = json.load(json_file)

        if message.author == self.bot.user:
            return
        

        for question in questions:
            if message.content.startswith(question):
                answer = random.choice(answers)
                await message.channel.send(answer)
                break

    @commands.command(name="hello")
    async def on_hello(self, ctx):
        await ctx.send("hello")



async def setup(bot):
    await bot.add_cog(On_Message(bot))