# Work with Python 3.6
import os
import discord
from discord.ext import commands
from get_token import discord_token
 
client = commands.Bot(command_prefix = '!')
TOKEN = discord_token()

@client.command()
async def ping(ctx):
    await ctx.send(F'pong {round(client.latency*1000)}')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN, bot = True)