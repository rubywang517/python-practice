# https://www.youtube.com/watch?v=BJ-VvGyQxho

# Python Object-Oriented Programming

class Employee:

    raise_amount = 1.04 
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'
        Employee.num_of_emp += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # NOTE: it can also be the following
        # self.pay = int(self.pay * Employee.raise_amount)


emp1 = Employee('Ruby', 'Wang', '5000')
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
emp1 = Employee('Pf', 'Wang', '6000')
print(Employee.num_of_emp)

# first practice 
# we can access class variable by both class and instance 
# self.pay = int(self.pay * self.raise_amount)
# self.pay = int(self.pay * Employee.raise_amount)
print(emp1.raise_amount)
print(Employee.raise_amount)

# second practice
print(emp1.__dict__)
print(Employee.__dict__)
# it is only in Employee's name space

# third practice 
# we can change class variable and all instance variables will also change
Employee.raise_amount = 1.05
print(emp1.raise_amount)
print(Employee.raise_amount)

# fourth practice 
# we can change class variable from instance but it only applies to instance
emp1.raise_amount = 1.06
print(emp1.raise_amount)
print(Employee.raise_amount)
# and it will appear in the namespace of instance
print(emp1.__dict__)









