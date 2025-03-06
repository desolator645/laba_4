class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = str(salary)
        
employees = [
    Employee('Ivan', 100),
    Employee('Egor', 101),
    Employee('Lev', 102)
]
    
for employee in employees:
    print(employee.name,employee.salary)