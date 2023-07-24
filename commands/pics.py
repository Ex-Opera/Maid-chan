import discord
import aiohttp
import random

class Pics(commands.Cog):
  def __init__(self, Maidchan):
    self.Maidchan = Maidchan
    self.session = aiohttp.ClientSession()

  async def send_pic(self, ctx, url, id):
    try:
      async with self.session.get(url) as response:
        data = await response.json()
        await ctx.channel.send(data[id])
    except Exception as err:
      await ctx.channel.send(f'Master, an error occurred: {err}')

  @commands.command(name="anime", brief="Master i'll send an anime picture!", help="Master i'll send a random anime picture from a given category or pick a random one for you! The available categories are: waifu, neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe.")
  async def anime(self, ctx, *, category=None):
    category = category or random.choice(['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe'])
    await self.send_pic(ctx, f'https://api.waifu.pics/sfw/{category}', "url")

  @commands.command(name="hentai", brief="M-master, i'll send you hentai pictures", help="M-master i'll satisfy your desires by sending a random hentai picture or you can pick from a category. The available categories are: waifu, neko, trap and blowjob")
  async def hentai(self, ctx, *, category=None):
    if ctx.channel.is_nsfw() == True:
       category = category or random.choice(['waifu', 'neko', 'trap', 'blowjob'])
       await self.send_pic(ctx, f"https://api.waifu.pics/nsfw/{category}", "url")
    else:
      await ctx.channel.send("M-master, wrong channel!")

  @commands.command(name="fox", brief="Master i'll send an image of a fox", help="Master i'll send a random image of a fox")
  async def fox(self, ctx):
    await self.send_pic(ctx, "https://randomfox.ca/floof/", "image")

async def setup(Maidchan):
  await Maidchan.add_cog(Pics(Maidchan))
