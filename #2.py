class Employee:
    name = None
    age = None
    city = None
    pass

people = Employee()

people.name = "Иван"
people.age = 17
people.city = "Вологда"

print(people.name)
print(people.age)
print(people.city)