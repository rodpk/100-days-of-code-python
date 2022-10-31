######## NUMBER GUESSING GAME #############
from art import logo
import random
import logic

print(logo)
print("*** Welcome to the Number Guessing Game! ***")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(0, 101)

print(f"Psst... don't tell anyone, but Im thinking the number {number}")

difficulty = logic.choose_difficulty()
attempts = logic.get_attempts(difficulty)
player_won = False

while attempts > 0:

    try:
        guessed_number = int(input("Make a guess: "))
    except:
        print('You need to inform a number')
        continue
    
    if (logic.check_number(guessed_number, number)):
        attempts -= 1
        print(f"You have {attempts} attempts, guess Again.")
    else:
        player_won = True
        break

if player_won:
    print(f"Well done, the number I was thinking is {number}. You have found it in {attempts} attempts in {difficulty} difficulty")
else:
    print(f"It's a shame, you could not find the number I was thinking about the number {number}")