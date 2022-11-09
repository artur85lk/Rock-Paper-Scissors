import random

def game():
    while True:
        option = ["rock", "paper", "scissors"]
        computer = random.choice(option)
        you = input()
        if you == "!exit":
            print("Bye!")
            break
        elif you in option:

            win = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
            if win[you] == computer:
                print(f"Sorry, but the computer chose {computer}")
            elif win[computer] == you:
                print(f"Well done. The computer chose {computer} and failed")
            else:
                print(f"There is a draw ({computer})")
        else:
            print("Invalid input")
            continue

if __name__ == '__main__':
    game()
