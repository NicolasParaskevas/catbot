import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import cat

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '!')
catbot = cat.Cat()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def meow(ctx):
    await ctx.send(catbot.meow_back())

@client.command()
async def catfact(ctx):
    await ctx.send("{} Cat facts coming soon".format(ctx.message.author.mention))

@client.command()
async def catpic(ctx):
    resp = requests.get('https://api.thecatapi.com/v1/images/search')
    if resp.status_code == 200:
        for item in resp.json():
            await ctx.send(item['url'])


client.run(token)