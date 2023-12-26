import random
import asyncio
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    def load_animation(self, path) -> tuple[list[str], int | float]:
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

    @commands.command(name='rayhero', help='Rayhero')
    async def rayhero(self, ctx):
        frames, duration = self.load_animation('anims/rayhero.txt')
        message = await ctx.reply(frames[0])
        for frame in frames:
            await asyncio.sleep(duration)
            await message.edit(content=frame)


async def setup(bot):
    await bot.add_cog(Fun(bot))
