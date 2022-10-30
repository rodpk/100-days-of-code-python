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


def sum(cards_array):
    final_value = 0
    for card in cards_array:
        final_value += card
    return final_value

def check_winner(player_sum, computer_sum):
    ## result: player win, machine win or draw

    ## player win = closest to 21 or machine passes 21, player != machine
    ## machine win = closest to 21 or player passes 21, machine player
    ## draw = both lose or both has the same value

    player_won = False
    machine_won = False
    draw = False

    if (player_sum == computer_sum or (player_sum > 21 and computer_sum > 21)):
        print('draw')
        draw = True
    elif player_sum > 21:
        print('psum')
        player_won = False
    elif computer_sum > 21:
        print('csum')
        computer_won = False
    elif (21 - player_sum) < (21 - computer_sum):
        print('pwon')
        player_won = True
    else:
        print('mwon')
        machine_won = True
    
    if player_won: return 'player won'
    elif machine_won: return 'machine won'
    else: return 'draw'

# computer_cards = [ draw_card(), draw_card() ]
# player_cards = [ draw_card(), draw_card() ]


# player_cards_sum = sum(player_cards)
# computer_cards_sum = sum(computer_cards)

# winner = check_winner(player_cards_sum, computer_cards_sum)
# print(f'Computer cards: {computer_cards}, Player cards: {player_cards}')
# print(f'Player sum: {player_cards_sum}, Machine sum: {computer_cards_sum}, Result: {winner}')


while True:
    print(logo)
    player_cards = [ draw_card(), draw_card() ]
    computer_cards = [ draw_card(), draw_card() ]
    print(f'Your cards: {player_cards}\nComputer\'s first card: {computer_cards[0]}')

    another = input('Draw another card? (y/n)').lower()

    if (another == 'y'):
        player_cards.append(draw_card())
        print(f'Your cards: {player_cards}')
    
    computer_cards_sum = sum(computer_cards)
    
    
    if (computer_cards_sum < 21 or computer_cards_sum < 17):
        computer_cards.append(draw_card())
        computer_cards_sum = sum(computer_cards)

    player_cards_sum = sum(player_cards)
    winner = check_winner(player_cards_sum, computer_cards_sum)
    print(f'Computer cards: {computer_cards}, Player cards: {player_cards}')
    print(f'Player sum: {player_cards_sum}, Machine sum: {computer_cards_sum}, Result: {winner}')
    break