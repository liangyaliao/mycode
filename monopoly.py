#!/usr/bin/env python3

import random
spaces = ["go", "collect rent", "buy stock", "sell stock", "parking", "buy bitcoin", "collect interest", "pay income tax"]
current = 0
dice = 0
rolls = 0

print("Welcom to the Python Monopoly board! ")
roll_em = input("Press Enter to roll the dice, press q to end: ")

while (roll_em.lower() != "q"):
    dice = random.randint(1,6)
    rolls += 1
    current = (current + dice) % 8
    mySpace = spaces[current]
    print('\nYou rolled a {0}. You\'re at "{1}.'.format(dice, mySpace.upper()))
    roll_em = input("Press Enter to roll the dice again (Press q to end): ")

print("\nThanks for playing...you rolled",rolls,"times.\n")


