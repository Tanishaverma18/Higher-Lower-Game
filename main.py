from art import logo
from art import vs
import random
from game_data import data
import os

score = 0
game_should_continue = True
def check(Choose, compare_A, compare_B):
    if compare_A["follower_count"] > compare_B["follower_count"]:
        return Choose == "a" # returns True
    else:
        return Choose == "b" # returns False
    
compare_B = random.choice(data)

while game_should_continue:
    compare_A = compare_B
    print(f"Compare A: {compare_A["name"]}, {compare_A["description"]}, from {compare_A["country"]}")

    print(vs)

    compare_B = random.choice(data)
    print(f"Against B: {compare_B["name"]}, {compare_B["description"]}, from {compare_B["country"]}")

    if compare_A == compare_B:
        compare_B = random.choice(data)

    Choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check(Choose, compare_A, compare_B)

    # Clearing the Screen
    os.system('cls')
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, That's wrong! Final Score: {score}")
