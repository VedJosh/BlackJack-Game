from BLACKJACK_ELEMENTS import *
import time
from BLACKJACK_ART import logo, game_over, money_finish

print(logo)
choice = 'yes'
money_user = 5000
money_computer = 5000
name = input("Your Name: ")
while choice == 'yes':
    x,y,money_user,money_computer = blackjack(name,money_user,money_computer)
    choice = input("Do you want to play BlackJack (yes/no): ").lower()
    if not x:
        print(money_finish)
        print("You Don't have enough money to play!")
        break
    elif not y:
        print("Computer does not have enough money to play!")
        break

print(game_over)
time.sleep(10)