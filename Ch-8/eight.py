# -----------------------------------------------FUNCTIONS & RECURSIONS-------------------------------------------------------
'''
TYPES OF FUNCTIONS IN PYTHON

There are two types of functions in python:
  1- Built in functions (Already present in python)
  2- User defined functions (Defined by the user)

Examples of built in functions includes len(), print(), range() etc.
'''

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(average)


avg() # Function Call
print("Thank you!")
avg()
print("Thank you!")
avg()
print("Thank you!")

# -----------------------------------------------FUNCTIONS WITH ARGUMENTS-------------------------------------------------------
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

a = goodDay("Jonny", "Thank you") 
print(a)


# -----------------------------------------------DEFAULT PARAMETER VALUE-------------------------------------------------------
def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Mohan", "Thanks")
goodDay("Rohan")


# -----------------------------------------------RECURSION-------------------------------------------------------

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")