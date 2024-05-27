
import random
from discord.ext import commands

"""
    on_message.py
    Bot responses to messages in chat

"""


class On_Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # Write Functions here
    @commands.Cog.listener()
    async def on_message(self, message):
        print("on_question")

        questions = ["do", "does", "am", "will", "is", "are", "can", "have", "should", "would", "could", "did", "shall"]
        answers = ["Yes", "No", "For sure", "Perchance", "Perhaps", "Perhaps not", "Definitely not", "Nope", "Maybe", "Without a doubt", "Absolutely!", "Not a chance", "You bet!", "Never in a million years", "It's possible", "In your dreams", "Affirmative", "Negative", "Signs point to yes", "Don't count on it", "Ask again later", "My sources say no", "Outlook not so good", "Yes, but keep it quiet", "No, but nice try", "I can't say for sure", "Possibly", "Unlikely", "Very doubtful", "Absolutely not", "No, but maybe later", "For sure, but don't tell anyone", "No way, Jose", "I'd say yes", "I'd say no", "Chances are slim", "It's a secret", "Most likely", "You wish", "As if", "Definitely yes"]

        greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'howdy', 'hiya', 'greetings', 'salutations']
        goodbyes = ['goodbye', 'bye', 'farewell', 'see you later', 'catch you later', 'take care', 'have a great day', 'until next time', 'adios', 'so long']

        message_content = message.content.lower()

        if message.author == self.bot.user:
            return

        # Check for greetings
        for greeting in greetings:
            if message_content.startswith(greeting):
                await message.channel.send(greeting.capitalize() + f" {message.author.mention}!")
                return

        # Check for goodbyes
        for bye in goodbyes:
            if message_content.startswith(bye):
                await message.channel.send(bye.capitalize() + f" {message.author.mention}!")
                return

        # Check for questions
        for question in questions:
            if message_content.startswith(question):
                answer = random.choice(answers)
                await message.channel.send(answer)
                return

        


async def setup(bot):
    await bot.add_cog(On_Message(bot))