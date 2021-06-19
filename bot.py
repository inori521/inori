import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('ODU1Nzc1MjA4MDA3MTM5MzI4.YM3YxQ.LDhdhee6zG2V81M1Tlu6BX6F4Ew')