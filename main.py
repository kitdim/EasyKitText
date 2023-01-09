from tkinter import *

def add_str():
    t.insert('2.4', 'Hello')

def del_str():
    t.delete('1.0', END)

def get_str():
    print(t.get('1.0',END))




root = Tk()
root.geometry('400x400+1000+300')



f_menu = Frame(root, bg="#1F252A", height=40)
f_text = Frame(root)
f_menu.pack(fill = X)
f_text.pack(fill=BOTH, expand=1)

l_menu = Label(f_menu, text="Menu", bg="#2B3239", fg="#C6DEC1", font="Arial 10")
l_menu.place(x=10, y=10)

btn_add = Button(root, text="Add", command=add_str).place(x=50,y=10) #размещение кнопки на добавление строки
btn_del = Button(root, text="Delete", command=del_str).place(x=90,y=10) #размещение кнопки на удаление строки
btn_get = Button(root, text="Get", command=get_str).place(x=140,y=10) #размещение кнопки для получение строки

t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap = WORD, 
        insertbackground = "#EDA756", selectbackground = "#4E5A65", width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side = LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side= LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()