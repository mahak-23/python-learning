# 1. Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter number: "))

for i in range(10):
    print(f"{num} X {i+1} = {num * (i+1)}")