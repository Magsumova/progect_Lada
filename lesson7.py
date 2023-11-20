# Задания № 1

""" Практика
Попробуйте написать свою функцию, которая решает какую-либо задачу.
Например, функцию для вычисления факториала числа, определения простого числа и т.д."""

'''def is_prime(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Пример использования
user_input = int(input("Введите число: "))
if is_prime(user_input):
    print(f"{user_input} - простое число.")
else:
    print(f"{user_input} - не простое число.")'''
    
# Задания № 2

''' Разработка программы для конвертации температуры из Цельсия в Фаренгейт и обратно, используя функции.'''

'''def celsius_to_fahrenheit(celsius):
    """Конвертирует температуру из Цельсия в Фаренгейт."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Конвертирует температуру из Фаренгейта в Цельсий."""
    return (fahrenheit - 32) * 5/9

# Пример использования
temperature_celsius = float(input("Введите температуру в градусах Цельсия: "))
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius} градусов Цельсия равны {temperature_fahrenheit} градусам Фаренгейта.")

temperature_fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit} градусов Фаренгейта равны {temperature_celsius} градусам Цельсия.")'''

# Задания № 3

''' Создание программы для нахождения наименьшего общего кратного (НОК)
двух чисел с использованием функций.'''

'''def find_gcd(x, y):
    """Находит наибольший общий делитель (НОД) двух чисел."""
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    """Находит наименьшее общее кратное (НОК) двух чисел."""
    return abs(x * y) // find_gcd(x, y)

# Пример использования
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

lcm_result = find_lcm(number1, number2)
print(f"Наименьшее общее кратное ({number1}, {number2}): {lcm_result}")'''

# Задания № 4

""" Создание функции для вычисления факториала числа."""

'''def factorial(n):
    """Вычисляет факториал числа."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования
number = int(input("Введите число для вычисления факториала: "))
result = factorial(number)
print(f"Факториал числа {number} равен {result}")'''

# Задания № 5

""" Разработка калькулятора для расчета ежемесячных выплат по кредиту с использованием функций."""

'''def calculate_monthly_payment(loan_amount_kzt, annual_interest_rate, loan_term):
    """Рассчитывает ежемесячный платеж по кредиту в тенге."""
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = loan_term * 12

    # Формула для расчета ежемесячного платежа
    monthly_payment_kzt = (loan_amount_kzt * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    return monthly_payment_kzt

# Пример использования
loan_amount_kzt = float(input("Введите сумму кредита в тенге: "))
annual_interest_rate = float(input("Введите годовую процентную ставку (%): "))
loan_term = int(input("Введите срок кредита в годах: "))

monthly_payment_result_kzt = calculate_monthly_payment(loan_amount_kzt, annual_interest_rate, loan_term)
print(f"Ежемесячный платеж по кредиту составит: {monthly_payment_result_kzt:.2f} тенге.")'''

# Задания № 6

""" Напишите функцию
is_palindrome_number(number),
которая будет проверять, является ли данное число палиндромом (читается одинаково слева направо и справа налево). Например, 121 или 1331 являются палиндромами."""

'''def is_palindrome_number(number):
    """Проверяет, является ли число палиндромом."""
    number_str = str(number)
    return number_str == number_str[::-1]

# Пример использования
user_input = int(input("Введите число: "))

if is_palindrome_number(user_input):
    print(f"{user_input} - это палиндром.")
else:
    print(f"{user_input} - это не палиндром.")'''


