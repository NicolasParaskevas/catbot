import os
import discord
import random
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class Cat():
    #genereate random meow
    def meow_back(self):
        e_number = random.randrange(1,3)
        o_number = random.randrange(1,3)
        reply = "m" + (e_number*"e") + (o_number*"o") + "w"
        return reply

    def send_fact(self):
        pass

class Catbot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return 
        if message.content.startswith("!meow"):
            cat = Cat()
            await message.channel.send(cat.meow_back())
        if message.content.startswith("!catpic"):
            resp = requests.get('https://api.thecatapi.com/v1/images/search')
            if resp.status_code == 200:
                for item in resp.json():
                    await message.channel.send(item['url'])
        if message.content.startswith("!catfact"):
            return
client = Catbot()
client.run(token)