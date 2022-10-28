import random


## PREPS
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Psst, the chosen word is {chosen_word}')

display = []

for _ in range(word_length):
    display.append('_')

## GAME

chances = 5
end_of_game = False
lost = False


## ( display.__contains__('_') or chances <= 0 )
while not end_of_game:
    guess = input('Guess a letter: ')
    found = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            found = True
    if (not found):
        chances -= 1
        print(chances)
    print(display)

    if "_" not in display:
        end_of_game = True
    elif chances == 0:
        end_of_game = True
        lost = True

if not lost:
    print(f'Well done, the answer is {chosen_word}')
else:
    print(f'You\'ve lost, the answer was {chosen_word}')