#simpleFight0_.py - characters can die, if both are dead, fight goes on and the living character will be attacked
# also you can now heal for the "int" value in Character.stats, both chars at once without any costs
import random
random.seed()

#some classes
class Enemy:
    def __init__(self, stats):
        self.stats = stats

class Character:
    def __init__(self, stats):#toDo: Inventory/equipped items
        self.stats = stats

#some functions
def chkInt(): #turn input into integer
    chk = 0
    while chk == 0:
        x = input()
        try:
            y = int(x)
            chk = 1
            return y
        except:
            print('number error')
            
def attack(att, hp): #substracting attack value from hp / maybe use this to differentiate between melee/magic/ranged attacks?
    hp -= att
    return hp

def hitRange(hitB, mod_val): #defining the attack value range
    x = int(hitB)-1
    y = int(hitB)+1
    z = random.randint(x,y) + mod_val
    return z

def init_partyList(): #mostly fixed stats
    pL = []
    print("You will play as two different characters. What are their names?")
    for n in range(2):
        print("Name of charakter", n +1)
        name = str(input())
        pL.append(Character({"name":name,"str":5, "dex":5, "int":10, "hp":15, "hitBase":2, "hit":0, "dead":0}))
    return pL
          
    

def init_monsterList(m_class, x, y): #make a list of monsters with a rng count of x to y monsters
    monster_list = []
    for m_cnt in range(x, y):
        monster = m_class({"name":"Monster", "str":2, "hp":10, "att":0, "hitBase":2, "hit":0})
        monster_list.append(monster)
    return monster_list

menu = 1 #setting up the game loop
score = 0

#initiate party "party_list
party_list = init_partyList()
c1 = party_list.pop(0)
c2 = party_list.pop(0)

#initiate monster_list, random length 0 - (1-5)
monster_list = init_monsterList(Enemy, 0, random.randint(1,5))


if len(monster_list) > 1:
    print("You are facing ", len(monster_list), " Enemies!")
else:
    print("You are facing ", len(monster_list), " Enemy!")

mon = monster_list.pop(0) #loading first monster
mon_hp = mon.stats["hp"]
mon_att = hitRange(mon.stats["hitBase"], mon.stats["str"])
#make a Dungeon

while menu > 0: #run game, exit if input = 0
    
    #load new monster:
    if mon_hp <= 0:
        try:
            mon = monster_list.pop(0)
            mon_hp = mon.stats["hp"]
            print(len(monster_list) + 1, " Monsters remaining!")
        except:
            break
    
    print('')
    print('Select Action \n (1)Fight \n (2)Heal \n (3)Flee \n (0)Exit')
    menu = chkInt()
    
    if menu == 1: #fighting
        if mon == None:
            break
            
        if c1.stats["dead"]:
            print(c1.stats["name"], " is dead.")
        else:
            print(c1.stats["name"], " attacks!")
            mon_hp = attack(c1.stats["hitBase"], mon_hp) #c1 attack
            
        if c2.stats["dead"]:
            print(c1.stats["name"], " is dead.")
        else:
            print(c2.stats["name"], " attacks!")
            mon_hp = attack(c2.stats["hitBase"], mon_hp) #c2 attack
        
        rng = random.randint(1,2)
        if rng == 1:
            if c1.stats["dead"]:
                c2.stats["hp"] = attack(mon_att, c2.stats["hp"])
            else:
                c1.stats["hp"] = attack(mon_att, c1.stats["hp"]) #monster attack
                if c1.stats["hp"] <= 0:
                    print(c1.stats["name"], " died.")
                    c1.stats["dead"] = 1
        if rng == 2:
            if c2.stats["dead"]:
                c1.stats["hp"] = attack(mon_att, c1.stats["hp"])
            else:
                c2.stats["hp"] = attack(mon_att, c2.stats["hp"]) #monster attack
                if c2.stats["hp"] <= 0:
                    print(c2.stats["name"], " died.")
                    c2.stats["dead"] = 1
        
        if mon_hp <= 0 and c2.stats["hp"] > 0 and c1.stats["hp"] > 0:
            score += 1
            continue
        elif c1.stats["hp"] <= 0 and c2.stats["hp"] <= 0:
            print("you loose")
            break
        
        print(c1.stats["name"], ": ", c1.stats["hp"], "\n", c2.stats["name"], ": ", c2.stats["hp"], "\nMonster Hp: ", mon_hp, "\n\n")
        
            
    elif menu == 2: #toDo: set playerHp Max! #healing
        c1.stats["hp"] += c1.stats["int"]
        c2.stats["hp"] += c2.stats["int"]
        print("You healed for ", c1.stats["int"], " Hp.")

    elif menu == 3: #ToDo: needs to do something #fleeing
        print("flee!")

if score != 1:
    print("You Defeated ", score, " Monsters!")
else:
    print("You Defeated ", score, " Monster!")


