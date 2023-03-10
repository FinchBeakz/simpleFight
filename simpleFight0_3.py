#simpleFight0_3.py - adding monster_list to populate with a random amount of enemies, adding a healing step to test (survive) monster list
import random
random.seed()

#some classes
class Enemy:
    def __init__(self, stats):
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
            
def attack(att, hp): #substracting attack value from hp
    hp -= att
    return hp

def hitRange(hitB, mod_val): #defining the attack value range
    x = int(hitB)-1
    y = int(hitB)+1
    z = random.randint(x,y) + mod_val
    return z

def init_monsterList(m_class, x, y): #make a list of monsters with a rng count of x to y monsters
    monster_list = []
    for m_cnt in range(x, y):
        monster = m_class({"str":2, "hp":10, "att":0, "hitBase":2, "hit":0})
        monster_list.append(monster)
    return monster_list

menu = 1 #setting up the game loop

#initiate monster_list, random length 0 - (1-5)
monster_list = init_monsterList(Enemy, 0, random.randint(1,5))

#player
playerStr = 2
playerHp = 15
playerAtt = 0
playerHitB = 3
playerHit = 0
heal_pwr = 10

score = 0
if len(monster_list) > 1:
    print("You are facing ", len(monster_list), " Enemies!")
else:
    print("You are facing ", len(monster_list), " Enemy!")
mon = monster_list.pop(0)
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
            score += 1
        except:
            break
    
    print('')
    print('Select Action \n (1)Fight \n (2)Heal \n (3)Flee \n (0)Exit')
    menu = chkInt()
    
    if menu == 1: #fighting
        if mon == None:
            break

        mon_hp = attack(playerHitB, mon_hp)
        playerHp = attack(mon_att, playerHp)
        
        if mon_hp <= 0 and playerHp >0:
            continue
        elif playerHp <= 0:
            print("you loose")
            break
        
        print("Your Hp: ", playerHp, "\nMonster Hp: ", mon_hp, "\n\n")
        
            
    elif menu == 2: #toDo: set playerHp Max! #healing
        playerHp += heal_pwr
        print("You healed for ", heal_pwr, " Hp.")

    elif menu == 3: #ToDo: needs to do something #fleeing
        print("flee!")

if score > 1:
    print("You Defeated ", score, " Monsters!")
else:
    print("You Defeated ", score, " Monster!")


#-----------code dump----------
#   #Old if menu == 1:
#         print("fight!")
#         playerAtt = hitRange(playerHitB)
#         enemyAtt = hitRange(enemyHitB)
#         enemyHp = attack(playerAtt, enemyHp)
#         print("You attack the Enemy for ", playerAtt, " Damage!")
#         playerHp = attack(enemyAtt, playerHp)
#         print("The enemy attacks you for ", enemyAtt, " Damage!")
#         
#         if enemyHp <= 0 and playerHp > 0:
#             print("You win!")
#             score+=1
#             enemyHp = 10
#         elif playerHp <= 0:
#             print("You loose!")
#             menu = 0