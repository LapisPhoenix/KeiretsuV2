import io
import discord
import datetime
import pyshorteners
from discord.ext import commands
from ext import notifications


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.notifier = notifications.Notifications()

    @commands.command(name='guildinfo', help='Shows debug info about the guild')
    async def guildinfo(self, ctx, guild: discord.Guild = None):
        if guild is None:
            await ctx.reply('Please specify a guild')
            return

        message = f""">>> **Guild Debug**
        **Guild Name:** {guild.name}
        **Guild ID:** {guild.id}
        **Guild Owner:** {guild.owner}
        **Guild Owner ID:** {guild.owner_id}
        **Guild Created At:** {guild.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Guild Member Count:** {guild.member_count}
        **Guild Emoji Count:** {len(guild.emojis)}
        **Guild Role Count:** {len(guild.roles)}
        **Guild Channel Count:** {len(guild.channels)}
        **Guild Text Channel Count:** {len(guild.text_channels)}
        **Guild Voice Channel Count:** {len(guild.voice_channels)}
        **Guild Category Count:** {len(guild.categories)}
        **Guild Boost Tier:** {guild.premium_tier}
        **Guild Boost Count:** {guild.premium_subscription_count}"""

        await ctx.reply(message)

    @commands.command(name='userinfo', help='Shows debug info about the user')
    async def userinfo(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.reply('Please specify a user')
            return

        message = f""">>> **User Debug**
        **User Name:** {user.name}
        **User ID:** {user.id}
        **User Created At:** {user.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **User Bot:** {user.bot}
        **User Avatar:** {user.avatar.url if user.avatar else user.default_avatar.url}
        **User Discriminator:** {user.discriminator if user.discriminator else 'None'}
        **User Flags:** {user.public_flags}
        **User System:** {user.system}
        **User Mention:** {user.mention}"""

        await ctx.reply(message)

    @commands.command(name='channelinfo', help='Shows debug info about the channel')
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            await ctx.reply('Please specify a channel')
            return

        message = f""">>> **Channel Debug**
        **Channel Name:** {channel.name}
        **Channel ID:** {channel.id}
        **Channel Created At:** {channel.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Channel Category:** {channel.category}
        **Channel Position:** {channel.position}
        **Channel NSFW:** {channel.is_nsfw()}
        **Channel Slowmode Delay:** {channel.slowmode_delay}
        **Channel Topic:** {channel.topic}
        **Channel Mention:** {channel.mention}"""

        await ctx.reply(message)

    @commands.command(name='roleinfo', help='Shows debug info about the role')
    async def roleinfo(self, ctx, role: discord.Role = None):
        if role is None:
            await ctx.reply('Please specify a role')
            return

        message = f""">>> **Role Debug**
        **Role Name:** {role.name}
        **Role ID:** {role.id}
        **Role Created At:** {role.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Role Position:** {role.position}
        **Role Color:** {role.color}
        **Role Permissions:** {role.permissions}
        **Role Mention:** {role.mention}"""

        await ctx.reply(message)

    @commands.command(name='emojiinfo', help='Shows debug info about the emoji')
    async def emojiinfo(self, ctx, emoji: discord.Emoji = None):
        if emoji is None:
            await ctx.reply('Please specify an emoji')
            return

        message = f""">>> **Emoji Debug**
        **Emoji Name:** {emoji.name}
        **Emoji ID:** {emoji.id}
        **Emoji Created At:** {emoji.created_at.strftime('%d/%m/%Y %H:%M:%S')}
        **Emoji URL:** {emoji.url}
        **Emoji Animated:** {emoji.animated}
        **Emoji Managed:** {emoji.managed}
        **Emoji Require Colons:** {emoji.require_colons}
        **Emoji Available:** {emoji.available}"""

        await ctx.reply(message)

    @commands.command(name='ping', help='Pong!')
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name='shorten', help='Shortens a URL')
    async def shorten(self, ctx, url):
        s = pyshorteners.Shortener()
        await ctx.reply(s.tinyurl.short(url))

    @commands.command(name='help', help='Shows this message')
    async def help(self, ctx):
        await ctx.reply("[Help Page](<https://github.com/LapisPhoenix/KeiretsuV2/wiki/Documentation>)")

    @commands.command(name='generate_markdown', help='Generates markdown documentation for the bot')
    async def generate_markdown(self, ctx):
        message = "# Keiretsu V2 Documentation\n\n"

        for cog in self.bot.cogs:
            cog = self.bot.get_cog(cog)
            message += f"## {cog.qualified_name}\n\n---\n\n"

            for command in cog.get_commands():
                message += f"### {command.name}\n"
                message += f"**Description:** {command.help}\n <br>"
                message += f"**Usage:** {command.usage}\n <br>"
                message += f"**Aliases:** {command.aliases}\n"
                message += "\n"

            message += "\n---\n\n"

        await ctx.reply(file=discord.File(fp=io.StringIO(message), filename='KeiretsuV2.md'))

    @commands.command(name='uptime', help='Shows the bot\'s uptime')
    async def uptime(self, ctx):
        uptime = datetime.datetime.now() - self.bot.boot_time
        uptime = str(uptime).split('.')[0]
        boot_time = self.bot.boot_time.strftime('%d/%m/%Y %H:%M:%S')
        await ctx.reply(f'Uptime: {uptime} ({boot_time})')

    @commands.command(name='download', help='Links to the github repo')
    async def download(self, ctx):
        await ctx.reply('https://github.com/LapisPhoenix/KeiretsuV2')

    @commands.command(name='watch', help='Whitelists a channel for logging')
    async def watch(self, ctx, channel: discord.TextChannel = None):
        await ctx.message.delete()
        if channel is None:
            self.notifier.show('Keiretsu V2', 'Please specify a channel')
            return

        with open("whitelist.txt", "a") as f:
            channels = f.read().splitlines()
            if channel.id in channels:
                self.notifier.show('Keiretsu V2', 'Channel is already whitelisted')
                return

            f.write(f"{channel.id}\n")
            self.notifier.show('Keiretsu V2', f"Whitelisted {channel.mention}")

    @commands.command(name='unwatch', help='Unwhitelists a channel for logging')
    async def unwatch(self, ctx, channel: discord.TextChannel = None):
        await ctx.message.delete()
        if channel is None:
            self.notifier.show('Keiretsu V2', 'Please specify a channel')
            return

        with open("whitelist.txt", "r") as f:
            channels = f.read().splitlines()
            if channel.id not in channels:
                self.notifier.show('Keiretsu V2', 'Channel is not whitelisted')
                return

        with open("whitelist.txt", "w") as f:
            for line in channels:
                if line != channel.id:
                    f.write(f"{line}\n")

        self.notifier.show('Keiretsu V2', f"Unwhitelisted {channel.mention}")


async def setup(bot):
    await bot.add_cog(Utils(bot))
