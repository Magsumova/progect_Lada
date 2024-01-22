# Задания № 1

""" Создайте класс Person, представляющий человека, с атрибутами name и age.
Определите метод introduce, который будет выводить приветствие с именем и возрастом человека."""

"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"Привет меня зовут: {self.name}, Мне {self.age}")
        
person_1 = Person("Марина",25)
person_2 = Person("Катя",26)

person_1.introduce()
person_2.introduce()"""

# Задания № 2

"""Создайте класс, представляющий продукт в интернет-магазине. 
Реализуйте методы экземпляра для управления информацией о продукте, 
такие как добавление описания и установка цены."""


"""class Product():
    def __init__(self,name,descripsion="",price=0.0):
        self.name = name
        self.descripsion = descripsion
        self.price = price
        
        def set_description(self, description):
            self.description = descripsion

    def set_price(self, price):
        if price >= 0:
            self.price = price
        else:
            print("Цена не может быть отрицательной.")

    def display_info(self):
        print(f"Название: {self.name}")
        print(f"Описание: {self.description}")
        print(f"Цена: {self.price} руб.")


product1 = Product("Ноутбук", "Мощный и легкий", 1200.0)
product1.display_info()


product1.set_description("Ультрабук для профессионалов")
product1.set_price(1299.99)


product1.display_info()"""

    