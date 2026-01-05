#titlescreen test
import os
import random
import time
import argparse
import msvcrt
os.system('cls')
def prints(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def printss(text, delay=0.15):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def fprints(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def moneywin(money):
    money += random.randint(1,5)
    return money
def xpwin(exp):
    exp += random.randint(5,50)
    return exp
def ept():
    global playerturn, goblinturn
    playerturn = False
    goblinturn = True
def egt():
    global playerturn, goblinturn
    playerturn = True
    goblinturn = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_title():
    print(r"""
            

                    WELCOME TO:
            
  ▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄▄       ▄▄      ▄▄▄▄▄     ▄▄▄▄▄▄     ▄▄▄▄▄▄    ▄   ▄▄▄▄ 
 ██▀▀▀▀█▄  ██▀▀▀▀█▄  ██▀▀▀▀█▄   ▄█▀▀█▄   ██▀▀▀▀█▄  █▀██▀▀▀█▄  █▀██▀▀▀█▄  ▀██████▀ 
 ▀██▄  ▄▀  ▀██▄  ▄▀  ▀██▄  ▄▀   ██  ██   ▀██▄  ▄▀    ██▄▄▄█▀    ██▄▄▄█▀    ██   ▄ 
   ▀██▄▄     ▀██▄▄     ▀██▄▄    ██▀▀██     ▀██▄▄     ██▀▀█▄     ██▀▀▀      ██  ██ 
 ▄   ▀██▄  ▄   ▀██▄  ▄   ▀██▄ ▄ ██  ██   ▄   ▀██▄  ▄ ██  ██   ▄ ██         ██  ██ 
 ▀██████▀  ▀██████▀  ▀██████▀ ▀██▀  ▀█▄█ ▀██████▀  ▀██▀  ▀██▀ ▀██▀         ▀█████ 
                                                                           ▄   ██ 
                                                                           ▀████▀ 

          
          
""")
def draw_titleslow():
    fprints(r"""
            

                    WELCOME TO:
            
  ▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄▄       ▄▄      ▄▄▄▄▄     ▄▄▄▄▄▄     ▄▄▄▄▄▄    ▄   ▄▄▄▄ 
 ██▀▀▀▀█▄  ██▀▀▀▀█▄  ██▀▀▀▀█▄   ▄█▀▀█▄   ██▀▀▀▀█▄  █▀██▀▀▀█▄  █▀██▀▀▀█▄  ▀██████▀ 
 ▀██▄  ▄▀  ▀██▄  ▄▀  ▀██▄  ▄▀   ██  ██   ▀██▄  ▄▀    ██▄▄▄█▀    ██▄▄▄█▀    ██   ▄ 
   ▀██▄▄     ▀██▄▄     ▀██▄▄    ██▀▀██     ▀██▄▄     ██▀▀█▄     ██▀▀▀      ██  ██ 
 ▄   ▀██▄  ▄   ▀██▄  ▄   ▀██▄ ▄ ██  ██   ▄   ▀██▄  ▄ ██  ██   ▄ ██         ██  ██ 
 ▀██████▀  ▀██████▀  ▀██████▀ ▀██▀  ▀█▄█ ▀██████▀  ▀██▀  ▀██▀ ▀██▀         ▀█████ 
                                                                           ▄   ██ 
                                                                           ▀████▀ 

          
          
""")
options = ["Start", "Options", "Config"]
current = 0
draw_titleslow()
while True:
    os.system('cls')  # clear screen
    draw_title()
    for i, option in enumerate(options):
        cursor = "|" if i == current else " "
        print(f"{cursor} {option}")
    
    key = msvcrt.getch()
    if key == b'H':  # up arrow
        current = (current - 1) % len(options)
    elif key == b'P':  # down arrow
        current = (current + 1) % len(options)
    elif key == b'\r':  # enter
        selection = options[current]
        print(f"You selected: {selection}")
        break
