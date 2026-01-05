import os
import random
import time
import argparse
skip = False
playdead = False
parser = argparse.ArgumentParser()
parser.add_argument('-S', '--skip-epilogue', action='store_true', help='Skip the epilogue')
parser.add_argument('-K', '--dead-on-spawn', action='store_true', help='Spawn dead, skips first fight')
parser.add_argument('-X', '--admin', action='store_true', help='Admin mode (bonus stats, spawn with Excalibur)')
args = parser.parse_args()

skip = args.skip_epilogue
spawn_dead = args.dead_on_spawn
admin_mode = args.admin

# Example usage
if skip:
    skip = True
if spawn_dead:
    playdead = True
if admin_mode:
    print("Admin mode enabled...")

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
items = [
    "Sword"
    "Shield"
    "Staff"
    "HealthPotion"
    "Sandwich"
    "Cookie"
    "Boots"
]
playeritems = [
    "Amulet",
    "Sandwich",
    "Embers Dagger"
]
currentarmor = [
    "Iron helmet",
    "Iron boots",
    "Iron chestplate",
    "Iron greaves",
    "Iron gauntlets"
]
currentwep = [
    "Familiar Longsword"
]
spells = [
    "Big Magaraha"
]
summons = [
    "Sasha"
]
#playerstats
playerhealth = 100
playerdamage = 15
playerspeed = 10
#Goblin stats
goblinhp = 110
goblindamage = 10
goblinspeed = 5
#Embers Stats
emberhealth = 75
emberdamage = 5
#turnlogic
os.system('cls')
if skip == False:
    prints("The year is 1522. You are 22, a traveling bandit alongside your two comrades, Ash, a muscular black haired orc, and Ember, a short red haired elf. Youre in the middle of a forest, walking a trail as the sun sets. Ember is drunk, and Ash trying to annoy her.")
    prints("Ash: Ember look theres a goblin behind you!")
    prints("Ember: WHAT? WHERE!")
    prints("Ember draws her sword, then in her panic stumbles backwards into a pile of mud.")
    prints("Ash: HAHAHA THERES NO GOBLIN IDIOT!")
    prints("Ember, now beet red in the face with anger and embarrasment: You bastard, one of these days youll end up like the Boy who cried wolf!")
    prints("Ash: As if!")
    prints("You: Alright alright quiet down you two, god why should i have to babysit you like this youre grown adults... embarrasing.")
    prints("Ember: HE STARTED IT THOUGH!")
    prints("You: And i finished it, end of story.")
    prints("Ember: Yeah Ash, its done now!")
    prints("Ember sticks her tongue out at Ash, but mud spills onto it. You and Ash burst out laughing while she tries to spit it out.")
    prints("Ash: HAHAH- wait... did you guys hear that?")
    prints("Ember: Shutup im not falling for that aga-")
    prints("Ash: No really i actually heard so-")
    prints("Ember: I SAID SHUTUP! god are you dea-")
    prints("Before Ember can finish her sentence, a goblin jumps out from the trees, carrying a club made from bone and leather.")
    prints("You draw your sword, the familiar weight in your hands readying you for battle. it catches on the scabbard once or twice before emerging.")
    prints("Ember, who still hasnt gotten up, scrambles to her feet, falls again, then stands up, drops her bottle of Whiskey, and draws her dagger, an elven blade gifted to her from her grandfather.")
    prints("Ash, caught off guard, freezes up, before Ember nudges him and tells him to focus. He draws his battleaxe, appearing very heavy, and lifts it over his shoulder.")
    prints("You engage the goblin first, dealing a direct slash to his stomach, which doesnt pierce the armor. Ash leaps onto Embers shoulder, jumps off, and deals a crushing aerial strike, which staggers the goblin.")
    prints("Ember then follows up, closing the distance alarmingly fast, nearly teleporting. She travels ~15 feet in a second, before dealing a precise slash to an artery on the goblins neck, killing him instantly.")
    prints("You: Well, we sure made quick work of that one, huh guys?")
    prints("Ember: yeah, youre so amazing at fighting, man!")
    prints("You: Yeah yeah, it was a one time fluke, relax.")
    prints("Ash: Well, who has to babysit now, eh?")
    prints("You and ember together: Ash, shut up.")
    prints("You travel into a town, before deciding to rest up a bit. you book a hotel, and spend the night in your room.")
    prints("Ember and ash are sitting at the table, conversating loudly. You sit at a desk, sharpening your blade, the rubies which are embedded in the hilt glistening in the light of the torch and the steel, with its intricate floral design shining.")
    prints("Ember: ...And thats when i told him, 'thats not an elephant! thats a frog!'")
    prints("They both burst out laughing rather loudly. you nearly cut your hand on the blade from the surprise.")
    prints("Suddenly, they start talking quietly, but you can still make out some words.")
    prints("Ash: just tell him how you...")
    prints("Ember: Its not that simple, ash... you know that.")
    prints("You: What are yall whispering about over there, how great i am?")
    prints("Ember turns, suddenly VERY red.")
    prints("Ember: NONE OF YOUR BUSINESS! GO BACK TO SHARPENING YOUR BLADE, SLASH MISSER!")
    prints("Ash, rolling his eyes: Nice one, ember.")
    prints("Ember: Fuck off, both of you!")
    prints("You go back to your blade, and Ember and Ash go back to conversating loudly. Later you all go to bed.")
    prints("You awaken in the middle of the night to Ember pacing and muttering under her breath. You pretend not to hear, like you never woke up, and try to fall back asleep.")
    prints("Ember approaches your bed, and touches your face, while standing behind you. She lays next to you, wrapping herself around you, before passing out.")
    prints("You, used to it by now since she does this EVERY time she drinks, fall back asleep.")
    prints("The next morning, you all set out again, keeping score of how many goblins youve killed each like a game.")
    prints("Ember wins by 15, with you in second beating Ash out by 1.")
    prints("In town earlier you caught word of a dungeon that needed cleaning, you were promised 250 gold coins to clear it, so you and your comrades set out.")
    prints("Arriving at the dungeone, you clear waves of goblins like nothing, eventually setting up camp deep in the dungeon.")
    prints("Ash and Ember start drinking again, but Ember goes light tonight. Ash, however, downs 12 bottles of whiskey.")
    prints("You: Ash if you keep goin like this youll burn through your liver before ya see your thirties.")
    prints("Ash: Have ya seen what its like out there? we seein the same world right?")
    prints("You: Suppose thats fair. Whatever, aint my liver after all. do what ya will i suppose.")
    prints("You continue sharpening your blade to keep it in top shape, before heading to bed for the night.")
prints("You are startled awake by the sounds of blades clashing. You look up, and see your comrade, Ash, who now has a sword through his chest, which most likely doesnt belong there. Upon realizing this you stand at the ready, frantically drawing your blade, although you catch it on the scabbard three times before drawing. finally, you ready your sword, and engage the goblin.")
turndecide = True
while turndecide == True:
    if playerspeed >= goblinspeed:
        playerturn = True
        break
    else:
        goblinturn = True
        break

#the first fight ONLY. DO NOT reuse this logic.
startcombat = True
while startcombat == True and goblinhp > 0 and playerhealth > 0 and playdead == False:
    print(f"goblinHP: {goblinhp}")
    print(f"EmberHP: {emberhealth}")
    print(f"PlayerHP: {playerhealth}")
    if emberhealth < 0:
        printss("...")
        prints("Upon realizing Ember has fallen, you go into a blind rage, slashing and tearing at the goblin, until you take his head off, then you slash him more. Then, once the goblin has been confirmed dead, you rush to embers side.")
        prints("You: 'Ember! Are you ok?!'")
        time.sleep(0.5)
        prints("Ember: 'i... it... hurts... heh... w...what wou-*cough*...what would... Ash say... heh...'")
        time.sleep(0.2)
        prints("You: 'Ember, i... ill go get help, just do-'")
        time.sleep(0.35)
        prints("Ember: 'no. its... too late... think... lo-look... how much blood ive lost...'")
        time.sleep(0.35)
        prints("You look at the ground, realizing its been painted in blood, a pool laying beneath Ember, her steel armor, once shining now a deep crimson.")
        time.sleep(0.35)
        prints("Ember: 'I... was... gonna a-ask... you out... after this- *cough* -dungeon... ya know. I w-wish... i... could have. in my... bag... is a dagger... take it. Its... yours now. I wont need... it.'")
        prints("Embers eyes cloud up, as she grows cold. Its clear to you shes gone, although it doesnt quite hit you yet.")
        time.sleep(0.25)
        prints("You go to the bag, opening it up. Inside is a few gold coins, and a dagger. You pick up the dagger, running your fingers across the blade. Engraved is three words.")
        time.sleep(1)
        prints("The words read 'i love you.'")
        time.sleep(1)
        prints("Your vision begins to blur. The world feels numb. The stone beneath your knees cold, the air thick and heavy with grief. You start to cry. As the tears form, you begin to black out.")
        playdead = True
        break
    if playerturn == True:
        fprints("its your turn!")
        playeraction = input("What do you do? (attack, attack, attack)").lower()
        if playeraction == "attack":
            goblinhp -= playerdamage
            fprints(f"You slash at the goblin, dealing {playerdamage} damage!")
            playerturn = False
            goblinturn = True
    if goblinturn == True:
        emberhealth -= 35
        print("The goblin slashes wildly, striking Ember for 35 hp!")
        goblinturn = False
        emberturn = True
    if emberturn == True and emberhealth > 0:
        prints("Ember: 'Take THIS!")
        goblinhp -= 15
        print("Ember slashes at the goblin, dealing 15 damage")
        emberturn = False
        playerturn = True
#end first fight

#dead
while playdead == True:
            print("You feel your knees buckling. Your arms falling. You cant hold up your sword. You feel the goblin finally pierce your chest. A flash of pain envelops your body, as the goblin chuckles. You collapse.")
            time.sleep(1)
            action = input("You see a strange man. Do you approach him? (Y/N) ").lower()
            if action == "n":
                prints("You approach him anyways. What have you got to lose?")
                prints("the strange man: 'You were killed in the line of battle. I suppose you werent as strong as you seemed, kid... but the story isnt done here. not yet. You havent avenged your comrades. What would ember think, kid? What about Ash? Have you forgotten your vows? Your promises?'")
                prints("Get up.")
                time.sleep(0.75)
                prints("I said get up, kid.")
                prints("You slowly awaken.")
                prints("You appear to be in a village. Hundreds of thoughts attack your brain, pain rioting from your left arm... or, more like what USED to be your left arm. You look to where your arm once was and see a disgusting mess - flesh hanging from bone, fingers torn apart, muscle exposed, partially wrapped in bandages.")
                prints("a nurse rushes in, tending to yourarm, and injects it with a serum - something that appears reddish green - before you can react. After she removes the needle from your arm you yank it back.")
                prints("Then, your arm starts reforming. Must be a magic healing syringe. Your arm reappears from near nothing.")
                prints("nurse: 'thank goodness youre awake, i was worried you might have died. When you were brought into our clinic you didnt look much better than your arm was, haha!")
                reply = input("1: 'well, ive seen better days, but worse ones too, haha.' 2: 'Really? Good lord i cant even imagine, there was nothing left of my arm!' (1/2) ")
                prints(f"{reply}")
                break
            if action == "y":
                prints("You approach the strange man.")
                prints("the strange man: 'You were killed in the line of battle. I suppose you werent as strong as you seemed, kid... but the story isnt done here. not yet. You havent avenged your comrades. What would ember think, kid? What about Ash? Have you forgotten your vows? Your promises?'")
                prints("Get up.")
                time.sleep(0.25)
                prints("I said get up, kid.")
                prints("You slowly awaken.")
                prints("You appear to be in a village. Hundreds of thoughts attack your brain, pain rioting from your left arm... or, more like what USED to be your left arm. You look to where your arm once was and see a disgusting mess - flesh hanging from bone, fingers torn apart, muscle exposed, partially wrapped in bandages.")
                prints("a nurse rushes in, tending to yourarm, and injects it with a serum - something that appears reddish green - before you can react. After she removes the needle from your arm you yank it back.")
                prints("Then, your arm starts reforming. Must be a magic healing syringe. Your arm reappears from near nothing.")
                prints("nurse: 'thank goodness youre awake, i was worried you might have died. When you were brought into our clinic you didnt look much better than your arm was, haha!")
                reply = input("1: 'well, ive seen better days, but worse ones too, haha.' 2: 'Really? Good lord i cant even imagine, there was nothing left of my arm!' (1/2) ")
                prints(f"{reply}")
                break
#end dead

#start of actual game
prints("15 days later, youve been discharged from the hospital. You go to the local graveyard and make graves for your comrades - though their bodies do not lie beneath.")
prints("You try to cry but the tears dont come. Doesnt matter, 'tears are a waste of water, and a solider wastes nothing', your father always said.")
prints("However you cant stay here forever. You are destined for great things.")
path = input("Pick your path, lone warrior. (Bounty hunter, Revenge, Mercenary) ").lower()
if path == "revenge":
    prints("coming soon. this is an entirely different experience that will not be implemented until much later.")
exploring = True
while exploring == True:
    action = input("What will you do? (explore, check inventory, view summons)").lower()
    if action == "check inventory":
        prints(f"weapon: {currentwep}")
        prints(f"armor: {currentarmor}")
        prints(f"items: {playeritems}")
        action = input("back, inspect").lower()
        if action == "inspect":
            action = input("Inspect which item?").lower()
            if action == "Embers Dagger":
                prints("You pull the dagger from your bag, and turn it over in your hands. Its a high quality dagger, most likely costing a lot of money. Engraved into it are the words 'i love you'.")
            if action == "Familiar Longsword":
                prints("You pull the longsword from its scabbard, resting on your left hip. you turn it in your hands, memories flashing. Fighting alongside Ash and Ember, slaughtering goblins - and some memories that arent yours.")
    if action == "view summons":
        prints(f"Current Summons: {summons}")
        action = input("Back, Inspect").lower()
        if action == "inspect":
            action = input("Inspect which summon?").lower()
            if action == "sasha":
                print("A wolf, with a long, silver-grey coat, and a wide body. Shes a very strong and dependable ally.")
    if action == "explore":
        action = input("Where do you go? (Cave, )")