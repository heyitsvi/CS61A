# Object Orieneted Programming using Python

class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def printFullName(self):
        print(f'Hi this is {self.first_name} {self.last_name}')

class Developer(Employee):
    def __init__(self, first_name, last_name, age, salary, programming_lang):
        super().__init__(first_name, last_name, age, salary)
        self.programming_lang = programming_lang


emp1 = Developer("Amit", "Yadav", 22, 50000, "JavaScript")
print(emp1.printFullName())