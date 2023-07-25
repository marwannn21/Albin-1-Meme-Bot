import discord
from discord.ext import commands

import random
import asyncio
import requests

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

def fetch_question():
    response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
    if response.status_code == 200:
        data = response.json()
        if 'results' in data:
            result = data['results'][0]
            question = result['question']
            correct_answer = result['correct_answer']
            incorrect_answers = result['incorrect_answers']
            answers = [correct_answer] + incorrect_answers
            random.shuffle(answers)
            formatted_question = f"{question}\n\n"
            for idx, ans in enumerate(answers, start=1):
                formatted_question += f"{idx}. {ans}\n"
            return formatted_question, correct_answer
    return 'Failed to fetch question', None

@bot.command()
async def trivia(ctx):
    question, correct_answer = fetch_question()
    await ctx.send(f"Trivia Question:\n{question}")

    # You can store the correct answer in the context using ctx for later use
    ctx.correct_answer = correct_answer


@bot.event
async def on_message(message):
    # Check if the message author is the bot itself to avoid infinite loops
    if message.author == bot.user:
        return

    # Check if the message was sent in response to a trivia question
    if hasattr(message, 'correct_answer') and message.content.lower() == message.correct_answer.lower():
        await message.channel.send(f"{message.author.mention} Correct answer!")
    else:
        await message.channel.send(f"{message.author.mention} Wrong answer! Try again.")
    
    await bot.process_commands(message)



bot.run('ODUwMTI5NDE3OTEyNzEzMjE3.GnC9f3.a1HUAhyUSufA8sHc_ymTSDqecBI7y4q6Fi0OFY')