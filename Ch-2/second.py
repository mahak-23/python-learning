# -----------------------------VARIABLES----------------------------

a=1
b=3
c=2
name="MK"
print(a+b)




# -----------------------------DATATYPE--------------------------

a = 1 # a is an integer
b = 5.22 # b is a floating point number
c = "MK" # c is a string
d = False # d is a boolean variable
e = None # e is a none type variable




# --------------------------Rules Variables-------------------------------

a = 23
aaa = 435
Name = 34
John = 45
_John = 34

# @John = 56 # Invalid due to @ symbol
# J@ohn # Invalid due to @ symbol





# ------------------------------OPERATORS---------------------------------


# Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)

# Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b)

# Comparison Operators
d = 5==5
print(d)


# Logical Operators
e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))





# --------------------TYPE() FUNCTION AND TYPECASTING.------------------------
a = 31
print(type(a)) #<class 'int'>
b = "31.2"
print(type(b)) #<class 'str'>
b = float(a) # a but the type should be float
print(type(b), b) #<class 'float'> 31.0

t = str(a)
print(type(t)) #<class 'str'>




# ---------------------------input() FUNCTION------------------------------

a = input("Enter a value ")
b = input("Enter b value ")
print("sum is: ", a+b)

a1 = int(input("Enter number 1: "))
b1 = int(input("Enter number 2: "))
print("Number a1 is: ", a1)
print("Number b1 is: ", b1) 
print("Sum is ", a1 + b1)
