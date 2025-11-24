#game 2
import os
from random import randint
lives=3
status=True
suma=0
def roll_dice():
    dice1=randint(1,6)
    dice2=randint(1,6)
    return dice1,dice2

#print(roll_dice())

while True:
    key = input("Press any key to roll dices : ")
    dices = roll_dice()
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")
    suma+=1
    if (dices[0]+dices[1])%2==0:
        lives+=1
    else:
        lives-=1
    if dices[0]==6 and dices[1]==6:
        print("YOU WIN")
        print("Total de lanzamientos", suma)
        os.system("pause")
        break     
    if lives==0:
        print("GAMER OVER")
        print("Total de lanzamientos", suma)
    break