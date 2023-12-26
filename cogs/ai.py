import io
import aiohttp
from discord.ext import commands


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


async def setup(bot):
    await bot.add_cog(AI(bot))