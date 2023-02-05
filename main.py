from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def add_str():
    t.insert('2.4', 'Hello')


def del_str():
    t.delete('1.0', END)


def get_str():
    print(t.get('1.0', END))


def open_file():
    file_path = filedialog.askopenfilename(
        title="Выбор файла", filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    if file_path:
        t.delete('1.0', END)
        t.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Сохранение", filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    file = open(file_path, 'w', encoding='utf-8')
    text = t.get('1.0', END)
    file.write(text)
    file.close()


def close():
    answer = messagebox.askokcancel(
        title="Выход", message="Закрыть программу?")
    if answer:
        root.destroy()


def change_theme(theme_name):
    t['bg'] = theme_color[theme_name]['text_bg']
    t['fg'] = theme_color[theme_name]['text_fg']
    t['insertbackground'] = theme_color[theme_name]['cursor']
    t['selectbackground'] = theme_color[theme_name]['select_bg']


def about_program():
    messagebox.showinfo(title="О программе",
                        message="KitText версия 0.0.1")


# Словарь тем
theme_color = {
    "dark": {
        "text_bg":      "#343D46",
        "text_fg":      "#C6DEC1",
        "cursor":       "#EDA756",
        "select_bg":    "#4E5A65"
    },
    "light": {
        "text_bg":      "#fff",
        "text_fg":      "#000",
        "cursor":       "#8000FF",
        "select_bg":    "#777"
    },
}

# Создание главного окна, его разрешение и расположение при запуске
root = Tk()
root.title('KitText')  # создание титульника
root.iconbitmap('icon.ico')
root.geometry('1000x500+300+100')

main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label="File")
# main_menu.add_command(label="About")

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=close)
main_menu.add_cascade(label="Файл", menu=file_menu)

# Редактирование
redaction_menu = Menu(main_menu, tearoff=0)
redaction_menu.add_command(label="Очистить окно", command=del_str)
main_menu.add_cascade(label="Правка", menu=redaction_menu)

# Тема
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(
    label="Light Theme", command=lambda: change_theme('light'))
theme_menu_sub.add_command(
    label="Dark Theme", command=lambda: change_theme('dark'))
theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command=about_program)
main_menu.add_cascade(label="Разное", menu=theme_menu)

# f_menu = Frame(root, bg="#1F252A", height=40)
# f_menu.pack(fill=X)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)


# Найстройка окна ввода текста
t = Text(f_text, bg=theme_color['dark']['text_bg'], fg=theme_color['dark']['text_fg'], padx=10, pady=10, wrap=WORD,
         insertbackground=theme_color['dark']['cursor'], selectbackground=theme_color['dark']['select_bg'], width=30, spacing3=10, font=("Courier New", 11))
t.pack(fill=BOTH, expand=1, side=LEFT)

# Найстройка скрола
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
