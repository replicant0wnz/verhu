import disnake
import yaml

from disnake.ext import commands
from disnake.ext.commands import Context
from disnake.ext.commands import Context

client = disnake.Client()

class Character(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def create(self, message):
        print(message.content)

def setup(bot: commands.Bot):
    bot.add_cog(Character(bot))
