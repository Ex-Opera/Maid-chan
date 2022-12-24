import discord
from discord.ext import commands
from commands.engine.dice.Dice import *

class Recreation(commands.Cog):
  def __init__(self, Maidchan):
    self.Maidchan = Maidchan

  @commands.command()
  async def dice(self, ctx, *, dice):
    dice = Dice(dice)
    rolls, bonus, total = dice.roll()
    await ctx.send(f"Rolls: {rolls} Bonus: {bonus} -> {total}")

async def setup(Maidchan):
  await Maidchan.add_cog(Recreation(Maidchan))
