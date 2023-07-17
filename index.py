import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


bot.run('ODUwMTI5NDE3OTEyNzEzMjE3.GnC9f3.a1HUAhyUSufA8sHc_ymTSDqecBI7y4q6Fi0OFY')