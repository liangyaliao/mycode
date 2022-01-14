#!/usr/bin/env python3
  
import random
spaces = [{"name": "go", "income": 0},
          {"name": "collect rent", "income": 200},
          {"name": "buy stock", "income": -10},
          {"name": "sell stock", "income": 400},
          {"name": "parking fee", "income": -20},
          {"name": "buy bitcoin", "income": -30},
          {"name": "collect interest", "income": 400},
          {"name": "pay income tax", "income": -100},]
current1 = 0
current2 = 0
dice1 = 0
dice2 = 0
rolls1 = 0
rolls2 = 0
p1money= 100
p2money= 100

print("Welcom to the Python Monopoly board! ")
roll_em = input("Press Enter to roll the dice, press q to end: ")


while (roll_em.lower() != "q"):
    if p1money < 1000:
        dice1 = random.randint(1,6)
        rolls1 += 1
        current1 = (current1 + dice1) % 8
        mySpace1 = spaces[current1]
        p1money += mySpace1["income"]        
        print('\np1, you just rolled a {0}. You\'re at "{1}" position.You currently have ${2}.'.format(dice1, mySpace1["name"].upper(), p1money))
        roll_em = input("Press Enter to roll the dice again (Press q to end): ")
        print("\np1. Thanks for playing...you rolled",rolls1,"times.\n")
        

    elif p2money < 1000:
    
        dice2 = random.randint(1,6)
        rolls2 += 1
        current2 = (current2 + dice2) % 8
        mySpace2 = spaces[current2]
        p2money += mySpace2["income"]
        print('\np2, you just rolled a {0}. You\'re at "{1}" position.You currently have ${2}.'.format(dice2, mySpace2["name"].upper(), p2money))
        roll_em = input("Press Enter to roll the dice again (Press q to end): ")
        print("\np2.Thanks for playing...you rolled",rolls2,"times.\n")
        

    else:
        break
   
    
if rolls1 < rolls2:
    print("p1 won!")
else:
    print("p2 won!")
