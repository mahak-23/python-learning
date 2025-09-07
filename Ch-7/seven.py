# -----------------------------------------------LOOPS IN PYTHON-------------------------------------------------------
'''Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!'''
print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1, 6):
    print(i)

# -----------------------------------------------TYPES OF LOOPS IN PYTHON-------------------------------------------------------

'''Primarily there are two types of loops in python.
while loops
for loops'''

# -----------------------------------------------WHILE LOOP-------------------------------------------------------
i = 1
while(i<51):
    print(i)
    i +=1 # or i = i + 1

'''
Output:
1
2
3
4
5
'''

l = [1, "John", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1

# -----------------------------------------------FOR LOOP-------------------------------------------------------
for i in range(4):
    print(i)

## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Johny"
for i in s:
    print(i)

# -----------------------------------------------RANGE FUNCTION IN PYTHON-------------------------------------------------------
'''The range() function in python is used to generate a sequence of number.
We can also specify the start, stop and step-size as follows:
range (start, stop, step_size)'''
#step_size is usually not used with range()

# -----------------------------------------------FOR LOOP WITH ELSE-------------------------------------------------------
l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!

# -----------------------------------------------THE BREAK STATEMENT-------------------------------------------------------
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)


# -----------------------------------------------THE CONTINUE STATEMENT-------------------------------------------------------
for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    


# -----------------------------------------------THE PASS STATEMENT-------------------------------------------------------
'''It instructs to "do nothing" '''
1 = [1,7,8]
for item in 1:
    pass  # without pass, the program will throw an error