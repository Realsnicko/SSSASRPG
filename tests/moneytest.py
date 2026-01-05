#moneytest
import random
current_money = 2
def moneywin(current_money):
    current_money += random.randint(1,5)
    return current_money
current_money = moneywin(current_money)
print(f"{current_money}")