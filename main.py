"""
A little game where you have to guess what number Python decided for you
By Ulysse Valdenaire
"""
#import random module to get a random number 
import random

#function of the game
def guess():
    replay = ""
    #Loop of the game
    while replay != "NO":
        n = input("You have to guess a number between 0 and : choose the number you want ! : ")
        n = int(n)
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
                scr +=1
        print(f"Great ! You did it in {scr + 1} times !")
        #If the player wants to play again
        replay = input("Do you want to play again ? YES / NO ")
        y = 0
    #If the player quits the game
    print("It's was great playing with you ! See you ! ")


#call of the function
guess()