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

    def send_fact(self):
        pass
    
    def send_image(self):
        resp = requests.get('https://api.thecatapi.com/v1/images/search')
        if resp.status_code == 200:
            for item in resp.json():
                return item['url']