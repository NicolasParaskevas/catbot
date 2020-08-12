import random
import requests

class Cat():
    #genereate random meow
    def meow_back(self):
        random.seed()
        e_number = random.randrange(1,5)
        o_number = random.randrange(1,5)
        reply = "m" + (e_number*"e") + (o_number*"o") + "w!"
        return reply

    #right now limit to 1 fact per request
    def send_fact(self):
        resp = requests.get('https://catfact.ninja/facts?limit=1')
        if resp.status_code == 200:
            item = resp.json()
            #return the first fact
            for data in item['data']:
                return data['fact']
    
    def send_image(self):
        resp = requests.get('https://api.thecatapi.com/v1/images/search')
        if resp.status_code == 200:
            for item in resp.json():
                return item['url']