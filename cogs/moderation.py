import discord
from discord.ext import commands
import asyncio
import random
import os
from datetime import datetime as d

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    def RandomColor(self): 
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor

    @commands.command() 
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(
             title = f"<a:Accepted:777385228427722774> Kick {member}",
             description = (f'Reason: {reason}'),
             color = self.RandomColor(),
             timestamp = d.now()
        )
        embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
        await member.kick(reason=reason)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(
             title = f"<a:Accepted:777385228427722774> Banned {member}",
             description = (f'Reason: {reason}'),
             color = self.RandomColor(),
             timestamp = d.now()
        )
        embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
        await member.ban(reason=reason)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
    
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
        
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                 await ctx.guild.unban(user)
                 embed = discord.Embed(
                 title = f"<a:Accepted:777385228427722774> Unbaned",
                 description = (f'Successfully'),
                 color = self.RandomColor(),
                 timestamp = d.now()
                 )
                 embed.set_footer(text = 'Questions or suggestions enter the support server and say so')
                 await ctx.channel.send(embed = embed)
                 return
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Ban Error",
             description = ("Invalid user."),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)  

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
             title = "<a:error:777382842077675530> Kick Error",
             description = ("Invalid user."),
             color = self.RandomColor()
            )
            embed.set_footer(text = 'Questions or suggestions enter the support server and say so') 
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Moderation(bot))