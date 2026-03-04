from logo import logo
from data import data
import random
print(logo)
print("WELCOME TO THE HIGHER L0WER GAME")

user_score = 0

is_game_on = True

while is_game_on:

    data_a = random.choice(data)

    name1 = data_a['name']
    followers1 = int(data_a['follower_count'])
    description1 = data_a['description']
    country1 = data_a['country']

    data_b = random.choice(data)

    name2 = data_b['name']
    followers2 = int(data_b['follower_count'])
    description2 = data_b['description']
    country2 = data_b['country']

    print(f"Compare A {name1}, {description1}, from {country1}")
    print("\nVS")
    print(f"Against B: {name2}, {description2} from {country2}")


    user_guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

    def compare_followers(a, b):
        """Compares follower count and returns 'A' or 'B'"""
        if a['follower_count'] > b['follower_count']:
            return "A"
        else:
            return "B"

    # FIX: Pass full dictionary objects instead of integers
    correct_answer = compare_followers(data_a, data_b)

    if user_guess == correct_answer:
        print("Correct! ✅")
        user_score += 1
    else:
        print("Wrong Guess! ❌ Game Over!")
        is_game_on = False

    print(f"Current score: {user_score}")