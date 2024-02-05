# Задания № 1

""" Создайте простой интерфейс с несколькими метками и кнопками. Разместите текст на метках и добавьте функциональность к кнопкам."""

"""import tkinter as tk

def bold():
    text.tag_add("bold", tk.SEL_FIRST, tk.SEL_LAST)
    text.tag_config("bold", font=("Times New Roman", 14, "bold"))

window = tk.Tk()
window.title("Главное окно")
text = tk.Text(window, height=30, width=50)
text.pack()
button = tk.Button(window, text="Сделать жирным текст", command=bold)
button.pack()
window.mainloop()"""

# Задания № 2 

"""Создайте интерфейс, включающий в себя текстовое поле для ввода текста и текстовую область для отображения и редактирования текста. 
Реализуйте функциональность для работы с этими компонентами."""

"""import tkinter as tk

def update_text():
    text_area.delete(1.0, tk.END)  
    text_area.insert(tk.END, input_field.get())  

window = tk.Tk()
window.title("Текстовый редактор")


input_field = tk.Entry(window, width=50)
input_field.pack(pady=10)


text_area = tk.Text(window, height=10, width=50)
text_area.pack()


update_button = tk.Button(window, text="Обновить текст", command=update_text)
update_button.pack(pady=10)

window.mainloop()"""

