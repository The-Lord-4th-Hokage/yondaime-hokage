import discord
from discord.ext import commands
import requests 

class Vocaloid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.endpoint = 'https://api.meek.moe/'

    @commands.command()
    async def rin(self, ctx):
        data = requests.get(url=self.endpoint + 'rin').json()['url']
        await ctx.send(data)

    @commands.command()
    async def rin(self, ctx):
        data = requests.get(url=self.endpoint + 'rin').json()['url']
        await ctx.send(data)

    @commands.command()
    async def una(self, ctx):
        data = requests.get(url=self.endpoint + 'una').json()['url']
        await ctx.send(data)

    @commands.command()
    async def gumi(self, ctx):
        data = requests.get(url=self.endpoint + 'gumi').json()['url']
        await ctx.send(data)

    @commands.command()
    async def ia(self, ctx):
        data = requests.get(url=self.endpoint + 'ia').json()['url']
        await ctx.send(data)

    @commands.command()
    async def luka(self, ctx):
        data = requests.get(url=self.endpoint + 'luka').json()['url']
        await ctx.send(data)

def setup(bot):
    bot.add_cog(Vocaloid(bot))
