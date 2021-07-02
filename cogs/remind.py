import discord
from discord.ext import commands
import asyncio
import random
import os
import json


class Remind(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.data = self.load_json()

    def load_json(self):
        with open('./data.json') as file:
            data = json.load(file)
        return data

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor

    @commands.command()
    async def ppset(self, ctx, time: int):
        if str(ctx.author.id) in self.bot.data.keys():
            self.bot.data[str(ctx.author.id)] = time

        else:
            try:
                current = self.bot.data[str(ctx.author.id)]
                current = time
                self.bot.data[str(ctx.author.id)] = current
            except KeyError:
                self.bot.data[str(ctx.author.id)] = time

        with open('./data.json', "w") as file:
            json.dump(self.bot.data, file, indent = 4)

        await ctx.send(f"Your time has been changed to {time} seconds")

    @ppset.error
    async def ppset_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Time Error",
             description = ("Use seconds to set your time."),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Example z!ppset 1200 for 20m dont have to use "s"') 
            await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        #PP Bot (pp!r)
        if message.content.lower() == 'pp!r':
            if str(message.author.id) in self.bot.data.keys():
                await asyncio.sleep(self.bot.data[str(message.author.id)])
            else:
                await asyncio.sleep(120)
            await message.channel.send(f'{message.author.mention} **Raid Lista/Ready**')

        if message.content.lower() == 'pp!m':
            await asyncio.sleep(300)
            await message.channel.send(f'{message.author.mention} **Mine Lista/Ready**')

        if message.content.lower() == 'pp!petb':
            await asyncio.sleep(900)
            await message.channel.send(f'{message.author.mention} **Petb Lista/Ready**')

        if message.content.lower() == 'pp!rl':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Roulette Lista/Ready**')

        if message.content.lower() == 'pp!pray 50000000':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Pray Lista/Ready**')

        if message.content.lower() == 'pp!pray 500000000':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Pray Lista/Ready**')

        if message.content.lower() == 'pp!f':
            await asyncio.sleep(60)
            await message.channel.send(f'{message.author.mention} **Fish Lista/Ready**')

        if message.content.lower() == 'pp!h':
            await asyncio.sleep(60)
            await message.channel.send(f'{message.author.mention} **Hunt Lista/Ready**')

        if message.content.lower() == 'pp!b':
            await asyncio.sleep(30)
            await message.channel.send(f'{message.author.mention} **Beg Lista/Ready**')

        #PP Bot (pp)
        if message.content.lower() == 'ppr':
            if str(message.author.id) in self.bot.data.keys():
                await asyncio.sleep(self.bot.data[str(message.author.id)])
            else:
                await asyncio.sleep(120)
            await message.channel.send(f'{message.author.mention} **Raid Lista/Ready**')

        if message.content.lower() == 'ppm':
            await asyncio.sleep(300)
            await message.channel.send(f'{message.author.mention} **Mine Lista/Ready**')

        if message.content.lower() == 'pppetb':
            await asyncio.sleep(900)
            await message.channel.send(f'{message.author.mention} **Petb Lista/Ready**')

        if message.content.lower() == 'pprl':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Roulette Lista/Ready**')

        if message.content.lower() == 'pppray 50000000':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Pray Lista/Ready**')

        if message.content.lower() == 'pppray 500000000':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **Pray Lista/Ready**')

        if message.content.lower() == 'ppf':
            await asyncio.sleep(60)
            await message.channel.send(f'{message.author.mention} **Fish Lista/Ready**')

        if message.content.lower() == 'pph':
            await asyncio.sleep(60)
            await message.channel.send(f'{message.author.mention} **Hunt Lista/Ready**')
       
        if message.content.lower() == 'ppb':
            await asyncio.sleep(30)
            await message.channel.send(f'{message.author.mention} **Beg Lista/Ready**')

        #Mantaro
        if message.content.lower() == '->mine':
            await asyncio.sleep(320)
            await message.channel.send(f'{message.author.mention} **->mine Lista/Ready**')
        
        if message.content.lower() == '->loot':
            await asyncio.sleep(320)
            await message.channel.send(f'{message.author.mention} **->loot Lista/Ready**')

        if message.content.lower() == '->fish':
            await asyncio.sleep(265)
            await message.channel.send(f'{message.author.mention} **->fish Lista/Ready**')

        if message.content.lower() == '->chop':
            await asyncio.sleep(265)
            await message.channel.send(f'{message.author.mention} **->chop Lista/Ready**')

        #izzi

        if message.content.lower() == 'iz hourly':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **iz hourly Lista/Ready**')

        if message.content.lower() == 'iz hr':
            await asyncio.sleep(3600)
            await message.channel.send(f'{message.author.mention} **iz hr Lista/Ready**')

        if message.content.lower() == 'iz lottery':
            await asyncio.sleep(900)
            await message.channel.send(f'{message.author.mention} **iz lottery Lista/Ready**')

        if message.content.lower() == 'iz spbt':
            await asyncio.sleep(2700)
            await message.channel.send(f'{message.author.mention} **iz spbt Lista/Ready**')

        if message.content.lower() == 'iz rd bt all':
            await asyncio.sleep(1200)
            await message.channel.send(f'{message.author.mention} **iz rd bt all Lista/Ready**')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, discord.Forbidden):
            return
        else:
            raise error

def setup(bot):
    bot.add_cog(Remind(bot))
