import sys
import datetime
import io
import discord
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

    @commands.command(name='help_markdown', help='Gives back the same response as help, but in markdown.')
    async def help_markdown(self, ctx):
        def get_command_info(command, prefix):
            help_msg = f"{prefix}{command.name} "
            if command.params:
                help_msg += ' '.join(f"[{param}]" for param in command.params if param not in ('self', 'ctx'))
            aliases = ', '.join(command.aliases) if command.aliases else 'None'
            return f"| {command.name:<{max_name_length}} | {command.help:<{max_desc_length}} | {help_msg:<40} | {aliases} |"

        def process_command(command, prefix):
            nonlocal max_name_length, max_desc_length
            command_message = get_command_info(command, prefix)
            messages.append(command_message)
            if isinstance(command, commands.Group):
                for subcommand in command.commands:
                    process_command(subcommand, f"{prefix}{command.name} ")

        max_name_length = max(len(command.name) for command in self.bot.commands if not command.hidden)
        max_desc_length = max(len(command.help) for command in self.bot.commands if not command.hidden)

        header = "| Command" + " " * (max_name_length - 7) + "| Description" + " " * (
                max_desc_length - 11) + "| Usage                                      | Aliases |\n"
        header += "| " + "-" * (max_name_length + 2) + "| " + "-" * (max_desc_length + 2) + "| " + "-" * 42 + "| " + "-" * 8 + " |\n"
        messages = []

        for command in self.bot.commands:
            if command.hidden:
                continue
            process_command(command, self.bot.command_prefix)

        # Use join to concatenate messages with only a single newline
        await ctx.reply(file=discord.File(fp=io.StringIO(header + '\n'.join(messages)), filename='help.md'))


async def setup(bot):
    await bot.add_cog(Dev(bot))
