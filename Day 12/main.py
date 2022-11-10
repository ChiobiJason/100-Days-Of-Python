from art import logo
from random import randrange

print(logo)
print(
    "Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100."
)

print("I'm thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

no_of_tries = 0

if difficulty_level == "easy":
    no_of_tries = 10
elif difficulty_level == "hard":
    no_of_tries = 5

random_number = randrange(1, 101)

while no_of_tries != 0 and no_of_tries > 0:
    print(f"You have {no_of_tries} attempts remaining to guess the number")
    guess = eval(input("Make a guess: "))
    if guess > random_number and no_of_tries == 1:
        print("Too high.")
        print(
            f"You've run out of guesses, you lose  and the answer was {random_number}."
        )
        no_of_tries -= 1
        break
    elif guess < random_number and no_of_tries == 1:
        print("Too low.")
        print(
            f"You've run out of guesses, you lose and the answer was {random_number}."
        )
        no_of_tries -= 1
        break
    if guess > random_number:
        print("Too high.")
        print("Guess again.")
        no_of_tries -= 1
    elif guess < random_number:
        print("Too low.")
        print("Guess again.")
        no_of_tries -= 1
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        no_of_tries = 0
