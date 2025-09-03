# -----------------------------------------------CONDITIONAL EXPRESSION-------------------------------------------------------


# -----------------------------------------------IF ELSE AND ELIF IN PYTHON-------------------------------------------------------
a = int(input("Enter your age: "))

# If else statement
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")


print("End of Program")

# -----------------------------------------------RELATIONAL OPERATORS-------------------------------------------------------

# Relational Operators are used to evaluate conditions inside the if statements. Some
# examples of relational operators are:
# ==: equals.
# > =: greater than/ equal to.
# < =: lesser than/ equal to.


# -----------------------------------------------LOGICAL OPERATORS-------------------------------------------------------

# In python logical operators operate on conditional statements. For Example:
# and - true if both operands are true else false.
# or - true if at least one operand is true or else false.
# not-inverts true to false & false to true.


# -----------------------------------------------ELIF CLAUSE-------------------------------------------------------

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program")

# -----------------------------------------------multiple if statements-------------------------------------------------------

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")  

else:
    print("You are below the age of consent")
# End of If statement no: 2

print("End of Program")