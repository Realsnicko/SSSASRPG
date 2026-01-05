#screentest
import os
import msvcrt

title_art = """
  ▄▄▄▄▄     ▄▄▄▄▄     ▄▄▄▄▄       ▄▄      ▄▄▄▄▄     ▄▄▄▄▄▄     ▄▄▄▄▄▄    ▄   ▄▄▄▄ 
 ██▀▀▀▀█▄  ██▀▀▀▀█▄  ██▀▀▀▀█▄   ▄█▀▀█▄   ██▀▀▀▀█▄  █▀██▀▀▀█▄  █▀██▀▀▀█▄  ▀██████▀ 
 ▀██▄  ▄▀  ▀██▄  ▄▀  ▀██▄  ▄▀   ██  ██   ▀██▄  ▄▀    ██▄▄▄█▀    ██▄▄▄█▀    ██   ▄ 
   ▀██▄▄     ▀██▄▄     ▀██▄▄    ██▀▀██     ▀██▄▄     ██▀▀█▄     ██▀▀▀      ██  ██ 
 ▄   ▀██▄  ▄   ▀██▄  ▄   ▀██▄ ▄ ██  ██   ▄   ▀██▄  ▄ ██  ██   ▄ ██         ██  ██ 
 ▀██████▀  ▀██████▀  ▀██████▀ ▀██▀  ▀█▄█ ▀██████▀  ▀██▀  ▀██▀ ▀██▀         ▀█████ 
"""

options = ["Start", "Options", "Config"]
current = 0

while True:
    os.system('cls')  # clear screen
    print(title_art)
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
