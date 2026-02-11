import time
import os
import subprocess
import argparse
import platform
import json
slots = "nil"
load = True
choosingslot = True
curslot = 0
pslot = "0"
noskip = True
parse = True
def cls():
    os.system('cls')
def save():
    try:
        print("Saving...")
        with open("Slots.json", "w") as f:
            json.dump(slots, f, indent=4)
        print("Successfully Saved!")
    except OSError as e:
        print("Save failed:", e)
    time.sleep(0.5)
    cls()
parser = argparse.ArgumentParser()
parser.add_argument('-S', '--skip-epilogue', action='store_true', help='Skip the epilogue')
parser.add_argument('-D', '--dead-on-spawn', action='store_true', help='Spawn dead, skips first fight')
parser.add_argument('-X', '--admin', action='store_true', help='Admin mode (bonus stats, spawn with Excalibur)')
parser.add_argument('-C', '--creator', action='store_true', help='Simple debug mode.' )
parser.add_argument('-FTS', '--FastText', action='store_true', help='Faster Text Speed.') 
parser.add_argument('-STS', '--SlowText', action='store_true', help='Slower Text Speed.') 
args = parser.parse_args()

skip = args.skip_epilogue
spawn_dead = args.dead_on_spawn
admin_mode = args.admin
debug = args.creator
FTS = args.FastText
STS = args.SlowText
# Example usage
if skip:
    print("Btw this doesnt do anything...")
if spawn_dead:
    print("Btw this doesnt do anything...")
if admin_mode:
    print("Initializing with Admin Mode enabled...")
if debug:
    print("Initializing with Debug Mode enabled...")

import data

def cls():
    OS = platform.system()
    if OS == "Windows":
        os.system('cls')
    else: 
        os.system('clear')
terminascii = r"""
  _________ _________ _________   _____    _____________________________  ________    
 /   _____//   _____//   _____/  /  _  \  /   _____/\______   \______   \/  _____/    
 \_____  \ \_____  \ \_____  \  /  /_\  \ \_____  \  |       _/|     ___/   \  ___    
 /        \/        \/        \/    |    \/        \ |    |   \|    |   \    \_\  \   
/_______  /_______  /_______  /\____|__  /_______  / |____|_  /|____|    \______  /   
        \/        \/        \/         \/        \/         \/                  \/    
  __                       .__              .__              __          .__          
_/  |_  ___________  _____ |__| ____ _____  |  |     _______/  |_ ___.__.|  |   ____  
\   __\/ __ \_  __ \/     \|  |/    \\__  \ |  |    /  ___/\   __<   |  ||  | _/ __ \ 
 |  | \  ___/|  | \/  Y Y  \  |   |  \/ __ \|  |__  \___ \  |  |  \___  ||  |_\  ___/ 
 |__|  \___  >__|  |__|_|  /__|___|  (____  /____/ /____  > |__|  / ____||____/\___  >
           \/            \/        \/     \/            \/        \/               \/ 
"""
normascii = r"""
  _________ _________ _________   _____    _____________________________  ________    
 /   _____//   _____//   _____/  /  _  \  /   _____/\______   \______   \/  _____/    
 \_____  \ \_____  \ \_____  \  /  /_\  \ \_____  \  |       _/|     ___/   \  ___    
 /        \/        \/        \/    |    \/        \ |    |   \|    |   \    \_\  \   
/_______  /_______  /_______  /\____|__  /_______  / |____|_  /|____|    \______  /   
        \/        \/        \/         \/        \/         \/                  \/    
"""
# ===== BOOT INTRO =====
cls()
data.prints("Woah bro! I didn't know we were starting today! Oh s**t...")
time.sleep(1)
data.prints("Hold up... let me...")
time.sleep(0.25)
print("F**K-")
time.sleep(0.5)
print("S**T-")
time.sleep(0.3)
data.prints("oh hell what is... where'd I put...")
time.sleep(0.4)
data.prints("oh, s**t, there it is. Loading the Kernel")
time.sleep(0.3)

for _ in range(2):
    data.prints(".")
    time.sleep(0.15)
    data.prints("..")
    time.sleep(0.15)
    data.prints("...")
    time.sleep(0.15)

cls()

# ===== REAL BOOT SEQUENCE =====
data.prints("[BOOT SEQUENCE INITIALIZED]")
time.sleep(0.5)
data.prints("[LOADING KERNEL MODULES...]")
time.sleep(0.5)
data.prints("[SYSTEM ONLINE]")
time.sleep(0.5)
state = "main_menu"

while True:
    if state == "main_menu":
        data.prints("Welcome to:")
        print(terminascii)
        print("Load | New | Settings | Community")
        action = input("").lower()

        if action == "load":
            print("almost in the game.")
            # while load:
            #     if os.path.exists("Slots.json"):
            #         print("Save file found! Loading...")
            #         try:
            #             with open("Slots.json", "r") as f:
            #                 slots = json.load(f)
            #                 print("Loaded successfully!")
            #                 time.sleep(1)
            #                 break
            #         except json.JSONDecodeError:
            #             print("Save file corrupted! Starting fresh...")
            #             slots = {}  # fallback, or reinitialize slots dict
            #             time.sleep(1)
            #             break
            #     else:
            #     # default slots
            #         slots = {
            #         "slot1": {"Name": "nil", "hp": 250, "maxhp": 250, "atk": 15, "spd": 12,
            #                 "money": 0, "level": 1, "XP": 0, "slot": "slot1"},
            #         "slot2": {"Name": "nil", "hp": 250, "maxhp": 250, "atk": 15, "spd": 12,
            #                 "money": 0, "level": 1, "XP": 0, "slot": "slot2"},
            #         "slot3": {"Name": "nil", "hp": 250, "maxhp": 250, "atk": 15, "spd": 12,
            #                 "money": 0, "level": 1, "XP": 0, "slot": "slot3", "stats": {"dex": 0, "pre": 0, "fort": 0, "stre": 0}}
            #     }
            #         break
            # while choosingslot and pslot == "0":
            #     cls()
            #     print("Which slot will you load?")
            #     print("Slot stats:")

            #     for i in range(1, 4):
            #         slot = slots[f"slot{i}"]
            #         print(f"Slot{i}")
            #         print(f"    NAME: {slot['Name']}")
            #         print(f"    HP: {slot['hp']}")
            #         print(f"    ATK: {slot['atk']}")
            #         print(f"    SPD: {slot['spd']}\n")

            #     print("1/2/3")
            #     pslot = input()
            #     key = f"slot{pslot}"
            #     if key in slots:
            #         curslot = slots[key]
            #         print(f"Selected slot: {curslot['slot']}")
            #     else:
            #         print("That's not a valid slot dumbass")
            #         pslot = "0"
            #         time.sleep(0.25)
            # if curslot["Name"] == "nil":
            #     curslot["Name"] = input("What is your name?")
            #     save()
            # else:
            #     print(f"Welcome back, {curslot['Name']}!")

        elif action == "new":
            subprocess.run(["python", "Game.py", "--speed", str(data.text_speed)])

        elif action == "settings":
            state = "settings_menu"

        else:
            print("Invalid option.")

    elif state == "settings_menu":
        print("settings... s**t i forgot to... hold on")
        print("Compiling settings...")
        print("Text Speed")
        action = input("").lower()

        if action == "text speed":
            print("Slow | Med | Fast")
            action = input("").lower()

            if action == "slow":
                data.text_speed = 0.3
                print("selected slow speed.")
                cls()
                state = "main_menu"

            elif action == "med":
                data.text_speed = 0.05
                print("selected medium speed.")
                cls()
                state = "main_menu"

            elif action == "fast":
                data.text_speed = 0.015
                print("selected fast speed.")
                cls()
                state = "main_menu"

            else:
                print("Invalid option.")

        else:
            print("Invalid option.")




#Slot Loading
while load:
    if os.path.exists("Slots.json"):
        print("Save file found! Loading...")
        try:
            with open("Slots.json", "r") as f:
                slots = json.load(f)
                print("Loaded successfully!")
                time.sleep(1)
                break
        except json.JSONDecodeError:
            print("Save file corrupted! Starting fresh...")
            slots = {}  # fallback, or reinitialize slots dict
            time.sleep(1)
            break
    else:
    # default slots
        slots = {
        "slot1": {"Name": "nil", "hp": 250, "maxhp": 250, "atk": 15, "spd": 12,
                  "money": 0, "level": 1, "XP": 0, "slot": "slot1"},
        "slot2": {"Name": "nil", "hp": 250, "maxhp": 250, "atk": 15, "spd": 12,
                  "money": 0, "level": 1, "XP": 0, "slot": "slot2"},
        "slot3": {"Name": "nil", "hp": 250, "maxhp": 250, "atk": 15, "spd": 12,
                  "money": 0, "level": 1, "XP": 0, "slot": "slot3", "stats": {"dex": 0, "pre": 0, "fort": 0, "stre": 0}}
    }
        break
while choosingslot and pslot == "0":
    cls()
    print("Which slot will you load?")
    print("Slot stats:")

    for i in range(1, 4):
        slot = slots[f"slot{i}"]
        print(f"Slot{i}")
        print(f"    NAME: {slot['Name']}")
        print(f"    HP: {slot['hp']}")
        print(f"    ATK: {slot['atk']}")
        print(f"    SPD: {slot['spd']}\n")

    print("1/2/3")
    pslot = input()
    key = f"slot{pslot}"
    if key in slots:
        curslot = slots[key]
        print(f"Selected slot: {curslot['slot']}")
    else:
        print("That's not a valid slot dumbass")
        pslot = "0"
        time.sleep(0.25)
if curslot["Name"] == "nil":
    curslot["Name"] = input("What is your name?")
    save()
else:
    print(f"Welcome back, {curslot['Name']}!")