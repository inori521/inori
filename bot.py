import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODU1Nzc1MjA4MDA3MTM5MzI4.YM3YxQ.LFPApUwHNQvTgIs2sm44BcFIOC0')