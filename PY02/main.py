#! venv/bin/python3
from random import randint

if __name__ == '__main__':
    while True:
        total = 0
        target = randint(0, 100) # a random number is chosen
        print("Objective: enter up to 10 numbers which sum to a randomly chosen target value")
        for move in range(0, 10): # 10 moves to hit the target
            uinp = input("Enter a number: ") # user enters a number
            try:
                inp = int(uinp)
                total += inp # inputs are summed together
            except ValueError:
                print(f"{uinp} is not a valid integer")
                continue
            if total == target: # the aim is to hit the target
                print(f"Target hit! Moves taken: {move + 1}")
                print(f"Target was {target}")
                break # stop the game if the user has 'won'
            print(f"Current total: {total} is {'greater' if total > target else 'lower'} than target")
        if input("Play again (y/n): ").lower() == "n":
            break