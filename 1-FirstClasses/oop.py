# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

# Python Object-Oriented Programming

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'


emp1 = Employee('Ruby', 'Wang', '5000')
emp2 = Employee('Pf', 'Wang', '6000')


print(emp1.full_name())
# equal to print(Employee.full_name(emp1))
print(emp2.full_name())

# emp1 and emp2 are instances, which is the self variable 

