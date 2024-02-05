# Задания № 1

""" Создайте интерфейс, включающий в себя список элементов и выпадающий список.
Разработайте логику для выбора элементов и организации компонентов"""

"""import tkinter as tk
from tkinter import ttk

def show_selected():
    selected_item = listbox.get(listbox.curselection())
    selected_label.config(text="Выбранный элемент: " + selected_item)

window = tk.Tk()
window.title("Выбор элементов")


elements = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"]
listbox = tk.Listbox(window, selectmode=tk.SINGLE)
for element in elements:
    listbox.insert(tk.END, element)
listbox.pack(pady=10)


dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(window, textvariable=dropdown_var)
dropdown["values"] = elements
dropdown.pack(pady=10)


selected_label = tk.Label(window, text="Выбранный элемент: ")
selected_label.pack(pady=10)


show_button = tk.Button(window, text="Показать выбранный элемент", command=show_selected)
show_button.pack(pady=10)

window.mainloop()"""