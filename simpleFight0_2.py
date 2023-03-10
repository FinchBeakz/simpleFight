#simpleFight0_2.py - adding rng
import random
random.seed()

#some classes

#some functions
def chkInt():
    chk = 0
    while chk == 0:
        x = input()
        try:
            y = int(x)
            chk = 1
            return y
        except:
            print('number error')
def attack(att, hp):
    hp -= att
    return hp

def hitRange(hitB):
    x = int(hitB)-1
    y = int(hitB)+1
    z = random.randint(x,y)
    return z

menu = 1

#enemy
enemyHp = 10
enemyAtt = 0
enemyHitB = 2
enemyHit = 0

#player
playerHp = 15
playerAtt = 0
playerHitB = 3
playerHit = 0

score = 0

while menu > 0: #run game, exit if input = 0
    print('HP:', playerHp)
    print('Enemy:', enemyHp)
    print('')
    print('Select Action \n (1)Fight  \n (2)Flee \n (0)Exit')
    menu = chkInt()
    
    if menu == 1:
        print("fight!")
        playerAtt = hitRange(playerHitB)
        enemyAtt = hitRange(enemyHitB)
        enemyHp = attack(playerAtt, enemyHp)
        print("You attack the Enemy for ", playerAtt, " Damage!")
        playerHp = attack(enemyAtt, playerHp)
        print("The enemy attacks you for ", enemyAtt, " Damage!")
        
        if enemyHp <= 0 and playerHp > 0:
            print("You win!")
            score+=1
            enemyHp = 10
        elif playerHp <= 0:
            print("You loose!")
            menu = 0
        

    elif menu == 2:
        print("flee!")

print("You Defeated ", score, " Monsters!")