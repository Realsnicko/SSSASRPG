import shutil
import os
import time
import platform
player = {
    "name": "Player",
    "hp": 100,
    "max_hp": 100,
    "level": 1,
    "exp": 0,
    "gold": 0
}
text_speed = 0.05  # default speed
def center_block(text):
    columns = shutil.get_terminal_size().columns
    for line in text.split("\n"):
        print(line.center(columns))
OS = platform.system()
def cls():
    if OS == "Windows": os.system('cls')
    else: os.system('clear')
def death():
    cls()
    global state
    death_ascii = r"""









__     __           _____  _          _ 
\ \   / /          |  __ \(_)        | |
 \ \_/ /__  _   _  | |  | |_  ___  __| |
  \   / _ \| | | | | |  | | |/ _ \/ _` |
   | | (_) | |_| | | |__| | |  __/ (_| |
   |_|\___/ \__,_| |_____/|_|\___|\__,_|





"""
    center_block(death_ascii)
    time.sleep(2.5)
    print("Continue | Main Menu")
    action = input("").lower()
    if action == "main menu":
        exit
    if action == "continue":
        print("Bartender: 'So, whatcha need?'")
        time.sleep(1)
        Bartendialogue = True
        while Bartendialogue:
            print("")
            print("")
            print("1) 'Got any work that needs doing?' | 2) 'What do you mean, 'anymore'?'  | 3) 'What do yall have to drink 'round here?' | 4) 'WAIT- WHat- what- why... how... how am i back..?' | 5) end dialogue.")
            print("(You can use 1-3 for dialogue choices.)")
            dialogue = input("")
            if dialogue == "1":
                print("Bartender: 'Heh, boy do we have work for you. Grab a-")
                time.sleep(1)
                print("Bartender: 'Oh. You meant like mercenary work.")
                time.sleep(1)
                print("The bartender sighs.")
                time.sleep(1)
                print("Bartender: 'Yeah, we have that to. Theres this group of bandits been bothering us. Theyre based out in a cave towards the south of here.")
                time.sleep(1)
                print("Bartender: 'Here. Ill mark it for you. Go clear that out and ill pay you well. Anything else you need?")
                caveopen = True
                time.sleep(3)
            if dialogue == "2":
                print("Everyone suddenly goes quiet.")
                time.sleep(1)
                print("The bartender looks at you. The look on his face tells you that you likely werent supposed to ask that question. Perhaps you shouldnt question this anymore...")
                time.sleep(3)
            if dialogue == "3":
                print("Bartender: 'Water.'")
                time.sleep(1)
                print("Bartender: 'Thats it.'")
                time.sleep(3)
            if dialogue == "4":
                print("You feel yourself up and down, thoroughly patting yourself.")
                time.sleep(1)
                print("Youre perfectly ok. Unharmed. You look around.")
                time.sleep(1)
                print("The bartenders giving you a funny look. A group of thugs in the corner look annoyed, staring at you.")
                time.sleep(1)
                print("Bartender: 'You feelin alright kid..? Maybe you should get some fresh air. Be careful actin like that, dont wanna attract unwanted attention.'")
            if dialogue == "5":
                Bartendialogue = False
                gameloop = True
                state = "towncenter"
                cls()
def prints(text, delay=None):
    global text_speed
    if delay is None:
        delay = text_speed if text_speed is not None else 0.03
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()