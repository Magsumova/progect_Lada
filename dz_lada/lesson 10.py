# Задания № 1

"""Создайте словарь в котором будут ключами - жанры (кино/музыка), 
в значениях используйте списки с значениями для каждого жанра. 
Напишите функцию для добавления нового каталога для выбранного жанра."""

"""def add_catalog(genres, selected_genre, new_catalog):
    if selected_genre in genres:
        genres[selected_genre].append(new_catalog)
    else:
        genres[selected_genre] = [new_catalog]

# Example usage
catalogs = {
    "movies": ["Action", "Drama", "Comedy"],
    "music": ["Rock", "Pop", "Hip-Hop"]
}

new_genre = input("Введите новый жанр (фильмы/музыка): ")
new_catalog = input("Введите новый каталог: ")

add_catalog(catalogs, new_genre, new_catalog)

print("Обновленные каталоги:")
print(catalogs)"""

# Задания № 2

""" Создайте словарь, 
в котором будут хранится студенты с списком оценок. 
Напишите функцию для вычисления средней оценку каждого студента."""

"""def calculate_average_grade(students):
    average_grades = {}
    for student, grades in students.items():
        average_grades[student] = sum(grades) / len(grades)
    return average_grades

# Example usage
students_grades = {
    "Ivanov": [4, 5, 4, 3, 5],
    "Petrov": [5, 5, 5, 4, 4],
    "Sidorov": [3, 4, 4, 3, 5]
}

average_grades_students = calculate_average_grade(students_grades)

print("Average grades of students:")
for student, average_grade in average_grades_students.items():
    print(f"{student}: {average_grade}")"""
    
# Задания № 3

""" Создайте список с списками который отражает матрицу.
Реализуйте любую математическую
Функцию."""

"""def add_matrices(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)
    return result_matrix

# Пример использования
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrices(matrix_A, matrix_B)

print("Matrix A:")
for row in matrix_A:
    print(row)

print("\nMatrix B:")
for row in matrix_B:
    print(row)

print("\nResult of Matrix Addition:")
for row in result:
    print(row)"""
    
# Задания № 4

"""Создайте словарь, где ключи это названия книг, а значения - словари с информацией о каждой книге
Реализуйте поиск информации по автору."""

"""def search_by_author(books, author):
    found_books = []
    for title, book_info in books.items():
        if book_info.get('author') == author:
            found_books.append({title: book_info})
    return found_books

# Пример использования
books_dictionary = {
    'Book1': {'author': 'Author1', 'genre': 'Fiction', 'year': 2020},
    'Book2': {'author': 'Author2', 'genre': 'Non-Fiction', 'year': 2019},
    'Book3': {'author': 'Author1', 'genre': 'Mystery', 'year': 2021},
}

author_to_search = input("Введите автора для поиска: ")

results = search_by_author(books_dictionary, author_to_search)

if results:
    print(f"Найденные книги по автору {author_to_search}:")
    for book in results:
        print(book)
else:
    print(f"Нет информации о книгах автора {author_to_search}.")"""
    
# Задания № 5

''' Создайте кортеж coordinates с координатами точки в трехмерном пространстве (х,
У. 7). Напишите функцию, которая принимает этот кортеж и возвращает сумму всех его координат.'''

"""def sum_coordinates(coordinates):
    return sum(coordinates)

coordinates = (3, 5, 7)

total_sum = sum_coordinates(coordinates)

print("Point coordinates:", coordinates)
print("Sum of coordinates:", total_sum)"""

