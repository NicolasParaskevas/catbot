import os
import discord
from discord.ext import commands
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
    await ctx.send("{} {}".format(ctx.message.author.mention, catbot.send_fact()))

@client.command()
async def catpic(ctx):
    await ctx.send(catbot.send_image())
    
client.run(token)