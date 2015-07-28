import random

def getRandom(int):
    return random.randint(1, int)

def game():
    highnum = input("What's your hight number?")
    target = getRandom(highnum)
    while True:
        guess = input("What's your guess dude?")
        if guess == target:
            print("You got it")
            break
        elif guess > target:
            print("Little lower")
            continue
        elif guess < target:
            print("Higher and higher!")
            continue

game()

