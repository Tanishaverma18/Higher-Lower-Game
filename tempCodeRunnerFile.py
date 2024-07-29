compare_A = random.choice(data)
print(f"Compare A: {compare_A["name"]}, {compare_A["description"]}, from {compare_A["country"]}")
print(vs)
compare_B = random.choice(data)
print(f"Compare B: {compare_B["name"]}, {compare_B["description"]}, from {compare_B["country"]}")
if compare_A == compare_B:
    compare_B = random.choice(data)
Choose = input("Who has more followers? Type 'A' or 'B': ").lower()
is_correct = check(Choose, compare_A, compare_B)
if is_correct:
    score += 1
    print(f"You're right! Current Score: {score}")
else:
    print("Sorry, That's wrong! Final Score: {Score}")
