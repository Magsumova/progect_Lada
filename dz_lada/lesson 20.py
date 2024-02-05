# Задания № 1

""" Создайте простой интерфейс с текстовой меткой и кнопкой.
При нажатии на кнопку, текст на метке должен изменяться."""

"""import tkinter as tk
def on_enter_pressed(event):
    text = entry.get()
    label.config(text="Enter нажата. Текст:"+ text)
    
root = tk.Tk()
root.title("Пример с событием клавиатуры")


entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>",on_enter_pressed)

label = tk.Label(root, text= "")
label.pack()

root.mainloop()"""

# Задания № 2

""" Создайте интерфейс с текстовым полем и кнопкой
"Очистить". При нажатии на кнопку, 
текстовое поле должно очищаться. 
Также добавьте возможность ввода текста с клавиатуры и кнопку, 
которая будет выполнять действие при нажатии на клавишу Enter."""

"""import tkinter as tk

def clear_text():
    entry.delete(0, tk.END)

def on_enter_pressed(event):
    text = entry.get()
    label.config(text="Enter нажата. Текст:" + text)
    clear_text()

root = tk.Tk()
root.title("Пример с интерфейсом")

entry = tk.Entry(root)
entry.pack()

clear_button = tk.Button(root, text="Очистить", command=clear_text)
clear_button.pack()

def on_enter_pressed(event):
    text = entry.get()
    label.config(text="Enter нажата. Текст:" + text)
    clear_text()

entry.bind("<Return>", on_enter_pressed)

label = tk.Label(root, text="")
label.pack()

root.mainloop()"""