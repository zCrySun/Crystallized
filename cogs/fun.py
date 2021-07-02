from discord.ext import commands
import discord
import os
import datetime

import random


class Fun(commands.Cog):

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor
        
    def __init__(self, bot):
        self.bot = bot

        self.hug_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/759929693863804928/hug.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759929714168168488/hug2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759929717993635840/hug3.gif"
        ]
        self.pat_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/759931909253234718/pat.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759931947324669973/pat2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759931931340570634/pat3.gif"
        ]
        self.kiss_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/759928445731078144/kiss.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759928476589097030/kiss2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759928486424084530/kiss3.gif"

        ]
        self.slap_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/759929812919124048/slap.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759929828936908840/slap2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759929832175173632/slap3.gif"
        ]
        self.cry_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/759933477193121802/cry.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759933437208821820/cry2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/759933443957063680/cry3.gif"
        ]
        self.blush_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/765367006140039188/blush.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765367003673395230/blush2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765366988432211979/blush3.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765366982102351872/blush4.gif"
        ]
        self.bored_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/765368135230160906/bored.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765368142956331018/bored2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765368130167898122/bored3.gif"
        ]
        self.confused_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/765368578617901096/confused.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765368590329184266/confused2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765368587660689488/confused3.gif"
        ]
        self.lick_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/765369655941529650/lick.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765369665794867221/lick2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765369629592911912/lick3.gif"
        ]
        self.poke_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/765372697639125062/poke.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765372696812191764/poke2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765372688683368458/poke3.gif"
        ]
        self.pout_gifs = [
            "https://cdn.discordapp.com/attachments/700926180559421440/765373064355119124/pout.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765373067832459314/pout2.gif",
            "https://cdn.discordapp.com/attachments/700926180559421440/765373074043437086/pout3.gif"
        ]

    
    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        embed = discord.Embed(title = f"{ctx.author.name} gave a hug to {member.name}", color =self.RandomColor())
        embed.set_image(url = random.choice(self.hug_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        embed = discord.Embed(title = f"{ctx.author.name} gave a kiss to {member.name}", color = self.RandomColor())
        embed.set_image(url = random.choice(self.kiss_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        embed = discord.Embed(title = f"{ctx.author.name} patted {member.name}", color = self.RandomColor())
        embed.set_image(url = random.choice(self.pat_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)
    
    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        embed = discord.Embed(title = f"{ctx.author.name} slapped themselves {member.name}", color = self.RandomColor())
        embed.set_image(url = random.choice(self.slap_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)
    
    @commands.command()
    async def cry(self, ctx):
        embed = discord.Embed(title = f"{ctx.author.name} out of nowhere is crying...", color = self.RandomColor())
        embed.set_image(url = random.choice(self.cry_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def blush(self, ctx):
        embed = discord.Embed(title = f"{ctx.author.name} is blushing too much >-<", color = self.RandomColor())
        embed.set_image(url = random.choice(self.blush_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def bored(self, ctx):
        embed = discord.Embed(title = f"{ctx.author.name} is getting bored.", color = self.RandomColor())
        embed.set_image(url = random.choice(self.bored_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def confused(self, ctx):
        embed = discord.Embed(title = f"{ctx.author.name} has been confused :(", color = self.RandomColor())
        embed.set_image(url = random.choice(self.confused_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def lick(self, ctx, member: discord.Member):
        embed = discord.Embed(title = f"{ctx.author.name} is gently licking at {member.name}", color = self.RandomColor())
        embed.set_image(url = random.choice(self.lick_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def poke(self, ctx, member: discord.Member):
        embed = discord.Embed(title = f"{ctx.author.name} pokes {member.name}", color = self.RandomColor())
        embed.set_image(url = random.choice(self.poke_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def pout(self, ctx):
        embed = discord.Embed(title = f"{ctx.author.name} doesn't like that!", color = self.RandomColor())
        embed.set_image(url = random.choice(self.pout_gifs))
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008')
        await ctx.send(embed = embed)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
             title = "📡Pong!",
             description = round(self.bot.latency * 1000 ),
             color = self.RandomColor()
        )
        await ctx.send(embed = embed)
        
    @commands.command(name='8ball')
    async def _ball(self, ctx, *, question):
        responses = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.'
        ]
        answer = random.choice(responses)
        embed = discord.Embed(color = self.RandomColor())
        embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
        embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
        embed.set_author(name="8 Ball Machine", icon_url="https://cdn.discordapp.com/attachments/700926180559421440/770037931905253376/ball.png")
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008') 
        await ctx.send(embed=embed)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        embed = discord.Embed(
             title = "I pick!  <:zerotwosurprise:768289433543639112>",
             description =  random.choice(choices),
             color = self.RandomColor()
        )
        embed.set_footer(text = 'Questions or suggestions Cry Sun.#0008') 
        await ctx.send(embed = embed)
        
    

def setup(bot):
    bot.add_cog(Fun(bot))
