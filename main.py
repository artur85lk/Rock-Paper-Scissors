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
    game(point)
def game(point):
    point = point
    while True:
        option = ["rock", "paper", "scissors"]
        computer = random.choice(option)

        you = input()
        if you == "!exit":
            print("Bye!")
            break
        elif you == "!rating":
            print(f"Your rating: {point}")
        elif you in option:

            win = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
            if win[you] == computer:
                print(f"Sorry, but the computer chose {computer}")
            elif win[computer] == you:
                point += 100
                print(f"Well done. The computer chose {computer} and failed")
            else:
                print(f"There is a draw ({computer})")
                point += 50
        else:
            print("Invalid input")
            continue

if __name__ == '__main__':
    name()
