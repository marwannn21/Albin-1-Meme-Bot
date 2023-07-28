import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Set the bot's status to "mention for help"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mention for help"))


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        if message.mention_everyone is False:
            # Respond with the help information
            help_embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())
            help_embed.add_field(name="!ping", value="Get the bot's latency.")
            help_embed.add_field(name="!meme", value="Get a random meme.")
            help_embed.add_field(name="!gif [query]", value="Search and get a GIF based on the query.")
            await message.channel.send(embed=help_embed)    
    
    # Process other commands and messages as usual
    await bot.process_commands(message)

# Import the commands module (file) to access the ping and meme commands
import commands
commands.setup(bot)

bot.run('ODUwMTI5NDE3OTEyNzEzMjE3.GnC9f3.a1HUAhyUSufA8sHc_ymTSDqecBI7y4q6Fi0OFY')