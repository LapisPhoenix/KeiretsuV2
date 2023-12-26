import random
import asyncio
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @staticmethod
    def load_animation(path) -> tuple[list[str], int | float]:
        with open(path, 'r') as f:
            f.seek(0)
            duration = float(f.readline())
            frames = f.read().split('---')
            frames[0] = frames[0][3:]

        return frames, duration

    @commands.command(name='8ball', help='Ask the magic 8ball a question')
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.reply(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(name='coinflip', help='Flips a coin')
    async def coinflip(self, ctx):
        responses = ['Heads', 'Tails']
        await ctx.reply(random.choice(responses))

    @commands.command(name='roll', help='Rolls a dice', aliases=['dice'])
    async def roll(self, ctx, *, max: int = 6):
        await ctx.reply(random.choice(range(1, max + 1 if max == 1 else max)))

    @commands.command(name='bomb', help='Message will detinate in 5 seconds')
    async def bomb(self, ctx):
        countdown = 5
        message = await ctx.reply(f'THIS MESSAGE WILL DETINATE IN {countdown} SECONDS')
        while countdown != 0:
            await asyncio.sleep(0.8)
            countdown -= 1
            await message.edit(content=f'THIS MESSAGE WILL DETINATE IN {countdown} SECONDS')

        await message.edit(content=':bomb:')
        await asyncio.sleep(0.8)
        await message.edit(content=':fire:')

    @commands.command(name='mock', help='Mocks a message')
    async def mock(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to mock')
            return

        cap = True
        for i in range(len(message)):
            if message[i].isalpha():
                if cap:
                    message = message[:i] + message[i].upper() + message[i + 1:]
                else:
                    message = message[:i] + message[i].lower() + message[i + 1:]
                cap = not cap

        await ctx.message.delete()

        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(message)
        else:
            await ctx.reply(message)


async def setup(bot):
    await bot.add_cog(Fun(bot))
