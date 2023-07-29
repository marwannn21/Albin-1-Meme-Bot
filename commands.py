from discord.ext import commands
import requests
import discord
import asyncio

def log_command(ctx):
    print(f"Command '{ctx.command.name}' invoked by {ctx.author} in {ctx.guild} channel.")

@commands.command(help="Sends a message with the bot's ping") 
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

@commands.command(help="Returns a Meme")
async def memes(ctx):
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

@commands.command(help="Returns a Gif with the search query used")
async def gif(ctx, *, query=None):
    if not query:
        await ctx.send("Please include a search term after the command to find a GIF. For example: `!gif cats`")
        return

    gif_url = fetch_random_gif('GIFY_API_KEY', query)
    if gif_url:
        await ctx.send(gif_url)
    else:
        await ctx.send(f"No GIFs found for the search term '{query}'. Try another search term!")

#Meme Battle Command---

@commands.command(help="Starts a meme battle with server members")
async def memebattle(ctx):
    await ctx.send("Meme battle is about to begin! Type `!meme` followed by your meme caption to join the battle.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Get the user's meme caption
        message = await ctx.bot.wait_for("message", check=check, timeout=60.0)
        user_caption = message.content

        # Get a random meme
        meme_url = fetch_random_meme()
        if not meme_url:
            await ctx.send("Failed to fetch a meme. Try again later.")
            return

        # Display the random meme with the user's caption
        embed = discord.Embed(title="Meme Battle", description=f"{user_caption}\n\n[Original Meme]({meme_url})")
        embed.set_image(url=meme_url)
        await ctx.send(embed=embed)
    except asyncio.TimeoutError:
        await ctx.send("Meme battle timed out. Try again later.")



#Commands to main file
def setup(bot):
    bot.add_command(ping)  # Ping Command
    bot.add_command(memes)  # Meme Command
    bot.add_command(gif) #GIF Command (Tenor)
    bot.add_command(memebattle) #Meme Battle Command