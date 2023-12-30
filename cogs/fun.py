import random
import io
import asyncio
import discord
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

    @commands.command(name='empty', help='Sends an empty message')
    async def empty(self, ctx):
        await ctx.message.delete()
        await ctx.send('** **')

    @commands.command(name='morse', help='Converts text to morse code')
    async def morse(self, ctx, *, message: str = None):
        MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
                      'D': '-..', 'E': '.', 'F': '..-.',
                      'G': '--.', 'H': '....', 'I': '..',
                      'J': '.---', 'K': '-.-', 'L': '.-..',
                      'M': '--', 'N': '-.', 'O': '---',
                      'P': '.--.', 'Q': '--.-', 'R': '.-.',
                      'S': '...', 'T': '-', 'U': '..-',
                      'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '1': '.----',
                      '2': '..---', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...',
                      '8': '---..', '9': '----.', '0': '-----'}
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        morse = ''
        for char in message:
            if char.isalpha():
                morse += f'{MORSE_CODE[char.upper()]} '
            elif char == ' ':
                morse += ' '
            else:
                morse += f'{char}\n'

        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(morse)
        else:
            await ctx.reply(morse)

    @commands.command(name='unmorse', help='Converts morse code to text')
    async def unmorse(self, ctx, *, message: str = None):
        MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
                      'D': '-..', 'E': '.', 'F': '..-.',
                      'G': '--.', 'H': '....', 'I': '..',
                      'J': '.---', 'K': '-.-', 'L': '.-..',
                      'M': '--', 'N': '-.', 'O': '---',
                      'P': '.--.', 'Q': '--.-', 'R': '.-.',
                      'S': '...', 'T': '-', 'U': '..-',
                      'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '1': '.----',
                      '2': '..---', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...',
                      '8': '---..', '9': '----.', '0': '-----'}
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        text = ''
        for char in message.split(' '):
            if char in MORSE_CODE.values():
                text += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(char)]
            elif char == '':
                text += ' '
            else:
                text += f'{char}\n'

        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(text)
        else:
            await ctx.reply(text)

    @commands.command(name='clap', help='Adds clap emojis between words')
    async def clap(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to clap')
            return

        clap = ' 👏 '.join(message.split(' '))

        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(clap)
        else:
            await ctx.reply(clap)

    @commands.command(name='count', help='Counts down from n to x')
    async def count(self, ctx, start: int = 1, end: int = 10):
        if start >= end:
            await ctx.reply('End must be greater than start')
            return

        limit = 420     # haha funny number, also a good limit

        if start > limit or end > limit:
            await ctx.reply(f'Start and end must be less than {limit}')
            return

        message = ''
        for i in range(start, end):
            message += f'{i}, '

        if len(message) > 2000:
            await ctx.reply('Message too long, try a smaller range')
            return

        message += str(end)
        await ctx.reply(message)

    @commands.command(name='charspoil', help='Spoils a message character by character')
    async def charspoil(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to spoil')
            return

        spoil = ''
        for char in message:
            spoil += f'||{char}||'

        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(spoil)
        else:
            await ctx.reply(spoil)

    @commands.command(name='ascii', help='Converts text to ascii art')
    async def ascii(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        ascii = ''
        for char in message:
            ascii += f'`{ord(char)}` '

        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(ascii)
        else:
            await ctx.reply(ascii)

    @commands.command(name='hexify', help='Converts text to hex')
    async def hexify(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        hex = ''
        for char in message:
            hex += f'{ord(char):x} '.upper()
        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(hex)
        else:
            await ctx.reply(hex)

    @commands.command(name='unhexify', help='Converts hex to text')
    async def unhexify(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        text = ''
        for char in message.split(' '):
            text += chr(int(char, 16))
        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(text)
        else:
            await ctx.reply(text)

    @commands.command(name='binary', help='Converts text to binary')
    async def binary(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        binary = ''
        for char in message:
            binary += f'{ord(char):b} '
        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(binary)
        else:
            await ctx.reply(binary)

    @commands.command(name='unbinary', help='Converts binary to text')
    async def unbinary(self, ctx, *, message: str = None):
        if ctx.message.reference and not message:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            message = msg.content

        if not message:
            await ctx.reply('Please provide a message to convert')
            return

        text = ''
        for char in message.split(' '):
            text += chr(int(char, 2))
        # Reply to the message if it was a reply
        if ctx.message.reference:
            await ctx.message.reference.resolved.reply(text)
        else:
            await ctx.reply(text)

    @commands.command(name='0=1', help='Proves 0=1')
    async def zero_equals_one(self, ctx):
        await ctx.reply(""" # Why 1 = 2 and 0 = 1.

In math, there are many rules, but 1 rule particularly is important. You cannot divide by 0. Why? We are always told that dividing by 0 is impossible, and even our calculators error when we try to do this supposedly impossible feat. But what if it's its not?

Normally, when you divide smaller numbers the outcome is bigger, and vise versa, example:

```10 ÷ 2 = 5
10 ÷ 1/2 = 20
10 ÷ 1/4 = 40
10 ÷ 0.1 = 100```

So on, you'd think if you keep dividing by smaller and smaller numbers you'll reach infinity, right? 10/x = y.
Using this assumption, then 10 ÷ 0 = ∞. But this is an assumption, by thinking about it further, all we know is that if we divide 10 by a number that tends towards 0, then we get an answer that tends towards infinity. But this does not mean 10 divided by 0 is equal to infinity. Confused yet?

What is division exactly? For example 10 ÷ 2 could mean "*how many times do I need to add 2 to make 10, or 2 times what makes 10*". Dividing be a number is the reverse of multiplication. If we multiply any number, y, by a given number, x, can we multiple x with another number to get back to y, we will call the result z. y(x) = z(?) = y. For example, if we preform this 3(2) we get 6, then you can multiply by 1/2 to get back to 3.  Thus the multiplicative inverse of 2 is 1/2, and the multiplicative of 10 is 1/10. Notice, if we multiply these multiplicative numbers together we always get 1. Try this yourself, do 2(1/2) or 10(1/10). It always equals 1.

If we want to divide 0 we need to find its multiplicative inverse, which should be 1/0.  0(1/2) = 1? Well no. Anything multiplied by 0 is still 0, 
1(0) = 0 or 7(0) = 0 for example. Finding the multiplicative inverse is impossible. Zero has no multiplicative inverse. 

Lets say ∞ = 1/0, based on the definition of a multiplicative inverse previously stated, 0(∞) = 1. That means 0(∞) + 0(∞) = 2, simplify, 0(∞) = 2! If 0(∞) = 1 is true, and 0(∞) = 2 is true, then

# 1 = 2, thus 0 = 1""")

    @commands.command(name='pi', help='Gives back pi to the nth digit')
    async def pi(self, ctx, digits: int = 100):
        if digits > 1_000_001:
            await ctx.reply('Please provide a within 1,000,000 digits')
            return

        with open('assets/commands/pi.txt', 'r') as f:
            pi = f.read()

        await ctx.reply(file=discord.File(fp=io.StringIO(pi[:digits]), filename='pi.txt'))


async def setup(bot):
    await bot.add_cog(Fun(bot))
