import random
import time
import os
import shutil
import platform
import argparse
from data import death, cls, prints
player = {
    "name": "Player",
    "hp": 100,
    "max_hp": 100,
    "level": 1,
    "exp": 0,
    "gold": 0
}
party = []
goliathname = False
parser = argparse.ArgumentParser()
parser.add_argument('-S', '--skip-epilogue', action='store_true', help='Skip the epilogue')
parser.add_argument('-D', '--dead-on-spawn', action='store_true', help='Spawn dead, skips first fight')
parser.add_argument('-X', '--admin', action='store_true', help='Admin mode (bonus stats, spawn with Excalibur)')
parser.add_argument('-C', '--creator', action='store_true', help='Simple debug mode.' )
parser.add_argument('-FTS', '--FastText', action='store_true', help='Faster Text Speed.') 
parser.add_argument('-STS', '--SlowText', action='store_true', help='Slower Text Speed.')
parser.add_argument("--speed", type=float)
args = parser.parse_args()
import data
data.text_speed = args.speed
skip = args.skip_epilogue
spawn_dead = args.dead_on_spawn
admin_mode = args.admin
debug = args.creator
FTS = args.FastText
STS = args.SlowText
if skip:
    print("Btw this doesnt do anything...")
if spawn_dead:
    print("Btw this doesnt do anything...")
if admin_mode:
    print("Initializing with Admin Mode enabled...")
if debug:
    print("Initializing with Debug Mode enabled...")

#===============
#==ACTUAL GAME==
#===============

cls()
prints("You are inside of a tavern.")
time.sleep(1)
prints("The clinking of glasses fills the air, drunken laughter audible from across the bar.")
time.sleep(1)
prints("As you enter, you feel eyes immediately land on you. The hair on the back of your neck stands up.")
time.sleep(1)
prints("You glance around. Your heart starts racing. Something feels off.")
time.sleep(1)
prints("You decide to ignore it for the time being. You approach the bartender.")
time.sleep(1)
prints("Bartender: 'Huh. New face. Dont see many new people. Not anymore at least.")
time.sleep(1)
prints("Bartender: 'So, whatcha need?'")
time.sleep(1)
Bartendialogue = True
while Bartendialogue:
    print("")
    print("")
    print("1) 'Got any work that needs doing?' | 2) 'What do you mean, 'anymore'?'  | 3) 'What do yall have to drink 'round here?' | 4) end dialogue.")
    print("(You can use 1-3 for dialogue choices.)")
    dialogue = input("")
    print("")
    print("")
    if dialogue == "1":
        prints("Bartender: 'Heh, boy do we have work for you. Grab a-")
        time.sleep(1)
        prints("Bartender: 'Oh. You meant like mercenary work.")
        time.sleep(1)
        prints("The bartender sighs.")
        time.sleep(1)
        prints("Bartender: 'Yeah, we have that to. Theres this group of bandits been bothering us. Theyre based out in a cave towards the south of here.")
        time.sleep(1)
        prints("Bartender: 'Here. Ill mark it for you. Go clear that out and ill pay you well. Anything else you need?")
        caveopen = True
        time.sleep(3)
    if dialogue == "2":
        prints("Everyone suddenly goes quiet.")
        time.sleep(1)
        prints("The bartender looks at you. The look on his face tells you that you likely werent supposed to ask that question. Perhaps the game dev forgot to implement lore here...")
        time.sleep(3)
    if dialogue == "3":
        prints("Bartender: 'Water.'")
        time.sleep(1)
        prints("Bartender: 'Thats it.'")
        time.sleep(3)
    if dialogue == "4":
        Bartendialogue = False
        gameloop = True
        cls()
while gameloop:
    state = "towncenter"
    while state == "towncenter":
        cls()
        prints("You are in the middle of a small town. The houses made of brick and wood, a small fountain in the center. down the road is a forest.")
        prints("You hear the sound of children laughing, the bustling of the marketplace up the road, the church bells ringing. It is now 12pm.")
        print("1) Explore | 2) Bag | 3) Travel | 4) Speak with the people")

        action = input("").lower()
        print("")
        print("")
        if action == "explore" or action == "1":
            state = "battle"
            turn = "player"
            prints("A wild goblin appears. or... wait is that an orc..? how do you tell... fuck it thats a creature.")
            print("(lmao i have to put this just because, the one with more HP is an orc.)")
            E1 = random.choice(["goblin","orc"])
            if E1 == "goblin":
                E1HP = 100
            elif E1 == "orc":
                E1HP = 150
            while state == "battle":
                cls()
                if player['hp'] <= 0:
                    death()
                print(f"Creature: {E1HP}")
                print(f"Player: {player['hp']}")
                if turn == "player":
                    print("1) Attack | 2) flee")
                    action = input("").lower()
                    if action == "attack" or action == "1":
                        E1HP -= 25
                        prints("You attack the creature, dealing 25 damage!")
                        turn = "E1HP"
                        time.sleep(1)
                    if action == "flee" or action == "2":
                        prints("You flee from the fight. Coward...")
                        state = "towncenter"
                elif turn == "E1HP":
                    if E1HP <= 0:
                        prints("You defeated the creature!")
                        time.sleep(1)
                        state = "towncenter"
                    else:
                        player['hp'] -= 25
                        prints("The creature attacks you!")
                        turn = "player"
                        time.sleep(1)



        if action == "bag" or action == "2":
            print("LMAO ur geeked if you think im implementinng the bag this early ts just the prototype")
        

        if action == "Travel" or action == "3":
            print("Where to tho?")
            print("1) Ravenshire | 2) Southmarch")
            print("(Tip: You can use 1/2 to select the cities rather than typing the names!)")
            location = input("").lower()
            if location == "1" or location == "ravenshire":
                print("Goon!")
            if location == "2" or location == "Southmarch":
                print("Goon again! (but now 2!)")


        if action == "speak with people" or action == "4":
            state = "talking"
            while state == "talking":
                cls()
                prints("You enter the marketplace. You see several people, but 4 stick out to you.")
                prints("One gorgeous elf woman, who exudes a powerful aura.")
                prints("One tall man, who appears extremely strong, as if he could lift the world with a finger.")
                prints("A small dwarven man, carrying a sword on his waist.")
                prints("A cat, with a black and grey coat. Adorable.")
                print("Who do you speak to?")
                print("1) Elf girl | 2) Tall man | 3) Dwarf | 4) Cat | 5) Shark Man | 6) Back")
                speech = input("").lower()
                if speech == "cat" or speech == "4":
                    print("You approach the cat.")
                    time.sleep(1)
                    prints("Cat: 'meow.'")
                    time.sleep(1)
                    print("You pet the cat.")
                    time.sleep(1)
                    print("The cat climbs onto your shoulder.")
                    time.sleep(0.5)
                    prints("Cat: 'Yo whats good twin.'")
                    time.sleep(1)
                    print("Oh. Yeah. The cat talks. Like uhh... whats the cat from persona again? I forgot. Like Meowth ig.")
                    time.sleep(3)
                    print("Cat has joined your party!")
                    party.append("Cat")
                    time.sleep(3)


                if speech == "back" or speech == "6":
                    state = "towncenter"
                if speech == "elf girl" or speech == "elf" or speech == "1":
                    cls()
                    prints("You approach the elf girl.")
                    time.sleep(1)
                    prints("As you step close, before you even greet her, in a blink of an eye she does a full 180, facing you. She then leans in, inches from you.")
                    time.sleep(0.5)
                    prints("Elf girl: 'Hello. Do you need something?'")
                    time.sleep(1)
                    prints("The aura around this girl feels heavy. She is very clearly powerful. Be careful in what you say.")
                    time.sleep(0.5)
                    print("")
                    print("")
                    print("1) 'H-hello, I wish to ask about the area...' | 2) 'Hey, I wish to ask if you would like to join my team..?' | 3) 'S-so... are you... strong?' | 4) back")
                    print("(Tip: only press the number corresponding to the dialogue choice you wish!)")
                    dialogue = input("")
                    print("")
                    print("")
                    if dialogue == "1":
                        prints("Elf girl: 'Is that so... well, this area is of course called 'Timbercross', however if youre here id presume youre already aware of that...'")
                        prints("Elf girl: 'We dont very often get newcomers here... so why are you here? Though you dont have to answer that of course...'")
                        print("1) 'So, what is the whole 'we dont get newcomers' thing about?' | 2) back")
                        dialogue = input("")
                        print("")
                        print("")
                        if dialogue == "1":
                            prints("The elf girl turns to you, and in a swift move raises her hand. Suddenly your vision goes black. In your final moments you hear her speak.")
                            time.sleep(1)
                            prints("Elf girl: 'So disrespectful... why would you ask such a question.'")
                            time.sleep(3)
                            death()
                            state = "nil"
                        if dialogue == "back" or dialogue == "2":
                            prints("You awkwardly back away from the elf girl, and return to the marketplace.")
                            time.sleep(1)
                    if dialogue == "2":
                        prints("Elf girl: 'I would rather die than join a party with someone as weak as you, you are beneath me in every criteria. Leave my presence before i remove your head from your shoulders.'")
                        time.sleep(3)
                    if dialogue == "3":
                        prints("Elf girl: 'I am very strong. I am the strongest in this town. Strong enough to end you before youre even aware that youve been slain..'")
                        time.sleep(1)
                        prints("Elf girl: 'however...'")
                        time.sleep(1)
                        prints("She looks you up and down, noticing something about you.")
                        time.sleep(1)
                        prints("Elf girl: 'Judging by the look on your face... seems that you can already tell how powerful i am. Now leave my presence.'")
                        time.sleep(3)
                    if dialogue == "back" or dialogue == "4":
                        prints("You awkwardly back away from the elf girl, and return to the marketplace.")
                        state = "talking"


                if speech == "shark man" or speech == "5":
                    state = "Sharkman"
                    while state == "Sharkman":
                        cls()
                        print("")
                        print("")
                        prints("You approach the shark man.")
                        time.sleep(1)
                        prints("The shark man is playing with the children. The laughter grows louder as you approach.")
                        time.sleep(1)
                        prints("The shark man produces a cold aura, like snow, or ice.")
                        time.sleep(1)
                        prints("The shark man is carrying a large axe, with frost coming off of it. There are engravings in the side of a language you dont understand.")
                        time.sleep(1)
                        prints("As you approach, the shark man looks over his shoulder, spotting you. He then turns around.")
                        time.sleep(1)
                        prints("Shark man: 'Hey there! Names Sharko. You new here?'")
                        print("")
                        print("")
                        print("1) 'Woah, nice axe dude!' | 2) 'Nice to meet you, Sharko!' | 3) 'Wanna join my party?' | 4) 'Hey, what can you tell me about the town?' 5) back")
                        dialogue = input("")
                        if dialogue == "1":
                            state = "SMSD1"
                            while state == "SMSD1":
                                prints("Shark man: 'Thanks! Its imbued with a spirit, its name is Sudaruska!'")
                                time.sleep(1)
                                prints("Shark man: 'In order to wield it you have to learn Frostdraw though, which is kind of tough to learn. You know any magic yet?'")
                                time.sleep(1)
                                print("")
                                print("")
                                print("1) 'Frostdraw..?' | 2) 'Magic? Can I learn that too?' | 3) back")
                                sdialogue = input("")
                                if sdialogue == "1":
                                    prints("Shark man: 'Yeah, Frostdraw is a type of magic- well, thats what it was called in my hometown. The official name is IceBreathe.'")
                                    time.sleep(1)
                                    continue
                                if sdialogue == "2":
                                    prints("Shark man: 'Of course you can! I can teach you, but when youre a bit stronger.'")
                                if sdialogue == "back" or sdialogue == "3":
                                    state = "Sharkman"
                        if dialogue == "2":
                            prints("Sharko: 'Nice to meet you too, friend! I dont get many new people around here, its nice to have someone new to talk to!'")
                            time.sleep(1)
                            prints("Sharko: 'Ive been here for a while, but I dont get out much. I mostly just hang around the Tavern and the marketplace.'")
                            time.sleep(3)
                        if dialogue == "3":
                            prints("Sharko: 'Hmm... well, perhaps if you can answer one question.")
                            time.sleep(1)
                            prints("Sharko: 'Who would win in a fight.  Fully adapted mahoraga, or a refrigerator?'")
                            print("")
                            print("")
                            print("1) 'Fully adapted mahoraga' | 2) 'Refrigerator' | 3) 'Uh... whats a mahoraga?' | 4) 'erm... nevermind.'")
                            state = "SMSD2"
                            while state == "SMSD2":
                                dialogue = input("")
                                if dialogue == "1" or dialogue == "fully adapted mahoraga":
                                    prints("Sharko: 'WRONG! See, a refrigerator beats mahoraga because its already fully adapted to mahoraga. Duh.'")
                                    time.sleep(1)
                                    prints("Sharko: 'You gotta think outside the box, my guy.'")
                                    time.sleep(3)
                                if dialogue == "2" or dialogue == "refrigerator":
                                    prints("Sharko: 'Correct! You seem pretty smart, maybe ill join your party after all... wait a damn minute. Youre such a low level, what the fuck? Im NOT joining yo shi get yo levels up, tf?'")
                                    time.sleep(3)
                                if dialogue == "3" or dialogue == "uh... whats a mahoraga?":
                                    prints("Sharko: 'Ohhh.. you wanna see mahoraga, huh?'")
                                    time.sleep(1)
                                    prints("Sharko: 'With this treasure, i summon...'")
                                    time.sleep(1)
                                    prints("Sharko: 'Eight gripped sword...'")
                                    time.sleep(1)
                                    prints("Sharko: 'Divergent sila...'")
                                    time.sleep(1)
                                    prints("Sharko: 'Divine general...'")
                                    time.sleep(1)
                                    prints("Sharko: 'MAHORAGA.'")
                                    time.sleep(1)
                                    prints("Mahoraga appears, slamming Sharko into a wall. It rears its head to look at you, before the wheel above its head turns once, twice, and then it charges.")
                                    state = "MahoragaFight"
                                    MobbergabaHP = 10000
                                    while state == "MahoragaFight":
                                        if turn == "player":
                                            print(f"Mahoraga: {MobbergabaHP}")
                                            print(f"Player: {player['hp']} HP")
                                            print("1) Attack | 2) flee")
                                            action = input("")
                                            if action == "attack" or action == "1":
                                                MobbergabaHP -= 25
                                                prints("You attack Mahoraga, dealing 100 damage!")
                                                time.sleep(1)
                                            if action == "flee" or action == "2":
                                                prints("You tried to get awa- no, nevermind. mahoraga grabs you by the back of your skull, crushing it instantly.")
                                                death()
                                        elif turn == "Mahoraga":
                                            player['hp'] -= 100
                                            prints("Mahoraga attacks you, dealing 1000 damage!")
                                            time.sleep(1)
                                            if player['hp'] <= 0:
                                                death()
                                if dialogue == "4" or dialogue == "erm... nevermind.":
                                    print("Sharko: 'Heh, yeah maybe that was a bit too much for you. Get some more levels and then we can talk about me joining your party.'")
                                    time.sleep(3)
                        if dialogue == "4":
                            print("Sharko: 'Well, this town is called Timbercross. Its a nice little town, not much happens here though. We have a tavern, a marketplace, and a church. Thats about it.'")
                            time.sleep(3)
                        if dialogue == "5" or dialogue == "back":
                            state = "talking"
                if speech == "tall man" or speech == "2":
                    state = "tallman"
                    while state == "tallman":
                        cls()
                        if goliathname == True:
                            tallman = "Goliath"
                        else: tallman = "Tall Man"
                        print("You approach the tall man.")
                        time.sleep(1)
                        print(f"{tallman}: 'Hey there, you new here?'")
                        time.sleep(1)
                        print("You notice the tall man has a very deep voice, and a very strong presence. You can feel the power radiating off of him.")
                        time.sleep(1)
                        print("1) 'Hey, nice to meet you!' | 2) 'What can you tell me about the town?' | 3) 'Wanna join my party?' | 4) back")
                        dialogue = input("")
                        print("")
                        print("")
                        if dialogue == "1":
                            print(f"{tallman}: 'Nice to meet you too, friend. My name is Goliath.'")
                            goliathname = True
                            tallman = "Goliath"
                            time.sleep(1)
                            print(f"{tallman}: 'Im the local bodybuilder and boxer. I protect the town from those creatures that live in the forest.'")
                            time.sleep(1)
                            print(f"{tallman}: 'Ive been here for a while, but I dont get out much. I mostly just work out and hang around the Tavern.'")
                            continue
                        if dialogue == "2":
                            print(f"{tallman}: 'Well, newcomers dont come around often. Were...'")
                            time.sleep(1)
                            print("The tall man looks around, almost anxiously, as if hes worried someone might overhear him.")
                            time.sleep(1)
                            print(f"{tallman}: 'Well, were... *ahem* were not supposed to talk about it. There was an incident a few years back.'")
                            time.sleep(1)
                            print(f"{tallman}: 'Ive... already spoken too much. I recommend not asking other people this question. Not everybody reacts quite the same way.'")
                            time.sleep(3)
                        if dialogue == "3":
                            print(f"{tallman}: 'Heh, well! I cant quite turn down such an offer... hell, why not, ive nothing to do here anymore!'")
                            time.sleep(1)
                            print("Tall man has joined your party!")
                            party.append("Goliath")
                        if  dialogue == "4" or dialogue == "back":
                            state = "talking"