# Задания № 1

""" Создайте главное окно вашего примера приложения с различными компонентами, 
такими как метки, кнопки и текстовые поля. 
Зарегистрируйте обработчики событий для какой-либо из кнопок и добавьте функциональность."""

import tkinter as tk

def update_label():
    new_text = entry.get()
    label.config(text=new_text)

root = tk.Tk()
root.title("Пример приложения")


label = tk.Label(root, text="Нажмите кнопку, чтобы изменить текст")
label.pack()


entry = tk.Entry(root)
entry.pack()


button = tk.Button(root, text="Изменить текст метки", command=update_label)
button.pack()

root.mainloop()