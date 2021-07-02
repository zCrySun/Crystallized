import discord
from discord.ext import commands
import asyncio
import os
import config

# await bot.change_presence(activity=discord.Game(name=f"{len(bot.users)} users and {len(bot.guilds)} servers! s!invite"))
intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix = 'z!',
    case_insensitive = True
)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name=f"z!help {len(bot.guilds)} servers!", url="https://www.twitch.tv/crysun__"))
    print('Vamooooos')

@bot.command()
@commands.is_owner()
async def status_reload(ctx):
    await bot.change_presence(activity = discord.Streaming(name=f"z!help {len(bot.guilds)} servers!", url="https://www.twitch.tv/crysun__"))


for ext in os.listdir("./cogs"):
    if ext.endswith('.py'):
        bot.load_extension(f"cogs.{ext[:-3]}")

bot.run(config.token_main)
