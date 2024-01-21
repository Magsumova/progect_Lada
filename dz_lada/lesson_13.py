# Задания № 1

''' Создайте класс Саг, который имеет атрибуты brand, model и year. Добавьте метод descriptioni, который выводит
информацию о машине.'''

"""class Car ():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def descripsion (self):
        print(f"Автомобиль марки: {self.brand}, модель: {self.model}, года выпуска: {self.year}")

car1 = Car("Toyota","Camry",2022)
car2 = Car("Infiniti","FX35",2007)

car1.descripsion()
car2.descripsion()"""

# Задания № 2

""" Создайте класс Person, который имеет атрибуты name и age. Создайте подкласс
Employee, который наследует атрибуты name и age, и добавьте атрибут salary.
Реализуйте метод get_info). который выводит информацию о сотруднике."""

"""class Person ():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary
        
        
    def get_info(self):
        print(f"Имя сотрудника: {self.name}, Возраст сотрудника: {self.age}, Зарплата сотрудника: {self.salary}")
        
person1 = Employee("Алина",25,100000)
person2 = Employee("Максим",30,300000)

person1.get_info()
person2.get_info()"""

# Задания № 3

""" Создайте класс Animal, у
которого есть метод speak).
Создайте два подкласса: Dog и Cat, которые переопределяют метод speak() и возвращают соответственно Гав! и
"Мяу!"."""

"""class Animal ():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} Гав!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} Мяу!"
        
dog = Dog("Бобик")
cat = Cat("Мурка")

print(dog.speak())
print(cat.speak())"""

# Задания № 4

""" Разработайте класс BankAccount с атрибутами balance и account_number. Создайте метод deposit(), 
который позволяет внести средства на счет, и метод withdraw), который позволяет снять средства. 
Создайте подкласс SavingsAccount, который имеет атрибут interest rate и метод add_interest(), который добавляет проценты к балансу."""

"""class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Средства внесены. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Средства сняты. Новый баланс: {self.balance}")
        else:
            print("Недостаточно средств для снятия")

class SavingsAccount(BankAccount):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        super().deposit(self.balance * (self.interest_rate / 100))
        print(f"Проценты добавлены. Новый баланс: {self.balance}")


operation = int(input("Введите 1, чтобы внести деньги. Введите 2, чтобы снять деньги. Введите 3, чтобы добавить проценты: "))


bank_user = SavingsAccount(1000, "12345", 5)


if operation == 1:
    amount = float(input("Введите сумму для внесения на счет: "))
    bank_user.deposit(amount)
elif operation == 2:
    amount = float(input("Введите сумму для снятия со счета: "))
    bank_user.withdraw(amount)
elif operation == 3:
    bank_user.add_interest()
else:
    print("Введена некорректная операция.")"""
    
        


    

