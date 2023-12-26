import random
from tkinter import *
from tkinter import ttk
import Book

def on_mousewheel(event):
    return "break"

Library = [Book.Book('fIyWTKDlMnAC'),Book.Book('0OxACwAAQBAJ'),
           Book.Book('29RFDQAAQBAJ'),Book.Book('fIyWTKDlMnAC')]

#todo ненужная штука в будущем
for i in Library:
    i.mark = str(random.randint(0,10))

root = Tk()
root.title("LibNote: твоя электронная библиотека")
root.geometry("1024x768")
root.resizable(False, False)

#region LoadImages
background_img = PhotoImage(file="LibNote вёрстка/Единый фон приложения.png")
menu_img = PhotoImage(file="LibNote вёрстка/Плашка меню фон.png")
my_library_button_img = PhotoImage(file="LibNote вёрстка/Плашка меню моя библиотека.png")
recomendation_button_img = PhotoImage(file="LibNote вёрстка/Плашка меню рекомендации.png")
achivement_button_img = PhotoImage(file="LibNote вёрстка/Плашка меню достижения.png")
voice_button_img = PhotoImage(file="LibNote вёрстка/Плашка меню голосовой помощник.png")
menu_logo = PhotoImage(file="LibNote вёрстка/Лого меню.png")
my_library_bg_img = PhotoImage(file="LibNote вёрстка/Моя библиотека/Доп фон моя библиотека.png")
recomendation_bg_img = PhotoImage(file="LibNote вёрстка/Рекомендации/Фон рекомендации.png")
#endregion

background = ttk.Label(image=background_img)
background.place(x=0, y=0)

def show_frame(frame):
       my_library_frame.place_forget()
       recomendation_frame.place_forget()
       frame.place(x=328,y=47)

#todo Сделать каждому статусу по функции, создание и отображение карточки
def Ml_list_click(event):
    listbox = event.widget
    index = (str(listbox.curselection()).replace(",","")
             .replace("(","").replace(")",""))
    if len(index) == 0: return




#region Menu
menu_frame = Frame(width=281, height=771,border=0)
menu_frame.place(x=-2,y=0)
ttk.Label(menu_frame, image=menu_img).place(x=0, y=0)

Button(menu_frame,image=my_library_button_img,border=0,
        bg="#CCB575",activebackground="#CCB575",
        command=lambda: show_frame(my_library_frame)).place(x=133,y=118)

Button(menu_frame,image=recomendation_button_img,border=0,
       bg="#C4AF72",activebackground="#C4AF72",
       command=lambda: show_frame(recomendation_frame)).place(x=133,y=293)

Button(menu_frame,image=achivement_button_img,border=0,
       bg="#C4AF72",activebackground="#C4AF72").place(x=133,y=466)

Button(menu_frame,image=voice_button_img,border=0,
       bg="#C4AF72",activebackground="#C4AF72").place(x=128,y=644)
#endregion

#region Моя библиотека

my_library_frame = Frame(width=696,height=675,border=0)
ttk.Label(my_library_frame, image=my_library_bg_img,background='#DFD0B0').place(x=0, y=0)
my_library_frame.place(x=328,y=47)

# Запланировано
ML_WillRead_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#5E9186')
ML_WillRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#5E9186')
ML_WillRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click(event))

if len(Library) == 0:
    ML_WillRead_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(Library,start=1):
        ML_WillRead_Mark_list.insert(END,book.mark)
        truncated_text = f"{index}. {book.get_title()[:27]}..." if len(book.get_title()) > 27 else f"{index}. {book.get_title()}"
        ML_WillRead_list.insert(END, truncated_text.ljust(45))

scrollbar_willRead = Scrollbar(my_library_frame,orient="vertical")
scrollbar_willRead.config(command=lambda *args: (ML_WillRead_list.yview(*args), ML_WillRead_Mark_list.yview(*args)))

ML_WillRead_list.place(x=99, y=76, width=597,height=130)
ML_WillRead_Mark_list.place(x=590, y=76, width=30,height=130)
scrollbar_willRead.place(x=65,y=76+15,width=15,height=130-30)

ML_WillRead_list.config(yscrollcommand=scrollbar_willRead.set)
ML_WillRead_Mark_list.config(yscrollcommand=scrollbar_willRead.set)

ML_WillRead_list.bind("<MouseWheel>", on_mousewheel)
ML_WillRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

# Читаю
ML_NowRead_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#5E9186')
ML_NowRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#5E9186')
ML_NowRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click(event))

if len(Library) == 0:
    ML_NowRead_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(Library,start=1):
        ML_NowRead_Mark_list.insert(END,book.mark)
        truncated_text = f"{index}. {book.get_title()[:27]}..." if len(book.get_title()) > 27 else f"{index}. {book.get_title()}"
        ML_NowRead_list.insert(END, truncated_text.ljust(45))

scrollbar_NowRead = Scrollbar(my_library_frame,orient="vertical")
scrollbar_NowRead.config(command=lambda *args: (ML_NowRead_list.yview(*args), ML_NowRead_Mark_list.yview(*args)))

ML_NowRead_list.place(x=99, y=448, width=597,height=130)
ML_NowRead_Mark_list.place(x=590, y=448, width=30,height=130)
scrollbar_NowRead.place(x=65,y=448+15,width=15,height=130-30)

ML_NowRead_list.config(yscrollcommand=scrollbar_NowRead.set)
ML_NowRead_Mark_list.config(yscrollcommand=scrollbar_NowRead.set)

ML_NowRead_list.bind("<MouseWheel>", on_mousewheel)
ML_NowRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

# Прочитано

ML_WasRead_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#5E9186')
ML_WasRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#5E9186')

ML_WasRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click(event))

if len(Library) == 0:
    ML_WasRead_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(Library,start=1):
        ML_WasRead_Mark_list.insert(END,book.mark)
        truncated_text = f"{index}. {book.get_title()[:27]}..." if len(book.get_title()) > 27 else f"{index}. {book.get_title()}"
        ML_WasRead_list.insert(END, truncated_text.ljust(45))

scrollbar_WasRead = Scrollbar(my_library_frame,orient="vertical")
scrollbar_WasRead.config(command=lambda *args: (ML_WasRead_list.yview(*args), ML_WasRead_Mark_list.yview(*args)))

ML_WasRead_list.place(x=99, y=262, width=597,height=130)
ML_WasRead_Mark_list.place(x=590, y=262, width=30,height=130)
scrollbar_WasRead.place(x=65,y=262+15,width=15,height=130-30)

ML_WasRead_list.config(yscrollcommand=scrollbar_WasRead.set)
ML_WasRead_Mark_list.config(yscrollcommand=scrollbar_WasRead.set)

ML_WasRead_list.bind("<MouseWheel>", on_mousewheel)
ML_WasRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

#endregion

recomendation_frame = Frame(width=696,height=675,border=0)
ttk.Label(recomendation_frame, image=recomendation_bg_img,background='#DFD0B0').place(x=0, y=0)

root.mainloop()