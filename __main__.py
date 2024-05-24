
import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    

    questions = ["do", "does", "am", "will", "is", "are", "can", "have", "should", "would", "could", "did", "shall"]
    answers = ["Yes", "No", "For sure", "Perchance", "Perhaps", "Perhaps not", "Definitely not", "Nope", "Maybe", "Without a doubt", "Absolutely!", "Not a chance", "You bet!", "Never in a million years", "It's possible", "In your dreams", "Affirmative", "Negative", "Signs point to yes", "Don't count on it", "Ask again later", "My sources say no", "Outlook not so good", "Yes, but keep it quiet", "No, but nice try", "I can't say for sure", "Possibly", "Unlikely", "Very doubtful", "Absolutely not", "Yes, and it's amazing!", "No, but maybe later", "For sure, but don't tell anyone", "No way, Jose", "I'd say yes", "I'd say no", "Chances are slim", "It's a secret", "Most likely", "You wish", "As if", "Definitely yes", "Definitely maybe"]

    for question in questions:
        if message.content.startswith(question):
            answer = random.choice(answers)
            await message.channel.send(answer)

    await bot.process_commands(message)

@bot.command(name="hi")
async def on_help(ctx):
    await ctx.send("What would you like help with?")

bot.load_extension("cogs.test")

bot.run(TOKEN)