import random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

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


async def setup(bot):
    await bot.add_cog(Fun(bot))
