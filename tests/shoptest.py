#shoptest
#prices
items = [
    "Sword",
    "Chestplate"
]
swordprice = 5
chestplateprice = 15
money = 20
#items
while True:
    print(f"{items}")
    print(f"Sword: {swordprice}")
    print(f"Chestplate: {chestplateprice}")
    buy = input(f"What will you buy? you have {money} dollars. ").lower()
    if buy == "sword":
        money -= swordprice
        print("You bought the sword.")
        print(f"{money}")