
import random
from discord.ext import commands
from discord.ext.commands import Context


from discord.ext import commands

class test:
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    

        questions = ["do", "does", "am", "will", "is", "are", "can", "have", "should", "would", "could", "did", "shall"]
        answers = ["Yes", "No", "For sure", "Perchance", "Perhaps", "Perhaps not", "Definitely not", "Nope", "Maybe", "Without a doubt", "Absolutely!", "Not a chance", "You bet!", "Never in a million years", "It's possible", "In your dreams", "Affirmative", "Negative", "Signs point to yes", "Don't count on it", "Ask again later", "My sources say no", "Outlook not so good", "Yes, but keep it quiet", "No, but nice try", "I can't say for sure", "Possibly", "Unlikely", "Very doubtful", "Absolutely not", "Yes, and it's amazing!", "No, but maybe later", "For sure, but don't tell anyone", "No way, Jose", "I'd say yes", "I'd say no", "Chances are slim", "It's a secret", "Most likely", "You wish", "As if", "Definitely yes", "Definitely maybe"]

        for question in questions:
            if message.content.startswith(question):
                answer = random.choice(answers)
                await message.channel.send(answer)
                break

    @commands.command(name="hello")
    async def on_hello(self, ctx):
        await ctx.send("hello")


def setup(bot):
    bot.add_cog(test(bot))