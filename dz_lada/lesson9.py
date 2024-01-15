# Задания № 1

''' Создание словаря с информацией о студентах и вывод этой информации на экран.У даление студента из словаря по имени'''

'''student = {
    "Alina" : "21",
    "Vika" : "25", 
    "Karina" : "20",
    "Marina" : "26",
    "Mike" : "30"
    }

print("Имена студентов в словаре:",list(student.keys()))
del_student = input("Введите имя студента которые хотите удалить: ")

if del_student in student:
    del student[del_student]
    print(student)
else:
    print("Извините такого студента нету ")'''
    
# Задания № 2

''' Создайте словарь инвентарь с информацией о товарах в магазине. 
Каждый товар должен иметь уникальный идентификатор (как ключ словаря) 
и содержать следующие поля: название, количество, цена.'''

"""inventory = {
    1: {'Названия': 'Яблоки', 'количество': 10, 'цена': 1200},
    2: {'Названия': 'Персики', 'количество': 40, 'цена': 2000},
    3: {'Названия': 'Мандарины', 'количество': 20, 'цена': 2000}
}

for key, value in inventory.items():
    print(f"Товар ID: {key},\nНазвание: {value['Названия']},\nКоличество: {value['количество']},\nЦена: {value['цена']}\n")"""
    
    
# Задания № 3

""" Создайте два множества множество1 и множество2 с некоторыми общими и разными элементами."""

'''my_set1 = {1,23,4,5,6,78,8}
my_set2 = {34,45,65,2,21,4,5}

print("Разность: ",my_set1.difference(my_set2))
print("Общие: ",my_set1.union(my_set2))'''

# Задания № 4

"""Создание множества из списка
элементов.Определение
пересечения и объединения двух множеств."""

"""my_set1 = {1,23,4,5,6,78,8}
my_set2 = {34,45,65,2,21,4,5}

print('Определение: ',my_set1.difference(my_set2))
print('пересечения: ',my_set1.intersection(my_set2))
print('объединения: ',my_set1.union(my_set2))"""

# Задания № 5

"""Напишите функцию поиск_товара(), которая принимает идентификатор товара и возвращает информацию о нем."""

"""def search_product(identifier):
    products = {
        1: {"name": "Книга", "price": 500, "availability": True},
        2: {"name": "Ноутбук", "price": 1500, "availability": False},
        3: {"name": "Фонарик", "price": 200, "availability": True},
        # Добавьте другие товары по аналогии
    }

    if identifier in products:
        return products[identifier]
    else:
        return "Товар не найден"

product_identifier = 2
search_result = search_product(product_identifier)
print(search_result)"""

# Задания № 6

""" Напишите функцию нахождение пересечения(), 
которая принимает два множества и возвращает их пересечение 
(элементы, которые есть и в первом, и во втором множестве)."""

"""def finding_intersection(my_set1,my_set2):
    return my_set1.intersection(my_set2)
    
my_set1 = {1,23,4,5,6,78,8}
my_set2 = {34,45,65,2,21,4,5}

intersections = finding_intersection(my_set1,my_set2)
print('Пересечение:',intersections)"""

# Задания № 7

"""Создайте словарь страны_и города, где ключи
названия стран, а значения
списки городов в этих странах. Которые будут добавляться с Терминала"""
    

"""countries_cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск"],
}


country = input('Введите страну, в которую хотите добавить город: ')
city = input('Введите город: ')


if country in countries_cities:
    countries_cities[country].append(city)
else:
    countries_cities[country] = [city]


print(countries_cities)"""

# Задания № 8

""" Напишите функцию подсчет_стоимости(), которая считает общую стоимость всех товаров в инвентаре"""

"""def calculate_total_cost(inventory):
    total_cost = 0
    for item_id, characteristics in inventory.items():
        quantity = characteristics['quantity']
        price = characteristics['price']
        total_cost += quantity * price
    return total_cost

inventory = {
    1: {'Name': 'Apples', 'quantity': 10, 'price': 1200},
    2: {'Name': 'Peaches', 'quantity': 40, 'price': 2000},
    3: {'Name': 'Mandarins', 'quantity': 20, 'price': 2000}
}

result = calculate_total_cost(inventory)
print('Общая стоимость товаров на складе:', result)"""

# Задания № 9

""" Напишите функцию нахождение объединения
(, которая принимает два множества и возвращает их объединение
(все уникальные элементы из обоих множеств)."""

def association_location(my_set1,my_set2):
    return my_set1.union(my_set2)
    
my_set1 = {1,23,4,5,6,78,8}
my_set2 = {34,45,65,2,21,4,5}

associations = association_location(my_set1,my_set2)
print('объединения:',associations)

 


    


    
    

    




