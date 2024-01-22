# Задания № 1

""" Создайте контекстный менеджер, который измеряет время выполнения блока кода.
Затем используйте его для измерения времени выполнения операции ввода-вывода и вывода этого времени в миллисекундах."""

import contextlib
import time

@contextlib.contextmanager
def timing_context():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # in milliseconds
    print(f"Elapsed time: {elapsed_time:.2f} milliseconds")


with timing_context():
    user_input = input("Введите что-то: ")
    print(f"Вы ввели: {user_input}")

