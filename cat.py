import random

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