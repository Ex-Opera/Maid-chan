import discord
import aiohttp
import random

class Pics(commands.Cog):
  def __init__(self, Maidchan):
    self.Maidchan = Maidchan
    self.session = aiohttp.ClientSession()

  async def send__pic(self, ctx, url, id):
    try:
      async with self.session.get(url) as response:
        data = await response.json()
        await ctx.channel.send(data[id])
    except Exception as err:
      await ctx.channel.send(f'Master, an error occurred: {err}')

  @commands.command(name="anime", brief="Sends a random anime picture", help="Sends a random anime picture from a given category or a random one. The available categories are: waifu, neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe.")
  async def anime(self, ctx, *, category=None):
    category = category or random.choice(['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe'])
    await self.send_pic(ctx, f'https://api.waifu.pics/sfw/{category}', "url")

  @commands.command()
  async def hentai(self, ctx, *, category=None):
    if ctx.channel.is_nsfw() == True:
       category = category or random.choice(['waifu', 'neko', 'trap', 'blowjob'])
       await self.send_pic(ctx, f"https://api.waifu.pics/nsfw/{category}", "url")
     else:
       await ctx.channel.send("M-master, wrong channel!")

  @commands.command()
  async def fox(self, ctx):
    await self.send_pic(ctx, "https://randomfox.ca/floof/", "image")

async def setup(Maidchan):
  await Maidchan.add_cog(Pics(Maidchan))
