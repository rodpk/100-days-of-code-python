## list of cards

## generate random cards for the player and machine

## player cards

## machine cards

## check if the player wants to add anothr card

## if add should remove from list of cards

## verify if machine can add another card

##  in the end, check who is closer to 21, or if anyone passes the 21.

## check draw

## ends with < 17 must take another card

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    drawed = random.choice(cards)
    cards.remove(drawed)
    return drawed

def calculate_score(cards_array):
    final_value = 0
    for card in cards_array:
        final_value += card
    return final_value

def find_winner(player_score, machine_score):
    if player_score > 21 and machine_score > 21 or player_score == machine_score:
        return 'draw'
    elif player_score > machine_score and player_score <= 21 or machine_score > 21:
        return 'player won'
    elif machine_score > player_score and machine_score <= 21 or player_score > 21:
        return 'machine won'

play_again = True

while play_again:
    print(logo)
    player_cards = [ draw_card(), draw_card() ]
    computer_cards = [ draw_card(), draw_card() ]
    print(f'Your cards: {player_cards} \nComputer\'s first card: {computer_cards[0]}')


    keep_drawing = True
    while keep_drawing:

        another = input('Draw another card? (y/n): ').lower()

        if (another == 'y'):
            player_cards.append(draw_card())
            print(f'Your cards: {player_cards} - Sum: {calculate_score(player_cards)}')
        else:
            keep_drawing = False
    
    computer_cards_sum = calculate_score(computer_cards)
    
    
    if (computer_cards_sum < 21 or computer_cards_sum < 17):
        computer_cards.append(draw_card())
        computer_cards_sum = calculate_score(computer_cards)

    player_cards_sum = calculate_score(player_cards)
    winner = find_winner(player_cards_sum, computer_cards_sum)
    
    print('-----------------------------------')
    print(f'Machine cards: {computer_cards} - Sum: {computer_cards_sum}')
    print(f'Player cards: {player_cards} - Sum: {player_cards_sum}')

    print('+++++++++++++++++++++++++++++++++++')
    print(f'++ Result: {winner}           ++')
    print('+++++++++++++++++++++++++++++++++++')

    print('-----------------------------------')

    aswr = input('Want to play again ? (y/n): ').lower()
    
    play_again = True if aswr == 'y' else False