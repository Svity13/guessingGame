import random

def mainMenu():
    print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\n")
    print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    option = int(input("Enter your choice: "))
    if option == 1:
        gameEasy()
    elif option == 2:
        gameMed()
    elif option == 3:
        gameHard()

def gameEasy():
    r1 = random.randint(0, 50)
    for i in range(10):
        guess = int(input("Enter your guess: "))
        if guess == r1:
            print("Congrats you got it right!")
            break
        elif guess > r1:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < r1:
            print(f"Incorrect! The number is more than {guess}")
    print(f"The number was {r1}")

def gameMed():
    r1 = random.randint(0, 50)
    for i in range(5):
        guess = int(input("Enter your guess: "))
        if guess == r1:
            print("Congrats you got it right!")
            break
        elif guess > r1:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < r1:
            print(f"Incorrect! The number is more than {guess}")
    print(f"The number was {r1}")

def gameHard():
    r1 = random.randint(0, 50)
    for i in range(3):
        guess = int(input("Enter your guess: "))
        if guess == r1:
            print("Congrats you got it right!")
            break
        elif guess > r1:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < r1:
            print(f"Incorrect! The number is more than {guess}")
    print(f"The number was {r1}")

mainMenu()
