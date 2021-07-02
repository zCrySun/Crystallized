import discord
from discord.ext import commands
import asyncio
import os
import json
import random

class Aniremind(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.aniraids = self.load_json()

    def load_json(self):
        with open('./aniraids.json') as file:
            aniraids = json.load(file)
        return aniraids

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor

    @commands.command()
    async def aniset(self, ctx, time : int):
        if str(ctx.author.id) in self.bot.aniraids.keys():
            self.bot.aniraids[str(ctx.author.id)] = time

        else:
            try:
                current = self.bot.aniraids[str(ctx.author.id)]
                current = time
                self.bot.aniraids[str(ctx.author.id)] = current
            except KeyError:
                self.bot.aniraids[str(ctx.author.id)] = time

        with open('./aniraids.json', "w") as file:
            json.dump(self.bot.aniraids, file, indent = 4)

        await ctx.send(f"Your time has been changed to {time} seconds")

    @aniset.error
    async def aniset_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Time Error",
             description = ("Use seconds to set your time."),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Example z!aniset 1200 for 20m dont have to use "s"') 
            await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

    #AniGame
        if message.content.lower() == '.hourly':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Hourly listo/Ready**')

        if message.content.lower() == '.lottery':
            await asyncio.sleep(600)
            await message.channel.send(f'{message.author.mention} **Lottery lista/Ready**')

        if message.content.lower() == '.rd bt all':
            if str(message.author.id) in self.bot.aniraids.keys():
                await asyncio.sleep(self.bot.aniraids[str(message.author.id)])
            else:
                await asyncio.sleep(1200)
            await message.channel.send(f'{message.author.mention} **Raid Battle Ready**')

        if message.content.lower() == '.rd spawn i':
            await asyncio.sleep(14404)
            await message.channel.send(f'{message.author.mention} **Spawn raid lista/Ready**')

        if message.content.lower() == '.rd spawn':
            await asyncio.sleep(14404)
            await message.channel.send(f'{message.author.mention} **Spawn raid lista/Ready**')

        if message.content.lower() == '.rd spawn e':
            await asyncio.sleep(14404)
            await message.channel.send(f'{message.author.mention} **Spawn raid lista/Ready**')

        if message.content.lower() == '.rd spawn m':
            await asyncio.sleep(14404)
            await message.channel.send(f'{message.author.mention} **Spawn raid lista/Ready**')

        if message.content.lower() == '.rd spawn h':
            await asyncio.sleep(14404)
            await message.channel.send(f'{message.author.mention} **Spawn raid lista/Ready**')


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, discord.Forbidden):
            return
        else:
            raise error

def setup(bot):
    bot.add_cog(Aniremind(bot))
