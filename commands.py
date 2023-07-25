from discord.ext import commands
import requests

def log_command(ctx):
    print(f"Command '{ctx.command.name}' invoked by {ctx.author} in {ctx.guild} channel.")

@commands.command()
async def ping(ctx):
    latency = round(ctx.bot.latency * 1000)  # Convert to milliseconds and round to an integer
    await ctx.send(f'Pong! Bot Latency: {latency}ms')
    log_command(ctx)

def fetch_random_meme():
    # Use an API to fetch a random meme
    response = requests.get('https://meme-api.com/gimme')
    if response.status_code == 200:
        meme_data = response.json()
        meme_url = meme_data['url']
        return meme_url
    return None

@commands.command()
async def meme(ctx):
    meme_url = fetch_random_meme()
    if meme_url:
        await ctx.send(meme_url)
    else:
        await ctx.send("Failed to fetch a meme. Try again later.")
    log_command(ctx)

def setup(bot):
    bot.add_command(ping)  # Add the ping command to the bot
    bot.add_command(meme)  # Add the meme command to the bot
