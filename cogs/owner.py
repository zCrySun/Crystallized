from discord.ext import commands
import discord
import os


class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, arg: str = None):
        if arg is None:
            for ext in os.listdir("./cogs"):
                if ext.endswith('.py'):
                    self.bot.reload_extension(f"cogs.{ext[:-3]}")
            await ctx.send("Listo!")

        else:
            for ext in os.listdir("./cogs"):
                if ext.endswith('.py'):
                    try:
                        self.bot.reload_extension(f"cogs.{arg}")
                        return await ctx.send("Listo!")
                    except Exception as e:
                        return await ctx.send(e)


def setup(bot):
    bot.add_cog(Owner(bot))
