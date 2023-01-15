from tkinter import *


def add_str():
    t.insert('2.4', 'Hello')


def del_str():
    t.delete('1.0', END)


def get_str():
    print(t.get('1.0', END))


def open_file():
    del_str()
    t.insert('2.4', 'Открытие файла не готово')


def save_file():
    del_str()
    t.insert('2.4', 'Сохранение файла не готово')


def close_file():
    del_str()
    t.insert('2.4', 'Закрытие файла не готово')


root = Tk()
root.geometry('400x400+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label="File")
# main_menu.add_command(label="About")

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=close_file)
main_menu.add_cascade(label="Файл", menu=file_menu)

# Редактирование
redaction_menu = Menu(main_menu, tearoff=0)
redaction_menu.add_command(label="Очистить окно", command=del_str)
main_menu.add_cascade(label="Редактирование", menu=redaction_menu)

# Справка
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Онлайн")
help_menu_sub.add_command(label="Оффлайн")
help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_command(label="О программе")
main_menu.add_cascade(label="Справка", menu=help_menu)

# f_menu = Frame(root, bg="#1F252A", height=40)
# f_menu.pack(fill=X)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)


# Найстройка окна ввода текста
t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD,
         insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

# Найстройка скрола
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
