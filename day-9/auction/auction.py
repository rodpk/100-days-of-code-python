import imp
import os
from art import logo
clear = lambda: os.system('cls')

bidders_list = []

while True:
    print(logo)
    
    name = input('What is your name?: ')
    bid = float(input('What\'s your bid?: $'))

    bidders_list.append( {"name": name, "bid": bid} )
    aswr = input('Are there any other bidders? (y/n): ').lower()

    clear()
    if aswr == 'n':
        break

winner = {}
greatest_bid = 0

for bidder in bidders_list:
    if bidder["bid"] > greatest_bid: 
        greatest_bid = bidder["bid"]
        winner = bidder
    

#print("who is the winner????")
print(f'The winner is {winner["name"]} with the value of $ {winner["bid"]}')