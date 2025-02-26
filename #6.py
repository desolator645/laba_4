class Emoloyee:
    def show(self, name, salary):
        return name + ' - ' + salary
  
user = Emoloyee()
user.show('Romanov', '500 Dollars ')
print(user.show('Romanov', '500 Dollars '))