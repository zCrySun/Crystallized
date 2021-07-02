import discord
from discord.ext import commands
import re
import random
from datetime import datetime as d

class Todo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor

    @commands.command()
    async def help(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(
            colour = self.RandomColor(),
            timestamp = d.now()
        )
        embed.set_author( name=f'{ctx.author.name} how can i help?', icon_url=member.avatar_url)
        embed.add_field(name='Fun Comands', value='8ball  Kiss  Pat  Hug  Slap  Cry  Pout  Poke  Lick  Confused  Bored  Blush  Choose', inline=False)
        embed.add_field(name='Extras', value='Servericon  Purge  Invite  Ping Avatar  Stats  Info  Timer  Addvote', inline=False)
        embed.add_field(name='Moderation', value="Kick  Ban", inline=False)
        embed.add_field(name='Remind', value="aniset  ppset", inline=False)
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        embed.set_footer(text = 'Use z!help_(category) for more information')
     
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions( manage_messages = True)
    async def purge(self, ctx, limit: int):
        def not_pinned(msg):
            return not msg.pinned
        purged = await ctx.channel.purge(limit=limit + 1, check=not_pinned)
        embed = discord.Embed(
            title = "Purgeeeee",
            description = (f"Successfully removed {len(purged)}!"),
            color = self.RandomColor(),
            timestamp = d.now()
        )
        await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if re.fullmatch("<@(!?)700176493015334914>", message.content):
            await message.channel.send(f'Hi! {message.author.mention}, my prefix is "z!"')
        else:
            message.content == self.bot.user.mention

    #error 
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Purge Error",
             description = ("Insufficient permits."),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Todo(bot))
