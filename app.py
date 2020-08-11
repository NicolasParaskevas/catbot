import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import cat

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

catbot = cat.Cat()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!meow"):
        await message.channel.send(catbot.meow_back())

    if message.content.startswith("!catpic"):
        resp = requests.get('https://api.thecatapi.com/v1/images/search')
        if resp.status_code == 200:
            for item in resp.json():
                await message.channel.send(item['url'])
    
    if message.content.startswith("!catfact"):
        await message.channel.send("@" + message.author.name + " Cat facts coming soon")

client.run(token)