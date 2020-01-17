# Work with Python 3.6
import os
import discord
from discord.ext import commands

TOKEN = 'NjY3MjI4ODE2NjUyODk0MjQw.XiCiqA.TyqcocuOMbZ77TDI8I3iE-_FPZo'

client = commands.Bot(command_prefix = '!')

@client.command()
async def ping(ctx):
    await ctx.send('pong (round(client.latency*1000))')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)