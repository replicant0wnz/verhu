import dice
import disnake

from disnake.ext import commands
from disnake.ext.commands import Context

client = disnake.Client()

class Roll(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["r"])
    async def roll(self, context: Context, *, dice_to_roll: str) -> None:

        x = dice.roll(dice_to_roll) 
        total = sum(x)
        description = "` %s %s `" % (total, x)

        embed = disnake.Embed(
                description=description,
                color=0x9C84EF
        )

        await context.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Roll(bot))
