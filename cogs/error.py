import discord
from discord.ext import commands 
import os
import config
from datetime import datetime as d
import random
import asyncio


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Error",
             description = (f"{error}"),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008') 
            await ctx.send(embed = embed)

 

def setup(bot):
    bot.add_cog(Error(bot))