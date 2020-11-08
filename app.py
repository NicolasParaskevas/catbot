import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import cat

#load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

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

@client.command()
async def help(ctx):
    help_embed = discord.Embed(
        title = "Catbot",
        url = "https://github.com/NicolasParaskevas/catbot",
        colour = discord.Colour.blue()
    )
    help_embed.add_field(name="!catfact", value="Replies with a fact about cats", inline=False)
    help_embed.add_field(name="!catpic", value="Returns random cat picture", inline=False)
    help_embed.add_field(name="!meow", value="Cat meows back", inline=False)
    help_embed.set_footer(text="Made by Nicolas Paraskevas https://github.com/NicolasParaskevas")
    await ctx.send(embed = help_embed)
    
client.run(token)