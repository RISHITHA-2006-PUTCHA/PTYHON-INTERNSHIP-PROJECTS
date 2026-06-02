python
import random

print("===== Number Guessing Game =====")

while True:
    print("\nSelect Difficulty Level")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print("4. Exit")

    level = input("Enter your choice: ")

    if level == '1':
        limit = 10
        attempts = 5

    elif level == '2':
        limit = 50
        attempts = 7

    elif level == '3':
        limit = 100
        attempts = 10

    elif level == '4':
        print("Game Closed")
        break

    else:
        print("Invalid Choice")
        continue

    secret_number = random.randint(1, limit)

    print(f"\nGuess a number between 1 and {limit}")

    for i in range(attempts):
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed correctly")
            break

        elif guess < secret_number:
            print("Too Low")

        else:
            print("Too High")

        print("Attempts Left:", attempts - i - 1)

    else:
        print("You Lost")
        print("Correct Number was:", secret_number)
