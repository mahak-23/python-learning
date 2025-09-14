# -----------------------------------------------VIRTUAL ENVIRIONMENT-------------------------------------------------------
'''
An environment which is same as the system interpreter but is isolated from the other
Python environments on the system.
'''
# -----------------------------------------------INSTALLATION-------------------------------------------------------
'''To use virtual environments, we write:
    pip install virtualenv # Install the package

We create a new environment using:
    virtualenv myprojectenv # Creates a new venv

The next step after creating the virtual environment is to activate it. 
.\myprojectenv\Scripts\Activate.ps1
We can now use this virtual environment as a separate Python installation.

we can deactivate env in terminal
  deactivate
'''

# -----------------------------------------------PIP FREEZE COMMAND------------------------------------------------------
'''  
"pip freeze" returns all the package installed in a given python environment along with the versions.

  pip freeze > requirements .txt

The above command creates a file named "requirements.txt" in the same directory containing the output of "pip freeze".
We can distribute this file to other users, and they can recreate the same environment using:

  pip install –r requirements.txt
'''

# -----------------------------------------------LAMBDA FUNCTIONS-------------------------------------------------------
'''
Function created using an expression using "lambda" keyword.
Syntax:
   lambda arguments:expressions
'''

# def square(n):
#     return n*n 

square = lambda x: x*x

print(square(5))

# -----------------------------------------------JOIN METHOD (STRINGS)-------------------------------------------------------
'''Creates a string from iterable objects.'''

l = ["apple", "mango", "banana"]
result = ", and, ".join(l)
print(result) # output:  “apple,and,mango,and,banana”.

# -----------------------------------------------FORMAT METHOD (STRINGS)--------------------------------------------------
'''
Formats the values inside the string into a desired output.
template.format(p1,p2...)
Syntax:
"{} is a good {}".format("John", "boy") #1.
"{} is a good {o}".format("John", "boy") #2.
# output for 1:
# John is a good boy
# output for 2:
# boy is a good John 
'''
a = "{1} is a good {0}".format("John", "boy")

print(a)
# -----------------------------------------------MAP, FILTER & REDUCE-------------------------------------------------------
'''
Map applies a function to all the items in an input_list.
Syntax.
   map(function, input_list) # the function can be lambda function

Filter creates a list of items for which the function returns true.
   list(filter(function))  # the function can be lambda function

Reduce applies a rolling computation to sequential pair of elements.

    from functools import reduce
    val=reduce (function, list1)  # the function can be lambda function
'''
from functools import reduce
# Map Example 
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example
def even(n):
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))