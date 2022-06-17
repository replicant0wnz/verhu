import yaml
import random
import disnake

from disnake.ext import commands
from disnake.ext.commands import Context

class Psalm(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        f = open("psalms.yml")
        self.psalms = yaml.safe_load(f)

    @commands.command(aliases=["p"])
    async def psalm(self, context: Context) -> None:

        psalm = random.choice(self.psalms['psalms'])
        description= f"`{psalm}`"

        embed = disnake.Embed(
                description=description,
                color=0x9C84EF
        )

        await context.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Psalm(bot))
