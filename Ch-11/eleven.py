# -----------------------------------------------INHERITANCE & MORE ON OOPS-------------------------------------------------------
'''
Inheritance is a way of creating a new class from an existing class.
'''
# Syntax:

class Employee: # Base class
    # Code
    def __init__(self):
        pass

class Programmer (Employee): # Derived or child class
     def __init__(self):
        pass

'''
We can use the method and attributes of 'Employee' in 'Programmer' object.
Also, we can overwrite or add new attributes and methods in 'Programmer' class.
TYPES OF INHERITANCE
1) Single inheritance
2) Multiple inheritance
3) Multilevel inheritance
'''
# -----------------------------------------------Single inheritance-------------------------------------------------------
class Employee:
    company = "ITC"
    name="John"
    salary=123
    language="python"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)
a.show() 
b.showLanguage()

# -----------------------------------------------Multiple inheritance------------------------------------------------------
class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     
class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
# -----------------------------------------------Multilevel inheritance-------------------------------------------------------
class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)
# -----------------------------------------------Super Method-------------------------------------------------------
# super() method is used to access the methods of a super class in the derived class.
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Manager()
print(o.a, o.b, o.c)
'''
output:
Constructor of Programmer
Constructor of Manager
1 2 3
'''
# -----------------------------------------------Class Method-------------------------------------------------------
# A class method is a method which is bound to the class and not the object of the class.
'''
Syntax:
@classmethod
   def(cls,p1, p2):
'''
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show() #The class attribute of a is 1
# -----------------------------------------------Property Decorators and @.GETTERS AND @.SETTERS--------------------------------------------------
class Employee:

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.name = "John Fitzgerald"
print(e.fname, e.lname)

# -----------------------------------------------OPERATOR OVERLOADING IN PYTHON-------------------------------------------------------
'''
Operators in Python can be overloaded using dunder methods.
These methods are called when a given operator is used on the objects.

Operators in Python can be overloaded using the following methods:
p1+p2 # pl.__add__(p2)
p1-p2 # p1.__sub__(p2)
p1*p2 #p1.__mul__(p2)
p1/p2 #p1.__truediv_(p2)
p1//p2 # pl.__floordiv__(p2)

Other dunder/magic methods in Python:
str__() # used to set what gets displayed upon calling str(obj)
_len_() # used to set what gets displayed upon calling._len_() or len(obj)
'''

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)
