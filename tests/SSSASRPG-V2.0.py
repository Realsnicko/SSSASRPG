import os
import random
import time
import argparse
import msvcrt
import subprocess
import sys
os.system('cls')

skip = False
playdead = False
parser = argparse.ArgumentParser()
parser.add_argument('-S', '--skip-epilogue', action='store_true', help='Skip the epilogue')
parser.add_argument('-D', '--dead-on-spawn', action='store_true', help='Spawn dead, skips first fight')
parser.add_argument('-X', '--admin', action='store_true', help='Admin mode (bonus stats, spawn with Excalibur)')
parser.add_argument('-C', '--creator', action='store_true', help='Simple debug mode.' )
args = parser.parse_args()

skip = args.skip_epilogue
spawn_dead = args.dead_on_spawn
admin_mode = args.admin
debug = args.creator

if skip:
    skip = True
if spawn_dead:
    faststart = True
if admin_mode:
    print("Initializing with Admin Mode enabled...")
if debug:
    print("Initializing with Debug Mode enabled...")


#Player Stats========
name = "nil"
bphp = 125
bpdmg = 15
money = 500
level = 1
exp = 0
dexterity = 0
strength = 0
fortitude = 0
willpower = 0
precision = 0
ether = 0
heavywep = 0
mediumwep = 0
lightwep = 0
dex = dexterity
str = strength
fort = fortitude
wil = willpower
pr = precision
eth = ether
hvy = heavywep
med = mediumwep
lht = lightwep
ephp = bphp + fortitude
epdmg = bpdmg + hvy * 0.25 + str * 0.5
#=======================================
if debug:
    med = 15
    hvy = 15
    lht = 15
    str = 15
#=======================================
goblinhp = 100
goblindamage = 10
lostmoney = level * 2
battle = False
text_speed = 0.05

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def prints(text, delay=None, vertical=False):
    global text_speed
    if delay is None:
        delay = text_speed

    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]


    if vertical:


        buffer = [' ' * max_len for _ in lines]
        for col in range(max_len):
            for row in range(len(lines)):
                buffer[row] = buffer[row][:col] + lines[row][col] + buffer[row][col+1:]


            if col > 0:
                sys.stdout.write(f"\033[{len(lines)}A")
            

            for row in buffer:
                print(row)
            sys.stdout.flush()
            time.sleep(delay)


    else:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
wascii = (r"""
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
ascii = (r"""
  ▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄▄       ▄▄      ▄▄▄▄▄     ▄▄▄▄▄▄     ▄▄▄▄▄▄    ▄   ▄▄▄▄ 
 ██▀▀▀▀█▄  ██▀▀▀▀█▄  ██▀▀▀▀█▄   ▄█▀▀█▄   ██▀▀▀▀█▄  █▀██▀▀▀█▄  █▀██▀▀▀█▄  ▀██████▀ 
 ▀██▄  ▄▀  ▀██▄  ▄▀  ▀██▄  ▄▀   ██  ██   ▀██▄  ▄▀    ██▄▄▄█▀    ██▄▄▄█▀    ██   ▄ 
   ▀██▄▄     ▀██▄▄     ▀██▄▄    ██▀▀██     ▀██▄▄     ██▀▀█▄     ██▀▀▀      ██  ██ 
 ▄   ▀██▄  ▄   ▀██▄  ▄   ▀██▄ ▄ ██  ██   ▄   ▀██▄  ▄ ██  ██   ▄ ██         ██  ██ 
 ▀██████▀  ▀██████▀  ▀██████▀ ▀██▀  ▀█▄█ ▀██████▀  ▀██▀  ▀██▀ ▀██▀         ▀█████ 
                                                                           ▄   ██ 
                                                                           ▀████▀ 
         """)
prints(wascii, vertical=True)

options = ["Start", "Options", "Bossrush"]
current = 0
while True:
    cls()
    print(ascii)