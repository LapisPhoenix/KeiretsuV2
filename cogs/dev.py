import sys
import datetime
from discord.ext import commands


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name='reload', help='Reloads a cog')
    async def reload(self, ctx, cog):
        try:
            await self.bot.reload_extension(f'cogs.{cog}')
            await ctx.reply(f'Reloaded {cog}')
        except commands.ExtensionNotLoaded:
            await ctx.reply(f'Cog {cog} is not loaded')
        except commands.ExtensionNotFound:
            await ctx.reply(f'Cog {cog} was not found')
        except commands.ExtensionFailed:
            await ctx.reply(f'Cog {cog} failed to load')
        except commands.ExtensionAlreadyLoaded:
            await ctx.reply(f'Cog {cog} is already loaded')

    @commands.command(name='unload', help='Unloads a cog')
    async def unload(self, ctx, cog):
        try:
            await self.bot.unload_extension(f'cogs.{cog}')
            await ctx.reply(f'Unloaded {cog}')
        except commands.ExtensionNotLoaded:
            await ctx.reply(f'Cog {cog} is not loaded')
        except commands.ExtensionNotFound:
            await ctx.reply(f'Cog {cog} was not found')
        except commands.ExtensionFailed:
            await ctx.reply(f'Cog {cog} failed to load')
        except commands.ExtensionAlreadyLoaded:
            await ctx.reply(f'Cog {cog} is already loaded')

    @commands.command(name='load', help='Loads a cog')
    async def load(self, ctx, cog):
        try:
            await self.bot.load_extension(f'cogs.{cog}')
            await ctx.reply(f'Loaded {cog}')
        except commands.ExtensionNotLoaded:
            await ctx.reply(f'Cog {cog} is not loaded')
        except commands.ExtensionNotFound:
            await ctx.reply(f'Cog {cog} was not found')
        except commands.ExtensionFailed:
            await ctx.reply(f'Cog {cog} failed to load')
        except commands.ExtensionAlreadyLoaded:
            await ctx.reply(f'Cog {cog} is already loaded')

    @commands.command(name='shutdown', help='Shuts down the bot')
    async def shutdown(self, ctx):
        await ctx.reply('Shutting down')
        await self.bot.close()
        sys.exit()

    @commands.command(name='botdebug', help='Shows debug info about the bot')
    async def botdebug(self, ctx):
        uptime = datetime.datetime.now() - self.bot.boot_time
        uptime = str(uptime).split('.')[0]
        boot_time = self.bot.boot_time.strftime('%d/%m/%Y %H:%M:%S')
        message = f""">>> **Bot Debug**
        **Bot**: Keiretsu V2 - By Lapis Pheonix
        **Bot Version:** {self.bot.__version__}
        **Bot Prefix:** {self.bot.command_prefix}
        **Bot Latency:** {round(self.bot.latency * 1000)}ms
        **Connected Guilds:** {len(self.bot.guilds)}
        **Connected Users:** {len(self.bot.users)}
        **Loaded Emojis:** {len(self.bot.emojis)}
        **Loaded Cogs:** {len(self.bot.cogs)}
        **Loaded Commands:** {len(self.bot.commands)}, `{', '.join([command.name for command in self.bot.commands])}`
        **Bot Uptime:** {uptime} ({boot_time})"""

        await ctx.reply(message)


async def setup(bot):
    await bot.add_cog(Dev(bot))
