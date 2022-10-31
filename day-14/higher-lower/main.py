import random
from game_data import data
import art
import os

def fetch_profile():
    profile = random.choice(data)
    data.remove(profile)
    return profile

clear = lambda: os.system("cls")


player_score = 0
is_running = True


profile_a = fetch_profile()

print(
profile_a["name"]
)

player_won = True

while is_running:
    print(art.logo)
    print(f"Compare A: { profile_a['name'] } ({ profile_a['description'] }) from { profile_a['country'] }")

    print(art.vs)

    profile_b = fetch_profile()
    print(f"Against B: { profile_b['name'] } ({ profile_b['description'] }) from { profile_b['country'] }.")

    print(f'a_score = { profile_a["follower_count"] }, b_score = {  profile_b["follower_count"]  }')
    choice = input(f'Who has more followers? (A/B): ').upper()

    right_choice = False
    if choice == 'A': 
        right_choice = profile_a['follower_count'] > profile_b['follower_count']
    elif choice == 'B':
        right_choice = profile_a['follower_count'] < profile_b['follower_count']

    if (not right_choice):
        is_running = False
        player_won = False
    else:
        player_score += 1
        profile_a = profile_b
        clear()

print(f'Your score = {player_score}')

