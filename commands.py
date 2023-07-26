from discord.ext import commands
import requests

#API KEY
API_KEY = 'bMv9uLOxuj53bPxFeuA1XHGxpoR3BiEO'

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

#Gif Command

def fetch_random_gif():
    try:
        response = requests.get(f'https://api.giphy.com/v1/gifs/random?api_key={API_KEY}')
        response.raise_for_status()
        gif_data = response.json()
        gif_url = gif_data.get('data', {}).get('image_original_url')
        if gif_url:
            return gif_url
        else:
            print("Error: 'image_original_url' not found in the GIPHY API response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random GIF: {e}")
        return None

@commands.command()
async def gif(ctx):
    log_command(ctx)  # Log the command
    gif_url = fetch_random_gif()
    if gif_url:
        await ctx.send(gif_url)
    else:
        await ctx.send("Failed to fetch a GIF. Try again later.")

#Commands to main file
def setup(bot):
    bot.add_command(ping)  # Ping Command
    bot.add_command(meme)  # Meme Command
    bot.add_command(gif) #GIF Command (Tenor)