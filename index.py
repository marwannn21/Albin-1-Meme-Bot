import discord
from discord.ext import commands

import requests

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert to milliseconds and round to an integer
    await ctx.send(f'Pong! Bot Latency: {latency}ms')


def fetch_random_meme():
    # Use an API to fetch a random meme
    response = requests.get('https://meme-api.com/gimme')
    if response.status_code == 200:
        meme_data = response.json()
        meme_url = meme_data['url']
        return meme_url
    return None

@bot.command()
async def meme(ctx):
    meme_url = fetch_random_meme()
    if meme_url:
        await ctx.send(meme_url)
    else:
        await ctx.send("Failed to fetch a meme. Try again later.")

bot.run('ODUwMTI5NDE3OTEyNzEzMjE3.GnC9f3.a1HUAhyUSufA8sHc_ymTSDqecBI7y4q6Fi0OFY')