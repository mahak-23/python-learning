# 10. Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))

for i in range(1, 11):
    mult =11-i
    print(f"{n} X {mult} = {n*mult}")