from tkinter import *
from tkinter import ttk
import Book
from Achievement import Achivement

achivements_list = [
    "Completed 10 books",
    "Reached 100 reading hours",
    "Received Reader of the Month award"
]

Library = [Book.Book('0NchAwAAQBAJ'),Book.Book('fIyWTKDlMnAC'),Book.Book('86xhAwAAQBAJ'),
           Book.Book('0NchAwAAQBAJ'),Book.Book('fIyWTKDlMnAC'),Book.Book('86xhAwAAQBAJ')]

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
achivement_bg_img = PhotoImage(file="LibNote вёрстка/Group 52.png")
#endregion

background = ttk.Label(image=background_img)
background.place(x=0, y=0)


def show_frame(frame):
       my_library_frame.place_forget()
       recomendation_frame.place_forget()
       achivement_frame.place_forget()
       frame.place(x=328,y=47)

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
       bg="#C4AF72",activebackground="#C4AF72",
       command=lambda: show_frame(achivement_frame)).place(x=133,y=466)

Button(menu_frame,image=voice_button_img,border=0,
       bg="#C4AF72",activebackground="#C4AF72").place(x=128,y=644)
#endregion

#region Моя библиотека

my_library_frame = Frame(width=696,height=675,border=0)
ttk.Label(my_library_frame, image=my_library_bg_img,background='#DFD0B0').place(x=0, y=0)
my_library_frame.place(x=328,y=47)
ML_read_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat", 20, "normal"), fg="#46402F",
                       selectbackground='#70AC9F')

# Добавление книг в "читаю"
if len(Library) == 0:
    ML_read_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(Library, start=1):
        truncated_text = f"{index}. {book.get_title()[:29]}..." if len(book.get_title()) > 29 else f"{index}. {book.get_title()}"
        ML_read_list.insert(END, truncated_text)

# Создание экземпляра класса Achivement
achivements = Achivement(*achivements_list)

# Отображение списка достижений на achivement_frame
# achivements.display_achivements(achivement_frame)

#todo Добавить сроклл бар для библиотеки

ML_read_list.place(x=99, y=76, width=449,height=160)

#endregion

recomendation_frame = Frame(width=696,height=675,border=0)
ttk.Label(recomendation_frame, image=recomendation_bg_img,background='#DFD0B0').place(x=0, y=0)

achivement_frame = Frame(width=696,height=675,border=0)
ttk.Label(achivement_frame, image=achivement_bg_img,background='#DFD0B0').place(x=0, y=0)

root.mainloop()