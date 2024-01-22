# Задания № 1
""" Создайте несколько функций, которые выполняют арифметические операции (сложение, вычитание, умножение) 
для разных типов данных (целые числа, дроби, строки). 
Используйте статический полиморфизм для обработки разных типов данных одним и тем же кодом."""

"""def perform_operation(a, b, operation):
    try:
        result = operation(a, b)
        print(f"Результат операции: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")


def add_integers(x, y):
    return x + y

def subtract_integers(x, y):
    return x - y

def multiply_integers(x, y):
    return x * y

def add_floats(x, y):
    return round(x + y, 2)

def subtract_floats(x, y):
    return round(x - y, 2)

def multiply_floats(x, y):
    return round(x * y, 2)


def concatenate_strings(x, y):
    return x + y


perform_operation(5, 3, add_integers)
perform_operation(7.5, 2.2, multiply_floats)
perform_operation("Hello", " World", concatenate_strings)"""

# Задания № 2

"""Создайте базовый класс Shape c методом агеа), который вычисляет площадь фигуры.
Затем создайте подклассы, представляющие разные геометрические фигуры, такие
как Circle, Rectangle n Triangle.
Переопределите метод агеа) в каждом подклассе для вычисления площади соответствующей фигуры."""

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print(f"Площадь круга: {circle.area()}")
print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Площадь треугольника: {triangle.area()}")



