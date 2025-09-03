# 5. Write a program which finds out whether a given name is present in a list or not.

namesList = ["John", "Mohan", "Shyam", "Divi"]

name = input("Enter your name: ")

if(name in namesList):
    print("Your name is in the list")
else:
    print("Your name is not in the list")