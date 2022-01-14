#!/usr/bin/env python3

import random
spaces = [{"name": "go", "income": 100},
          {"name": "collect rent", "income": 200}, 
          {"name": "buy stock", "income": 300},
          {"name": "sell stock", "income": 400}, 
          {"name": "parking", "income": 500}, 
          {"name": "buy bitcoin", "income": 600}, 
          {"name": "collect interest", "income": 700}, 
          {"name": "pay income tax", "income": 800},]
current = 0
dice = 0
rolls = 0
p1money= 0
p2money= 0

print("Welcom to the Python Monopoly board! ")
roll_em = input("Press Enter to roll the dice, press q to end: ")

while (roll_em.lower() != "q") and p1money < 1000 and p2money < 1000:
    print(f"You currently have ${p1money}.")
    dice = random.randint(1,6)
    rolls += 1
    current = (current + dice) % 8
    mySpace = spaces[current]
    print('\nYou rolled a {0}. You\'re at "{1}.'.format(dice, mySpace["name"].upper()))
    p1money += mySpace["income"]
    roll_em = input("Press Enter to roll the dice again (Press q to end): ")

print("\nThanks for playing...you rolled",rolls,"times.\n")


