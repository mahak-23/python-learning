# -----------------------------------------------OBJECT ORIENTED PROGRAMMING-------------------------------------------------------
'''
Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming.
This concept focuses on using reusable code (DRY Principle).
'''
# -----------------------------------------------CLASS-------------------------------------------------------
'''
A class is a blueprint for creating object.
Syntax:
class Employee: # Class name is written in pascal case
    #Methods & Variables
'''
# -----------------------------------------------OBJECT------------------------------------------------------
'''
An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.
Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. - Abstractions & Encapsulation!
'''
# -----------------------------------------------MODELLING A PROBLEM IN OOPS-------------------------------------------------------
'''
We identify the following in our problem.
1) Noun → Class → Employee
2) Adjective → Attributes name, age, salary
3) Verbs → Methods → getSalary(), increment()
'''
# -----------------------------------------------CLASS ATTRIBUTES-------------------------------------------------------
'''
 An attribute that belongs to the class rather than a particular object.
'''
class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


john = Employee()
john.name = "John" # This is an instance attribute
print(john.name, john.language, john.salary)

rohan = Employee()
rohan.name = "Rohan Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
# -----------------------------------------------INSTANCE ATTRIBUTES-------------------------------------------------------
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

john = Employee()
john.language = "JavaScript" # This is an instance attribute
print(john.language, john.salary)
 

# -----------------------------------------------SELF PARAMETER and STATIC METHOD--------------------------------------------------
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


john = Employee()
# john.language = "JavaScript" # This is an instance attribute
john.greet()
john.getInfo() 
# Employee.getInfo(john)


# -----------------------------------------------_INIT_() CONSTRUCTOR-------------------------------------------------------

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


john = Employee("John", 1300000, "JavaScript") 
# john.name = "John"
print(john.name, john.salary, john.language)
