'''
We are going to write a program that generates a random number and asks the user to guess it.
If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly, if the user's guess is too low, the program prints "higher number please" When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module.
'''

import random

num = random.randint(1, 100)

print("Please Guess Number between 1 to 100")

guesses = 1
choice=-1

while choice != num:

    choice = int(input("Please enter number: "))

    if(choice < num):
        print("please enter higher number")
        guesses+=1
    elif(choice > num):
        print("please enter lower number")
        guesses+=1

else:
    print(f"You have guessed the number {num} correctly in {guesses} attempts")