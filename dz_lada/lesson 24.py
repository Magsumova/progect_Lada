import tkinter as tk

def on_checkbox():
    if var.get() == 1:
        res_label.config(text="Кнопка нажата")
    else:
        res_label.config(text="Кнопка не нажата")

root = tk.Tk()
root.title("Основное окно")
var = tk.IntVar()
checkbutt = tk.Checkbutton(root, text="Нажать", variable=var, command=on_checkbox)
checkbutt.pack()
res_label = tk.Label(root, text="")
res_label.pack()
root.mainloop()