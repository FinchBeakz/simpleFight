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
                      "base_att":2,
                      "att":0}
        
    def update_exp(self, exp_gained): #100 exp = 1 level (for now)
        print("You gained", exp_gained, "Experience Points!")
        old_level = self.experience["lvl"]
        self.experience["exp"] += exp_gained
        self.experience["lvl"] = math.floor(self.experience["exp"] / 100 + 1)
        if self.experience["lvl"] > old_level:
            print("level Up!")

def manage_list(action, lst, item): #load and save (character) list
    if action == "load":
        item = lst.append(0)
    else:
        print("wrong action")
    return lst

        
c1 = Character("hans", 0)
c2 = Character("blubb", 0)

character_list = [c1, c2]

character_list = manage_list("load", character_list, c1)
print(character_list(0).stats["name"])

print(c1.experience)

c1.update_exp(99)
print(c1.experience)
c1.update_exp(2)
print(c1.experience)
