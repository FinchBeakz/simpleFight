import math
import random
random.seed()


class Character:
    def __init__(self, name, dead):
        self.name = name
        self.experience = {"exp":0,
                      "lvl":1}
        self.dead = dead
        self.stats = {"hp":10,
                      "str":5,
                      "dex":5,
                      "int":5,
                      "b_att":2,
                      "att":0}
        
    def update_exp(self, exp_gained): #100 exp = 1 level (for now)
        print("You gained", exp_gained, "Experience Points!")
        old_level = self.experience["lvl"]
        self.experience["exp"] += exp_gained
        self.experience["lvl"] = math.floor(self.experience["exp"] / 100 + 1)
        if self.experience["lvl"] > old_level:
            print("level Up!")
        


c1 = Character("hans", 0)
print(c1.experience)

c1.update_exp(99)

print(c1.experience)

c1.update_exp(2)

print(c1.experience)