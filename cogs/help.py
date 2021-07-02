import discord
from discord.ext import commands
import re
import random
from datetime import datetime as d

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor

    @commands.command()
    async def help_remind(self, ctx):
        embed=discord.Embed(title="Remind Help", description="The remind is not necessary to activate it when doing the commands that are available the bot will notify you when it is ready", color = self.RandomColor(), timestamp = d.now())
        embed.add_field(name="Mantaro", value="Mine, Loot, Fish and Chop", inline=True)
        embed.add_field(name="izzi", value="hourly, lottery, spbt and rd bt all", inline=False)
        embed.add_field(name="AniGame", value="Lottery, Hourly, rd spawn(e, m, h and i) and rd bt all(this remind has a 20m CD or set CD with command z!aniset (time))", inline=False)
        embed.add_field(name="Not Kohai", value="Raid, Beg, Fish, Hunt, Mine, Pray, Roulette, Petb and Speed boost select your time with command z!ppset (time)", inline=True)
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        embed.set_footer(text="Bot in develpment - If you see any error, go to the support server and report it")
        await ctx.send(embed=embed)

    @commands.command()
    async def help_extras(self, ctx):
        embed=discord.Embed(title="Extras Help", description="", color = self.RandomColor(), timestamp = d.now())
        embed.add_field(name="Servericon", value="server image from where to use the command", inline=True)
        embed.add_field(name="Purge", value="Delete messages that you put in the command, example z!purge 10", inline=True)
        embed.add_field(name="Avatar", value="Gives you the pfp of the user you mention or yours using just the command", inline=True)
        embed.add_field(name="Addvote", value='Use "z!addvote bool" to add ✅ ❌ or use "z!addvote -a number from 1 to 10-" to add 1\u20e3 ... \U0001f51f', inline=False)
        embed.add_field(name="Info", value="Information you mention or yours if you use the command only", inline=True)
        embed.add_field(name="Timer", value="Custom reminder, so far you can remind with seconds, minutes and hours (but if you put the days in hours you can do the remind example z!timer 240h), the maximum of remind is 10 days if you try to put more it will not be possible.", inline=False)
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        embed.set_footer(text="Bot in develpment - If you see any error, go to the support server and report it")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))