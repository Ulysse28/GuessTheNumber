"""
A little game where you have to guess what number Python decided for you
"""

import random
def guess(n):


    x = random.randint(1, n)
    y = 0
    scr = 0

    while x != y:
        print(f"Choose a number between 1 and {n}")
        y = int(input())
        print(f"You chose the number {y}")
        if y < x:
            print("It's more !")
            scr +=1
        elif y > x:
            print("It's less !")
            scr -=1
    print(f"Great ! You did it in {scr + 1} times !")


guess(10)