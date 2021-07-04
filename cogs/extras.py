from datetime import datetime as d
from datetime import datetime, timedelta
import time
import os
import platform
import re
import asyncio
import discord
from discord.ext import commands
import random

class TimeParser:
    def __init__(self, argument):
        compiled = re.compile(r"(?:(?P<days>[0-9]{1,5})d)?(?:(?P<hour>[0-9]{1,5})h)?(?:(?P<minutes>[0-9]{1,5})m)?(?:(?P<seconds>[0-9]{1,5})s)?$")
        self.original = argument
        try:
            self.seconds = int(argument)
        except ValueError as e:
            match = compiled.match(argument)
            if match is None or not match.group(0):
                raise commands.BadArgument('Incorrect time specified, they are valid `4h`, `3m` or `2s` (z!timer 4h remind)') from e

            self.seconds = 0
            days = match.group('days')
            if days is not None:
                self.seconds += int(days) * 86400
            hour = match.group('hour')
            if hour is not None:
                self.seconds += int(hour) * 3600
            minutes = match.group('minutes')
            if minutes is not None:
                self.seconds += int(minutes) * 60
            seconds = match.group('seconds')
            if seconds is not None:
                self.seconds += int(seconds)

        if self.seconds <= 0:
            raise commands.BadArgument('Not enough time has been specified, they are valid z.B. `4h`, `3m` or `2s`')

        if self.seconds > 864000: # 10 days
            raise commands.BadArgument('7 days is a long time, dont you think so too?')
    
    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @staticmethod
    def human_timedelta(dt):
        now = datetime.utcnow()
        delta = now - dt
        hour, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, second = divmod(remainder, 60)
        day, hour = divmod(hour, 24)


        if day:
            if hour:
                return '%s and %s' % (Plural(Tag=day), Plural(hour=hour))
            return Plural(day=day)

        if hour:
            if minutes:
                return '%s and %s' % (Plural(hour=hour), Plural(Minute=minutes))
            return Plural(hour=hour)

        if minutes:
            if second:
                return '%s and %s' % (Plural(Minute=minutes), Plural(seconds=second))
            return Plural(Minute=minutes)
        return Plural(second=second)

class Plural:
    def __init__(self, **attr):
        iterator = attr.items()
        self.name, self.value = next(iter(iterator))

    def __str__(self):
        v = self.value
        if v > 1:
            return '%s %ss' % (v, self.name)
        return '%s %s' % (v, self.name)

class Extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Add me!",
            description = "You can invite me by clicking [here!](https://discord.com/api/oauth2/authorize?client_id=700176493015334914&permissions=268708983&scope=bot)",
            color = self.RandomColor()
        )
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/756359270706184222/759891425890140171/NeroChan.png")
        embed.add_field(name = "Server support!", value = "Do you have any questions about the bot or suggestions enter [here!](https://discord.gg/Yq798Dav6b)")
        embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
        """
        embed.add_image(url = "https://cdn.discordapp.com/attachments/756359270706184222/759193581034143775/MeguExploded.png")

        [text](link)
        """
        await ctx.send(embed = embed)

    @commands.command(aliases = ["av"])
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(
             title = f"Requested by {ctx.author.name}",
             description = f"""**Name:** {member}              
             **ID:** {member.id} """,
             color = self.RandomColor()
             
        )
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
        await ctx.send(embed = embed)
        
    @commands.command()
    async def stats(self,ctx):
        embed=discord.Embed(title="Bot Stats", url="", description="Hi, I am a bot guided to the command remind and among some other things", color = self.RandomColor(), timestamp = d.now())
        embed.add_field(name="👑 Owner:", value="Cry Sun.#0008", inline=True)
        embed.add_field(name="👑 Co-Owner:", value=".sylex#2803", inline=True)
        embed.add_field(name="📉 Servers:", value=f"{len(self.bot.guilds)}", inline=True)
        embed.add_field(name="💿 Prefix:", value="z!", inline=True)
        embed.add_field(name="📡 Ping:", value= round(self.bot.latency * 1000), inline=True)
        embed.add_field(name="🎗️ Support:", value="Click [here!](https://discord.gg/dY4eVeN) to get on help server", inline=True)
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        embed.set_footer(text="Bot in develpment - if you see any bugs dm me")
        await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(color = self.RandomColor(), timestamp = d.now())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
        await ctx.send(embed=embed)

    @commands.command()
    async def server(self,ctx):
        embed=discord.Embed(title="Sopport Server", description="here you can report bugs or send suggestions about reminds or things to improve the bot, [Join server!](https://discord.gg/Yq798Dav6b)", color = self.RandomColor(), timestamp = d.now())
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        embed=discord.Embed(title="Vote", description='''Thanks for supporting the bot !!
<a:Rainbow_Corgi:856646505389096970> [Click for vote](https://top.gg/bot/700176493015334914/vote)''', color = self.RandomColor())
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            roles = ", ".join([role.mention if role.name != "@everyone" else "@everyone" for role in member.roles])
            created_at = member.created_at.strftime('%B %d, %Y')
            joined_at = member.joined_at.strftime('%B %d, %Y')
            e = discord.Embed(title=f"Member info for {member}:", color = self.RandomColor(), timestamp = d.now())
            e.set_thumbnail(url=member.avatar_url)
            e.add_field(name="Join Date:", value=joined_at)
            e.add_field(name="Account creation date:", value=created_at, inline=False)
            e.add_field(name="ID:", value=f"{member.id}")
            e.add_field(name="Nickname:", value=f"{member.nick}")
            e.add_field(name="Roles:", value=roles, inline=False)
            e.set_footer(text = 'Questions or suggestions enter the support server and say so')
            await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions( manage_messages = True)
    @commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
    async def addvote(self, ctx, votecount = 'bool'):
        if votecount.lower() == 'bool':
            emote_list = ['✅', '❌']
        elif votecount in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            #emotes = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
            emotes = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']
            emote_list = []
            for i in range (0, int(votecount)):
                emote_list.append(emotes[i])
        else:
            ctx.say(':x: Enter a number between 2 and 10')

        message = await ctx.channel.history(limit=1, before=ctx.message).flatten()
        try:
            await ctx.message.delete()
        except:
            pass

        for emote in emote_list:
            await message[0].add_reaction(emote)

    @commands.command(aliases=['reminder'])
    @commands.cooldown(1, 15, commands.cooldowns.BucketType.user)
    async def timer(self, ctx, time : TimeParser, *, message=''):
        '''
        -----------
        timer 13m Pizza
        timer 2h Stream startet
        '''
        reminder = None
        completed = None
        message = message.replace('@everyone', '@\u200beveryone').replace('@here', '@\u200bhere')

        if not message:
            reminder = ':timer: Ok {0.mention}, Im going to put a timer {1}.'
            completed = ':alarm_clock: Ding Ding Ding {0.mention}! Your timer has expired.'
        else:
            reminder = ':timer: Ok {0.mention}, I am setting a timer for `{2}` in {1}.'
            completed = ':alarm_clock: Ding Ding Ding {0.mention}! Your timer for `{1}` has expired.'

        human_time = datetime.utcnow() - timedelta(seconds=time.seconds)
        human_time = TimeParser.human_timedelta(human_time)
        await ctx.send(reminder.format(ctx.author, human_time, message))
        await asyncio.sleep(time.seconds)
        await ctx.send(completed.format(ctx.author, message, human_time))
    
    #error 
    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound, commands.CommandOnCooldown):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Info Error",
             description = (f"{error}"),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Avatar Error",
             description = (f"{error}"),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)

    #@timer.error
    #async def timer_error(self, ctx, error):
        #if isinstance(error, commands.CommandOnCooldown):
            #embed = discord.Embed(
             #title = "<a:error:777382842077675530> Timer Error",
             #description = (f"{error}"),
             #color = self.RandomColor()
            #)
            #embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            #await ctx.send(embed = embed)

    @timer.error
    async def timer_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Command Error",
             description = (f"{error}"),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)
            
    @addvote.error
    async def addvote_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Addvote Error",
             description = (f"{error}"),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Extra(bot))
