import os
import difflib
import random
import re
import aiohttp
import asyncio
from colorama import Fore
from discord.ext import commands
from ext import notifications


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.regex = re.compile(r'(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)')
        self.notifier = notifications.Notifications()
        self.log_channel_id = int(os.environ.get('LOG_CHANNEL'))
        self.log_channel = self.bot.get_channel(self.log_channel_id)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            command = ctx.message.content.split()[0][1:]
            commands_list = [command.name for command in self.bot.commands]
            close_commands = difflib.get_close_matches(command, commands_list)
            if len(close_commands) == 0:
                await ctx.reply(f'Command not found')
            else:
                await ctx.reply(f'Command not found, did you mean {close_commands[0]}?')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f'Missing required argument: {error.param}')
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(f'Bad argument: {error}')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(f'Missing permissions: {error}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.regex.search(message.content):
            code = self.regex.search(message.content).group(2)
            if len(code) != 16 and len(code) != 24:
                print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Found a fake nitro code: {code}')
            try:
                print(f'[{Fore.GREEN}NITRO SNIPER{Fore.RESET}] Found a nitro code: {code}')
                self.notifier.show('Nitro Sniper', f'Found a nitro code in {message.guild.name if message.guild else "DMs"}')
                async with aiohttp.ClientSession() as session:
                    async with session.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                                            headers={'authorization': self.bot.http.token}) as r:
                        if 'This gift has been redeemed already.' in await r.text():
                            print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Failed to redeem nitro code: {code} (already redeemed)')
                            self.notifier.show('Nitro Sniper', f'Failed to redeem nitro code: {code} (already redeemed)')
                        elif 'nitro' in await r.text():
                            print(f'[{Fore.GREEN}NITRO SNIPER{Fore.RESET}] Successfully redeemed nitro code: {code}')
                            self.notifier.show('Nitro Sniper', f'Successfully redeemed nitro code: {code}')
                        else:
                            print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Failed to redeem nitro code: {code}')
                            self.notifier.show('Nitro Sniper', f'Failed to redeem nitro code: {code}')
            except Exception as e:
                print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Failed to redeem nitro code: {code} ({e})')

        elif '**giveaway**' in message.content.lower() or ('react with' in message.content.lower() and 'giveaway' in message.content.lower()):
            try:
                await asyncio.sleep(random.randint(60, 120))
                await message.add_reaction('🎉')
                print(f'[{Fore.GREEN}GIVEAWAY SNIPER{Fore.RESET}] Successfully reacted to giveaway')
                self.notifier.show('Giveaway Sniper', f'Entered a giveaway in {message.guild.name}')
            except Exception as e:
                print(f'[{Fore.RED}GIVEAWAY SNIPER{Fore.RESET}] Failed to react to giveaway ({e})')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if self.regex.search(after.content):
            code = self.regex.search(after.content).group(2)
            if len(code) != 16 and len(code) != 24:
                print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Found a fake nitro code: {code}')
            try:
                print(f'[{Fore.GREEN}NITRO SNIPER{Fore.RESET}] Found a nitro code: {code}')
                self.notifier.show('Nitro Sniper', f'Found a nitro code in {after.guild.name if after.guild else "DMs"}')
                async with aiohttp.ClientSession() as session:
                    async with session.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                                            headers={'authorization': self.bot.http.token}) as r:
                        if 'This gift has been redeemed already.' in await r.text():
                            print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Failed to redeem nitro code: {code} (already redeemed)')
                            self.notifier.show('Nitro Sniper', f'Failed to redeem nitro code: {code} (already redeemed)')
                        elif 'nitro' in await r.text():
                            print(f'[{Fore.GREEN}NITRO SNIPER{Fore.RESET}] Successfully redeemed nitro code: {code}')
                            self.notifier.show('Nitro Sniper', f'Successfully redeemed nitro code: {code}')
                        else:
                            print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Failed to redeem nitro code: {code}')
                            self.notifier.show('Nitro Sniper', f'Failed to redeem nitro code: {code}')
            except Exception as e:
                print(f'[{Fore.RED}NITRO SNIPER{Fore.RESET}] Failed to redeem nitro code: {code} ({e})')

        # with open("channels.txt", "r") as f:
        #     channels = f.read().splitlines()
        #     if after.channel.id in channels:
        #         message = f"**Message edited in {after.channel.mention}**\n" \
        #                   f"**Before:** `{before.content}`\n" \
        #                   f"**After:** `{after.content}`\n" \
        #                   f"**Author:** {after.author.mention}"
#
        #         await self.log_channel.send(message)

    # @commands.Cog.listener()
    # async def on_message_delete(self, message):
    #     with open("channels.txt", "r") as f:
    #         channels = f.read().splitlines()
    #         if message.channel.id in channels:
    #             message = f"**Message deleted in {message.channel.mention}**\n" \
    #                       f"**Content:** `{message.content}`\n" \
    #                       f"**Author:** {message.author.mention}"
#
    #             await self.log_channel.send(message)


async def setup(bot):
    await bot.add_cog(Events(bot))
