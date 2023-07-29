import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
        # Print the names of the servers the bot is a member of
    for guild in bot.guilds:
        print(f'Bot is a member of {guild.name} (ID: {guild.id})')
    # Set the bot's status to "mention for help"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mention for help"))
    
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message) 

@bot.event
async def on_message(message):
    print("Message received:", message.content) 
    if bot.user.mentioned_in(message):
        if message.mention_everyone is False:
            # Get the bot's profile photo
            bot_user = await bot.fetch_user(bot.user.id)  # Fetch the User object for the bot
            bot_avatar = bot_user.avatar.url

            # Create the embed for help information
            help_embed = discord.Embed(title="Meme Bot Help", description="List of available commands:", color=discord.Color.blue())
            help_embed.set_thumbnail(url=bot_avatar)  # Set the bot's profile photo as the thumbnail

            # Add individual commands and their descriptions to the embed
            for command in bot.commands:
                help_embed.add_field(name=f"!{command.name}", value=command.help, inline=False)

            # Set the timestamp for the current date and time when the help information was requested
            help_embed.timestamp = message.created_at

            # Add user information and profile photo in the footer
            help_embed.set_footer(text=f"Requested by {message.author.name}", icon_url=message.author.avatar.url)

            # Send the help information as an embed
            await message.channel.send(embed=help_embed)

    # Process other commands and messages as usual
    await bot.process_commands(message)


# Import the commands module (file) to access the ping and meme commands
import commands
commands.setup(bot)

bot.run('YOUR_TOKEN')