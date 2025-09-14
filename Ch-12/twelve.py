# -----------------------------------------------WALRUS OPERATOR-------------------------------------------------------
'''
The walrus operator (: =), introduced in Python 3.8, allows you to assign values to variables as part of an expression. 
This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression."
'''
# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 

# Output: List is too long (5 elements, expected <= 3)

# -----------------------------------------------TYPES DEFINITIONS IN PYTHON-------------------------------------------------------
'''Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.'''
#Variable type hint
age: int = 25
name: str = "Alice"

#Function type hints
def greeting(age:int, name: str) -> str:
    return f"{name} is {age} years old!"

# Usage
print(greeting(age, name)) # Output: Alice is 25 years old!

# -----------------------------------------------ADVANCED TYPE HINTS------------------------------------------------------
''' python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.'''

#You can import List, Tuple and Dict types from the typing module like this:
#The syntax of types looks something like this:

from typing import List, Tuple, Dict, Union

#List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

#Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

#Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

#Union type for variables that can hold multiple types
identifier: Union [int, str] = "ID123"
identifier = 12345 # Also valid

'''These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.'''



# -----------------------------------------------MATCH CASE-------------------------------------------------------

'''
Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming languages.
The basic syntax of the match statement involves matching a variable against several cases using the case keyword.
'''
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status (200)) # Output: OK
print(http_status (404)) # Output: Not Found
print(http_status (500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status

# -----------------------------------------------DICTIONARY MERGE & UPDATE OPERATORS-------------------------------------------------------
'''New operators | and allow for merging and updating dictionaries.'''

dict1= {'a': 1, 'b': 2} 
dict2= {'b': 3, 'c': 4} 
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1 |= dict2 # dict1 is now {'a': 1, 'b': 3, 'c': 4}

'''You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager'''

with (
    open('files/poems.txt') as f1, 
    open('files/this.txt') as f2
):
    # Process files
    print(f1.read())

# -----------------------------------------------EXCEPTION HANDLING IN PYTHON--------------------------------------------------
'''
There are many built-in exceptions which are raised in python when something goes wrong.
Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause.
When the exception is handled, the code flow continues without program interruption.
We can also specify the exception to catch like below:
'''

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e:
    print(e) 
except:
    print("others")  # All other exceptions are handled here

print("Thank You")

# -----------------------------------------------RAISING EXCEPTIONS-------------------------------------------------------
'''We can raise custom exceptions using the ‘raise’ keyword in python'''

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")

# -----------------------------------------------TRY WITH ELSE CLAUSE-------------------------------------------------------
# Sometimes we want to run a piece of code when try was successful.
try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except Exception as e:
    print(e) 
else:
    print("I am inside else")

# -----------------------------------------------TRY WITH FINALLY------------------------------------------------------
'''
Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
the exception.'''
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e) 
        return
    finally:
        print("Hey I am inside of finally") # Executed regardless
main()

# -----------------------------------------------IF __NAME__== ‘__MAIN__’ IN PYTHON -------------------------------------------------------
'''
‘__name__’ evaluates to the name of the module in python from where the program is
ran.
If the module is being run directly from the command line, the ‘ __name__’ is set to
string “__main__”. Thus, this behaviour is used to check whether the module is run
directly or imported to another file.

'''
from module import myFunc
myFunc()

# -----------------------------------------------THE GLOBAL KEYWORD-------------------------------------------------------
''' "global" keyword is used to modify the variable outside of the current scope.'''
a = 89
def fun(): 
    # global a
    a = 3
    print(a)
fun()
print(a)

# -----------------------------------------------ENUMERATE FUNCTION IN PYTHON-------------------------------------------------------
'''The "enumerate" function adds counter to an iterable and returns it'''
l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

# -----------------------------------------------LIST COMPREHENSIONS-------------------------------------------------------
'''List Comprehension is an elegant way to create lists based on existing lists.'''

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)