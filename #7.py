class Emoloyee:
    def show_name(self):
        print(self.name)
    def show_salary(self):
        print(self.salary)
  
user = Emoloyee()

user.name = 'Romanov'
user.salary = '500 Dollars'
user.show_name()
user.show_salary()