import random

print("Guessing the number!")

number = random.randint(1,9)
chances = 0

print("Guess a number between 1 to 5, you will only get 5 chances!!")

while chances < 5:
    guess = int(input("Type your guess!:- "))

    if guess == number:
        print("Congratulations! You guessed the right number!!")
        chances=5

    elif guess > number:
        print("Nope, try to guess lower")
    else:
        print("Nope, try to guess higher")

    chances= chances + 1

if chances > 5:
    print("GAME OVER, the number was:", number)
    