"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730481343"

from random import randint

print("Your fortune cookie says...")

randomNum: int = randint(1,4)

if randomNum < 3:  
    if randomNum == 1: 
        print("A foolish man listens to his heart. A wise man listens to cookies.")
    else: 
        print("To truly find yourself you should play hide and seek alone.")
else: 
    if randomNum == 3: 
        print("You are about to finish reading a fortune cookie.")
    else: 
        print("So live that you wouldn't be ashamed to sell the family parrot to the town gossip")

print("Now, go spread positive vibes!")