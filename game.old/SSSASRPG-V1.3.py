#SSSASRPG-V1.3
#=====IMPORTS=====
import os
import random
import time
import argparse
import msvcrt
os.system('cls')
#=====ARGUMENTS=====
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

# Example usage
if skip:
    skip = True
if spawn_dead:
    faststart = True
if admin_mode:
    print("Initializing with Admin Mode enabled...")
if debug:
    print("Initializing with Debug Mode enabled...")
#=====CHARACTER INFO=====
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
#=====Libraries=====
ORST = {
    "HP": 160,
    "DMG": 25,
    "SPD": 15

}
GOST = {
    "HP": 100,
    "DMG": 15,
    "SPD": 17   
}
#=====VARIABLES=====
goblinhp = 100
goblindamage = 10
lostmoney = level * 2
battle = False
items = [
    "Sword",
    "Sandwich",
    "VBucks Giftcard",
    "Sharko"
]
lore = {
    "Sword": "A great, shining blade, with a golden hilt that has rubies embedded to it, and an intricate floral design.",
    "Dagger": "A short blade. the words '<3 Ember' appear to be inscribed.",
    "Sharko": "Sharko? wtf are you doing in my game bro",
    "Sandwich": "Its uhh... its a sandwich. Theres some cheese on it. Think thats turkey?"
}
activesummons = [

]
summons = {
    "Sasha": "A great direwolf, standing at a staggering 5 feet tall and 200lbs.",
    "Imp": "A basic imp, with two horns and red skin."
}
equippeditems = [
    "Chestplate",
    "Boots",
    "Gauntlets",
    "Sword",
    "Helmet"
]
#=====FUNCTIONS=====
text_speed = 0.05  # default speed
def prints(text, delay=None):
    global text_speed
    if delay is None:  # use current speed if no override
        delay = text_speed
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
  ▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄▄       ▄▄      ▄▄▄▄▄     ▄▄▄▄▄▄     ▄▄▄▄▄▄    ▄   ▄▄▄▄ 
 ██▀▀▀▀█▄  ██▀▀▀▀█▄  ██▀▀▀▀█▄   ▄█▀▀█▄   ██▀▀▀▀█▄  █▀██▀▀▀█▄  █▀██▀▀▀█▄  ▀██████▀ 
 ▀██▄  ▄▀  ▀██▄  ▄▀  ▀██▄  ▄▀   ██  ██   ▀██▄  ▄▀    ██▄▄▄█▀    ██▄▄▄█▀    ██   ▄ 
   ▀██▄▄     ▀██▄▄     ▀██▄▄    ██▀▀██     ▀██▄▄     ██▀▀█▄     ██▀▀▀      ██  ██ 
 ▄   ▀██▄  ▄   ▀██▄  ▄   ▀██▄ ▄ ██  ██   ▄   ▀██▄  ▄ ██  ██   ▄ ██         ██  ██ 
 ▀██████▀  ▀██████▀  ▀██████▀ ▀██▀  ▀█▄█ ▀██████▀  ▀██▀  ▀██▀ ▀██▀         ▀█████ 
                                                                           ▄   ██ 
                                                                           ▀████▀ 

          
          
""")
def draw_menu_title():
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

#=====Sharko Stats
# SBHP = 1500
# SEHP = SBHP * level /2
# SBDMG = 200
# SEDMG = SBDMG + level *0.25
# abilities = [
#     "Domain Expansion",
#     "Slash",
#     "Dropkick",
# ]
# useability = random.randint(1,25)
# if useability in range(1,19):
#     ability = random.choice(abilities)
#     prints(f"Sharko used {ability}!")
# elif useability == 25:
#     prints(f"Sharko used DUKE ONOMONARESIA! it does {ephp}")
#     ephp -= ephp
# elif useability in range(20,24):
#     prints(f"Sharko used Jackpot!")
#     printss(f"Calculating...")
#     jackpot = random.randint(1,3)
#     if jackpot == 1:
#         JPD = ephp / 2
#         prints(f"Sharkos Jackpot! succeeded, you lose {JPD} HP!")
#     elif jackpot in range(2,3):
#         JPD = SEHP / 2
#         prints(f"Sharkos Jackpot! failed, Sharko loses {JPD} HP!")
#=====RANDOM NAME GENERATOR=====
def generate_event():
    first = ["Great", "Long", "Wild", "Wacky", "Mystical"]
    second = ["Evil", "Bloody", "Violent", "Fearsome"]
    third = ["War", "Clash", "Battle", "Crusade", "Genocide"]

    return f"{random.choice(first)} {random.choice(second)} {random.choice(third)}"

event = generate_event()
eventover = random.randint(1,1000)
if eventover == 1:
    event = "Sharkos Bum Ass Adventure"

#=====TITLE SCREEN=====
options = ["Start", "Options", "Bossrush"]
current = 0
draw_titleslow()
while True:
    os.system('cls')  # clear screen
    draw_menu_title()
    for i, option in enumerate(options):
        cursor = "->>" if i == current else " "
        print(f"{cursor} {option}")
    
    key = msvcrt.getch()
    if key == b'H':  # up arrow
        current = (current - 1) % len(options)
    elif key == b'P':  # down arrow
        current = (current + 1) % len(options)
    elif key == b'\r':  # enter
        selection = options[current]
        if selection == "Start":
            prints("Starting...")
            bossrush = False
            break
            
        if selection == "Options":
            suboptions = ["Text Speed", "Difficulty", "Close"]
            current = 0
            clear_screen()
            draw_title()
            while True:
                os.system('cls')  # clear screen
                draw_menu_title()
                for i, option in enumerate(suboptions):
                    cursor = "->>" if i == current else " "
                    print(f"{cursor} {option}")
                
                key = msvcrt.getch()
                if key == b'H':  # up arrow
                    current = (current - 1) % len(suboptions)
                elif key == b'P':  # down arrow
                    current = (current + 1) % len(suboptions)
                elif key == b'\r':  # enter
                    selection = suboptions[current]
                    if selection == "Close":
                        break
                    if selection == "Text Speed":
                        subsuboptions = ["Fast", "Medium", "Slow", "Close"]
                        current = 0
                        clear_screen()
                        draw_title()
                        while True:
                            os.system('cls')  # clear screen
                            draw_menu_title()
                            for i, option in enumerate(subsuboptions):
                                cursor = "->>" if i == current else " "
                                print(f"{cursor} {option}")
                            
                            key = msvcrt.getch()
                            if key == b'H':  # up arrow
                                current = (current - 1) % len(subsuboptions)
                            elif key == b'P':  # down arrow
                                current = (current + 1) % len(subsuboptions)
                            elif key == b'\r':  # enter
                                selection = subsuboptions[current]
                                if selection == "Close":
                                    break
                                if selection == "Fast":
                                    text_speed = 0.01
                                    prints("Text speed fast")
                                if selection == "Medium":
                                    text_speed = 0.05
                                    prints("Text speed medium")
                                if selection == "Slow":
                                    text_speed = 0.5
                                    prints("Text speed slow")

        if selection == "Bossrush":
            bossrush = True
            break
#===================


#=====BOOT TEST=====
if skip == False:
    os.system('cls')
    print("Alright, we will now begin testing to ensure everything runs ok.")
    time.sleep(0.25)
    prints("Testing slowed print...")
    printss("Testing super slowed print...")
    fprints("Testing fast print slowed...")
    time.sleep(0.25)
    prints("Testing completed! Welcome to Snickos Super Spectacular and Silly RPG! (SSSASRPG for short <3)")
    prints("beginning epilogue...")
#===================


#=====epilogue=====
    prints(f"You were born in the year 1205, 200 years after the {event}.")
    prints(f"You grew up in a small town, Etris.")
    prints(f"Your father was killed in the {event} when you were little.")
    prints(f"Since that day, you decided it was your duty, your RIGHT, to go out and avenge your father.")
    prints(f"And today you turn 16, meaning youre old enough to go out adventuring and fight for your own.")
    clear_screen()
    draw_title()
if faststart == False:
    prints("What is your name, my child?")
    name = input("My name is ")
    prints(f"What path do you choose, child?")
    path = input("1. i wish to be strong | 2. i wish to be alone in my training | 3. i wish to be infamous (1,2,3) ")
    if path == "1":
        path = "POS"
        prints("I shall guide you in your strength, child.")
    if path == "2":
        path = "LW"
        prints("So it is the path of the lone warrior, i see.")
    if path == 3:
        path = "INF"
        prints("This, i cannot help you with. You shall be on your own, child.")
    clear_screen()
    draw_title()
    time.sleep(0.5)
if faststart == True:
    name = "Snicko"
    path = "LW"
if skip == False:
    prints("You awaken in your bed. Birds can be heard in the trees, a beam of light shining through your window.")
    prints("You run downstairs, ecstatic - today is your 16th birthday.")
    prints("Reaching the bottom of the stairs, you run to your mother, who is preparing breakfast.")
    prints("You: 'Whats for breakfast, mom?'")
    prints("Mom: 'Roasted Skydasher and some wildberries, kiddo.'")
    prints("Your favorite meal. Roasted skydasher - a rather expensive meat. As the name suggests, it is an exceptionally fast avian creature.")
    prints("As such, it is very hard to catch one. However, due to its meat being so delicious, they are also endangered species.")
    prints("Upon finishing your breakfast, you dash out the door - but your mother calls out to you.")
    prints(f"Mom: {name}! You forgot your backpack and lunch!")
    prints("Upon hearing this, you turn around and walk back to your home.")
    prints("Mom: here you go kiddo.")
    prints("You obtained: Sandwich, Bag")
    time.sleep(1)
location = "Hometown"
while not bossrush:
    clear_screen()
    draw_title()
#===================


#=====SET STATS=====
    if admin_mode:
        str = int(1e200)
        hvy = int(1e200)
        med = int(1e200)
        lht = int(1e200)
    ephp = bphp + fortitude
    epdmg = bpdmg + hvy * 0.25 + str * 0.5
#=====IN CITY=====
    print(f"Location: {location}")
    print(f"HP: {ephp}")
    prints("What should you do?")
    action = input("Explore | View Bag | Shop | Train | Travel | ").lower()
    if action == "explore":
        clear_screen()
        if location == "Hometown":
            enemy = "Goblin"
            goblinhp = 100
            battle = True
#=====BATTLE LOGIC=====
            options = ["Attack", "Brace", "View Items", "Summon", "Flee"]
            current = 0
            playerturn = True
            draw_title()
            prints("You are face to face with a rabid, snarling goblin, wielding a long, sharp sword.")
            while battle:
                if playerturn:
                    options = ["Attack", "Brace", "View Items", "Summon", "Flee"]
                    os.system('cls')  # clear screen
                    draw_title()
                    print("You are face to face with a rabid, snarling goblin, wielding a long, sharp sword.")
                    for i, option in enumerate(options):
                        cursor = "->>" if i == current else " "
                        print(f"{cursor} {option}")
                    
                    key = msvcrt.getch()
                    if key == b'H':  # up arrow
                        current = (current - 1) % len(options) 
                    elif key == b'P':  # down arrow
                        current = (current + 1) % len(options)
                    elif key == b'\r':  # enter
                        selection = options[current]
                        if selection == "Attack":
                            suboptions = ["Slash", "Stab", "Counter"]
                            subcurrent = 0
                            clear_screen()
                            draw_title()
                            while True:
                                os.system('cls')  # clear screen
                                draw_title()
                                for i, option in enumerate(suboptions):
                                    cursor = "->>" if i == current else " "
                                    print(f"{cursor} {option}")
                                
                                key = msvcrt.getch()
                                if key == b'H':  # up arrow
                                    current = (current - 1) % len(suboptions)
                                elif key == b'P':  # down arrow
                                    current = (current + 1) % len(suboptions)
                                elif key == b'\r':  # enter
                                    selection = suboptions[current]
                                    if selection in ["Slash", "Stab", "Counter"]:
                                        atkdmg = random.randint(1, 10)  # adjust per attack
                                        esdmg = atkdmg + epdmg
                                        goblinhp -= esdmg
                                        prints(f"You used '{selection}', dealing {esdmg} damage! {enemy} has {goblinhp} remaining!")
                                        playerturn = False   # end player turn
                                        break  # exit submenu

                else:
                    prints(f"Goblin Attacks, dealing {goblindamage}! you have {ephp} hp left!")
                    playerturn = True






        # goblinturn = False
        # prints("A Wild Goblin Has Appeared! ")
        # while battle == True:
        #     clear_screen()
        #     draw_title()
        #     fprints(f"Goblin HP: {goblinhp}")
        #     fprints(f"Your HP: {ephp}")
        #     if goblinhp <= 0:
        #         prints("You have slain the goblin!")
        #         moneybefore = money
        #         money = moneywin(money)
        #         moneyafter = money
        #         gainedmoney = moneyafter - moneybefore
        #         xpbefore = exp
        #         exp = xpwin(exp)
        #         gainedxp = xpbefore - exp
        #         if exp >= 100 * level *0.25:
        #             print(f"Leveled up! You gained 3 stat points and are now level {level}!")
        #         battle = False
        #         prints(f"You earned {gainedmoney} dollars and")
        #         prints(f"{gainedxp} XP!")
        #         break
        #     if ephp <= 0:
        #         prints("You have been killed in combat...")
        #         prints(f"You lost {lostmoney}.")
        #         money -= lostmoney
        #         battle = False
        #         break
        #     playerturn = True
        #     if playerturn == True:
        #         action = input("Attack | Brace | View Items | Summon | Flee | ").lower()
        #         if action == "attack":
        #             prints("You swing your blade wildly!")
        #             goblinhp -= epdmg
        #             prints(f"Goblin has {goblinhp} HP left! ")
        #             if goblinhp > 0:
        #                 ept()
        #         if action == "view items":
        #             fprints(f"Items: {items}")
        #         if action == "uuddlrlrbastart":
        #             goblinhp -= goblinhp
        #     if goblinturn == True:
        #         ephp -= goblindamage
        #         prints(f"The goblin slashes forth, snarling wildly! It strikes you, dealing {goblindamage} damage! you have {ephp} HP left!")
#=====Training Logic=====
    if action == "train":
        training = True
        while training:
            keep = input("E to train and Q to stop!").lower()
            if keep == "e":
                exp += 1
                print(f"Level: {level} | Current EXP: {exp}")
                time.sleep(1)
            if keep == "q":
                break
#=====Bag Logic=====
    if action == "view bag":
        bagopen = True
        while bagopen:
            prints(f"Items in bag: {items}")
            prints(f"Equipped items: {equippeditems}")
            inspect_item = input("Which item? (back/exit to close) ").title()  # capitalizes first letter
            if inspect_item in ["Back", "Exit"]:
                break
            
            # Show lore
            prints(lore.get(inspect_item, "No lore available"))
            
            # Equip items not already equipped
            if inspect_item in items and inspect_item not in equippeditems:
                dowhat = input("Equip | Trash | Back | ").lower()
                if dowhat == "equip":
                    equippeditems.append(inspect_item)
                    items.remove(inspect_item)
                    prints(f"{inspect_item} equipped!")
                elif dowhat == "trash":
                    items.remove(inspect_item)
                    prints(f"{inspect_item} trashed.")
                elif dowhat == "back":
                    continue  # return to bag menu
            
            # Unequip items that are equipped
            elif inspect_item in equippeditems:
                dowhat = input("Unequip | Back | ").lower()
                if dowhat == "unequip":
                    items.append(inspect_item)
                    equippeditems.remove(inspect_item)
                    prints(f"{inspect_item} unequipped!")
                elif dowhat == "back":
                    continue  # return to bag menu
#=====Travel Logic=====
    if action == "travel":
        prints("Travel where? ")
        location = input("Castle | Dungeon | Marshwood")
        if location == "castle":
            prints("Upon arriving at the castle, you realize the Recommended level is 10. do you proceed?")
            proc = input("Y/N").lower()
            if proc == "y":
                location = "Castle"
                prints("you enter the castle.")






#=====BOSSRUSH LOGIC=====
while bossrush:
    print("mb gng dog ate the bosses")
    exit()