from discord.ext import commands
import requests
import discord

def log_command(ctx):
    print(f"Command '{ctx.command.name}' invoked by {ctx.author} in {ctx.guild} channel.")

@commands.command()
async def ping(ctx):
    latency = round(ctx.bot.latency * 1000)  # Convert to milliseconds and round to an integer
    await ctx.send(f'Pong! Bot Latency: {latency}ms')
    log_command(ctx)

#Meme Command

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

#Gif Command  # Use Giphy public API to search for a GIF based on the query

def fetch_random_gif(api_key, query=None):
    if query:
        url = f'https://api.giphy.com/v1/gifs/search?q={query}&api_key={api_key}'
    else:
        url = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        gif_data = response.json()
        if 'data' in gif_data and len(gif_data['data']) > 0:
            gif_url = gif_data['data'][0]['images']['original']['url']
            return gif_url
    return None

@commands.command()
async def gif(ctx, *, query=None):
    if not query:
        await ctx.send("Please include a search term after the command to find a GIF. For example: `!gif cats`")
        return

    gif_url = fetch_random_gif('bMv9uLOxuj53bPxFeuA1XHGxpoR3BiEO', query)
    if gif_url:
        await ctx.send(gif_url)
    else:
        await ctx.send(f"No GIFs found for the search term '{query}'. Try another search term!")


#Commands to main file
def setup(bot):
    bot.add_command(ping)  # Ping Command
    bot.add_command(meme)  # Meme Command
    bot.add_command(gif) #GIF Command (Tenor)