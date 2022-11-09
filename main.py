import random


def name():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    point = 0
    with open('rating.txt', 'r', encoding='utf-8') as test:
        for line in test:
            l = line.split()
            if l[0] == name:
                point = int(l[1])
    hight_game = input()
    print("Okay, let's start")
    game(point, hight_game)


def game(point, hight):
    point = point
    if hight == "":
        option = ["rock", "paper", "scissors"]
        win = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    else:
        option = hight.split(",")
        win = {"rock": ["lightning", "gun", "air", "water", "dragon", "paper", "devil"],
               "gun": ["lightning", "sponge", "air", "water", "dragon", "paper", "devil"],
               "lightning": ["wolf", "sponge", "air", "water", "dragon", "paper", "devil"],
               "devil": ["wolf", "sponge", "air", "water", "dragon", "paper", "tree"],
               "dragon": ["wolf", "sponge", "air", "water", "human", "paper", "tree"],
               "water": ["wolf", "sponge", "air", "snake", "human", "paper", "tree"],
               "air": ["wolf", "sponge", "scissors", "snake", "human", "paper", "tree"],
               "paper": ["wolf", "sponge", "scissors", "snake", "human", "fire", "tree"],
               "sponge": ["wolf", "rock", "scissors", "snake", "human", "fire", "tree"],
               "wolf": ["gun", "rock", "scissors", "snake", "human", "fire", "tree"],
               "tree": ["gun", "rock", "scissors", "snake", "human", "fire", "lightning"],
               "human": ["gun", "rock", "scissors", "snake", "devil", "fire", "lightning"],
               "snake": ["gun", "rock", "scissors", "dragon", "devil", "fire", "lightning"],
               "scissors": ["gun", "rock", "water", "dragon", "devil", "fire", "lightning"],
               "fire": ["lightning", "gun", "air", "water", "dragon", "rock", "devil"]}

    while True:
        computer = random.choice(option)
        print(computer)
        you = input()
        if you == "!exit":
            print("Bye!")
            break
        elif you == "!rating":
            print(f"Your rating: {point}")
        elif you in option:

            if computer in win[you]:
                print(f"Sorry, but the computer chose {computer}")
            elif you in win[computer]:
                point += 100
                print(f"Well done. The computer chose {computer} and failed")
            elif you == computer:
                print(f"There is a draw ({computer})")
                point += 50
        else:
            print("Invalid input")
            continue


if __name__ == '__main__':
    name()
