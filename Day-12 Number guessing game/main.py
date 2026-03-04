import random

print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1-100")

random_number  = random.randrange(1, 101)
difficulty = input("Choose difficulty type easy or hard: ")

if difficulty == "easy":
    difficulty = 10
else:
    difficulty = 5

user_guess = int(difficulty)

is_game_on = True
while is_game_on:
    print(f"You have {user_guess} guess make a guess: ")
    make_guess = int(input("Make a guess: "))
    if make_guess > random_number:
        print("Too High make a guess again")
        user_guess -= 1

    elif make_guess < random_number:
        print("Too Low Make another guess")
        user_guess -= 1
    else:
        print("Correct! ")
        is_game_on = False

    if user_guess == 0:
        is_game_on = False
