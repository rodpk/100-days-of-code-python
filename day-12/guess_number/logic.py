def check_number(guessed_number, number):
    guess_again = True
    if guessed_number > number:
        print("Too high")
    elif guessed_number < number:
        print("Too low")
    elif guessed_number == number:
        #print(f"Well done, the number I was thinking is {number}")
        guess_again = False
    return guess_again

def get_attempts(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 5
    elif difficulty == "hard":
        return 3

def choose_difficulty():
    difficulty_list = ["easy", "medium", "hard"]
    incorrect_difficulty = True
    while incorrect_difficulty:
        difficulty = input(f'Choose a difficulty {difficulty_list}: ').lower()
        if difficulty not in difficulty_list:
            print("Wrong difficulty, try again")
        else:
            return difficulty
