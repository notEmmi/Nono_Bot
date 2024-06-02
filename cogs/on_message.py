import random
from discord.ext import commands

"""
    on_message.py
    Bot responses to messages in chat
    
    Detail:
    Bot responds to simple yes or no questions, along with greetings and goodbyes.
    It also detects certain curse words and sends a warning when they are detected.

    (The bots a little silly so he can be random at times :))

    **Done working on FOR NOW**

    For future works:
        - Add more curse words (such as slurs)
        - Fix warning responses AFTER ADDING MORE GAMES AND COMMANDS
        - Fix when so bot does not respond to "him" (etc), thinking its "hi"
        - if possible, update runtime (for learning purpose)
            - same thing for curse words (classy == ass according to bot)

"""

class On_Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_message(self, message):

        data = {
            "questions": {
                "triggers": {"do ", "does ", "am ", "will ", "is ", "are ", "can ", "have ", "should ", "would ", "could ", "did ", "shall "},
                "responses": ["Yes", "No", "For sure", "Perchance", "Perhaps", "Perhaps not", "Definitely not", "Nope", "Maybe", "Without a doubt", "Absolutely!", "Not a chance", "You bet!", "Never in a million years", "It's possible", "In your dreams", "Affirmative", "Negative", "Signs point to yes", "Don't count on it", "Ask again later", "My sources say no", "Outlook not so good", "Yes, but keep it quiet", "No, but nice try", "I can't say for sure", "Possibly", "Unlikely", "Very doubtful", "Absolutely not", "No, but maybe later", "For sure, but don't tell anyone", "No way, Jose", "I'd say yes", "I'd say no", "Chances are slim", "It's a secret", "Most likely", "You wish", "As if", "Definitely yes"]
            },
            "greetings": {
                "triggers": {'good morning', 'good afternoon', 'hello', 'hi', 'hey', 'howdy', 'hiya', 'greetings', 'salutations'},
                "responses": ["Hello", "Hi", "Hey", "Howdy", "Hiya", "Greetings", "Salutations"]
            },
            "goodbyes": {
                "triggers": {'goodbye', 'bye', 'farewell', 'see you later', 'catch you later', 'take care', 'have a great day', 'until next time', 'adios', 'so long', 'good night'},
                "responses": ["Goodbye", "Bye", "Farewell", "See you later", "Catch you later", "Take care", "Until next time", "Adios", "So long"]
            },
            "curse_words": {
                "triggers": {"ass", "bitch", "bullshit", "cock", "cunt", "crap", "damn", "dammit", "dick", "dumb", "fuck", "hell", "shit", "piss", "pussy", "slut", "whore", "twat", "wanker", "bugger"},
                "responses": [
                    "🚫 Hey, watch your language! Let’s keep things friendly and fun here. How about we play a game instead? Type `!games` to see what we can do!",
                    "🚫 Whoa there, language! Let's keep it classy, shall we? How about a round of trivia to lighten the mood? Type `!trivia` to start!",
                    "🚫 Oops! That’s a no-no word. Let's use our indoor voices. Need a distraction? How about a game of Truth or Dare? Type `!truthordare` to challenge someone!",
                    "🚫 Uh-oh, someone's getting a bit too spicy! Let’s tone it down. Fancy a game of Rock, Paper, Scissors instead? Type `!rps` to play!",
                    "🚫 Yikes! Let’s keep the chat squeaky clean. How about guessing a number instead? Type `!numberguess` to give it a try!",
                    "🚫 Naughty words alert! Remember, politeness is key. Need something to do? How about trying to solve a Hangman puzzle? Type `!hangman` to start!"
                ]
            }
        }

        message_content = message.content.lower()

        if message.author == self.bot.user:
            return

        # Check for greetings
        if any(message_content.startswith(trigger) for trigger in data["greetings"]["triggers"]):
            print(f"on_message trigger: {message_content}")
            response = random.choice(data["greetings"]["responses"])
            await message.channel.send(f"{response} {message.author.mention}!")
            return

        # Check for goodbyes
        elif any(message_content.startswith(trigger) for trigger in data["goodbyes"]["triggers"]):
            print(f"on_message trigger: {message_content}")
            response = random.choice(data["goodbyes"]["responses"])
            await message.channel.send(f"{response} {message.author.mention}!")
            return

        # Check for questions
        elif any(message_content.startswith(trigger) for trigger in data["questions"]["triggers"]):
            print(f"on_message trigger: {message_content}")
            response = random.choice(data["questions"]["responses"])
            await message.channel.send(response)
            return

        # Check for curse words
        elif any(trigger in message_content for trigger in data["curse_words"]["triggers"]):
            print(f"on_message trigger: {message_content}")
            response = random.choice(data["curse_words"]["responses"])
            await message.channel.send(f"{message.author.mention} {response}")
            return

async def setup(bot):
    await bot.add_cog(On_Message(bot))
