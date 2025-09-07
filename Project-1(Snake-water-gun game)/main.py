'''
We all have played snake, water gun game in our childhood. 
If you haven't, google the rules of this game and write a python program capable of playing this game with the user.

snake = 1
water = -1
gun = 0
'''

import random

computer = random.choice([-1, 0, 1])

choice = input("Enter your choice(s, w, g): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[choice]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    '''
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")
    '''

    if(((computer - you)==-1) or ((computer - you)==2)):
        print("You Lose!")
    else:
        print("You Win!")