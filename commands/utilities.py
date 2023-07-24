import discord
import aiohttp
import config
from discord.ext import commands
from discord.ext.commands import bot
from random import choice
# from main import Maidchan


class Utilities(commands.Cog):
  def __init__(self, Maidchan):
    self.Maidchan = Maidchan

  @commands.command()
  async def say(self, ctx, *, said):
    await ctx.send(said)
    await ctx.message.delete()

  @commands.command()
  async def avatar(self, ctx, *, user: discord.Member = None):
    user = user or ctx.author
    await ctx.send(user.avatar.url)

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'Pong! {round(self.Maidchan.latency * 1000)}ms')

  @commands.command()
  async def translate(self, ctx, *, input_text):
    language = input_text[:2]
    url = f"https://translation.googleapis.com/language/translate/v2?key={config.translate_key}"
    input_translate = {
        "q": input_text[3:],
        "target": language,
        "format": "text",
    }
    async with aiohttp.ClientSession() as session:
      async with session.post(url, json=input_translate) as res:
        data = await res.json()
        await ctx.send(
            f"Detected language: {data['data']['translations'][0]['detectedSourceLanguage']} \nTranslation: {data['data']['translations'][0]['translatedText']}"
        )


async def setup(Maidchan):
  await Maidchan.add_cog(Utilities(Maidchan))
