import discord
import pyshorteners
from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

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


async def setup(bot):
    await bot.add_cog(Utils(bot))
