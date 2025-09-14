# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a  = [1,2,66, 55, 35, 78654, 5321145]

f = list(filter(divisible5, a))
print(f)