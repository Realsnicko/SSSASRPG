import random
import os
import sys
moves = [
    "Slash",
    "Stab",
    "Fireball",
    "Doom"
]
moveodd = random.randint(1,10)
move = random.choice(moves)
if moveodd in (1,3):
    move = "Slash"
if moveodd in (4,7):
    move = "Stab"
if moveodd in (8,9):
    move = "Fireball"
if moveodd == 10:
    move = "Doom"
print(f"Sharko used {move}")
print(f"{moveodd}")