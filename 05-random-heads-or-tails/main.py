print("Welcome to Guess the Coin Challenge!")

import random

user_guess = input("Guess Heads or Tails: ")
random_head_or_tails = random.choice(["Heads", "Tails"])

print(f"System Chose {random_head_or_tails}")

if user_guess == random_head_or_tails:
    print("Correct! You Guessed it right!")
else:
    print("Wrong! try agian!")