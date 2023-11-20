


# Задания № 1
""" Напишите программу, которая выводит все четные числа от 0 до 20 включительно"""

'''number = 20
count = 0

while count <= number:
    print(count)
    count += 2'''

# Задания № 2

 #Напишите программу, которая запрашивает у пользователя число n и выводит таблицу умножения для этого числа от 1 до 10.'''


'''n = int(input('Введите число n: '))

count = 1
while count <= 10:
    sum = n * count
    print(f"{n} x {count} = {sum}")
    count += 1'''
    
# Задания № 3

''' Напишите программу с использованием цикла for, которая выведет каждую букву в строке
"Python".'''

'''string = 'Python'

for python in string:
    print(python)
    '''
# Задания № 4

''' Напишите программу с использованием цикла while, которая считает сумму всех нечетных чисел от 1 до 100.'''

'''sum = 0
number = 1

while number <= 100: 
    sum += number
    number += 2
    
print("Сумма нечетных чисел:",sum)'''

# Задания № 5

''' Напишите программу, которая запрашивает у пользователя число и выводит все четные числа от 0 до введенного числа включительно.'''

'''number = int(input('Введите любое число: '))
count = 0

while count <= number:
    print(count)
    count += 2'''
    
# Задания № 6

''' Напишите программу, которая запрашивает у пользователя число и находит сумму всех чисел от 1 до введенного числа.'''

'''sum = 0
number = 1
user_number = int(input('Введите любое число: '))

while number <= user_number: 
    sum += number
    number += 1
    
print("Сумма чисел:",sum)'''

# Задания № 7

''' Напишите программу с использованием вложенных циклов, которая выводит следующую пирамиду:'''

"""number_st = 5

count = '*'

for i in range(number_st):
    for i in range(1):
        print(count)
        count += '*'"""
        
# Задания № 8

''' Напишите программу с использованием вложенных циклов, которая выводит таблицу умножения от 1 до 5.'''

'''number = 5
count = 1

for i in range(number):
    for i in range(1):
        divide = number * count
        print(f"{count}*{number}={divide}")
        count+=1'''
        
# Задания № 9

"""Напишите программу с использованием вложенных циклов, которая проверяет, является ли заданное число простым. Проверьте все числа от 2 до заданного числа """

"""upper_limit = int(input("Введите число: "))

for number in range(2, upper_limit + 1):
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    status = "простое" if is_prime else "не простое"
    print(f"{number} - {status}")"""
    
# Задания № 10

""""Создание программы для вывода всех четных чисел в диапазоне от 1 до заданного числа."""

''''user_number = int(input('Введите любое число: '))

for i in range(1,user_number + 1):
    if i % 2 == 0:
        print(i)'''
        
# Задания № 11
''' Реализация "Мини-викторины" с вопросами и вариантами ответов, используя цикл for.'''

'''print('---------- "Мини-викторины" с вопросами и вариантами ответов, проверкой правильности и выводом результата. ----------')
print()

# Инициализируем счетчики правильных и неправильных ответов
correct_answers = 0
incorrect_answers = 0

questions = [
    ('Химический знак водорода это? \n a)O \n b)C \n d)H \n b)S', 'd'),
    ('У кальция атомная масса? \n a)40 \n b)20 \n d)35 \n b)65', 'a'),
    ('У кислорода на последнем энергетическом уровне? \n a)2 электрона \n b)6 электронов \n d)5 электронов \n b)4 электрона', 'b')
]

for question, correct_answer in questions:
    print(question)
    user_answer = input('Введите ответ только символами: ')

    if user_answer == correct_answer:
        print('Ответ верный.')
        correct_answers += 1
    else:
        print('К сожалению не верно.')
        incorrect_answers += 1

    print()

print('Викторина закончилась. Неправильных ответов:', incorrect_answers)
print('Правильных ответов:', correct_answers)

# Выводим правильные ответы
print('Правильные ответы:')
for i, (_, correct) in enumerate(questions, 1):
    print(f'{i}. Правильный ответ: {correct}')'''
    
# Задания № 12

''' Разработка текстовой игры с использованием циклов для повторяющихся ходов.'''


'''import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 10. Попробуйте угадать.")

number_to_guess = random.randint(1, 10)
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input("Введите вашу догадку: "))

    if guess == number_to_guess:
        print("Поздравляю! Вы угадали число.")
        break
    else:
        print("Не угадали. Попробуйте снова.")
        attempts += 1

if attempts == max_attempts:
    print(f"Игра окончена. Вы исчерпали все {max_attempts} попыток. Загаданное число было: {number_to_guess}")'''







    




        
        
