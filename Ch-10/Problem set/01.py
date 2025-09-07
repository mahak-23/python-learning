# 1. Create a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company="My_company"

    def __init__(self, name, salary, id):
        self.name=name
        self.salary=salary
        self.id=id


p = Programmer("John", 1200000, 101)
print(p.name, p.salary, p.id, p.company)
r = Programmer("Rohan", 1200000, 102)
print(r.name, r.salary, r.id, r.company)

 