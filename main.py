import random
from tkinter import *
from tkinter import ttk
import Book

root = Tk()
root.title("LibNote: твоя электронная библиотека")
root.geometry("1024x768")
root.resizable(False, False)
book_frame = Frame()

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
book_maket = PhotoImage(file="LibNote вёрстка/Моя библиотека/Карточка книги шаблон.png")
#endregion

background = ttk.Label(image=background_img)
background.place(x=0, y=0)

def on_mousewheel(event):
    return "break"

def on_closing():
    with open('UserInfo.txt', mode='w') as userInfoFile:
        userInfoFile.write(str(int(countOfLaunches)+1)+'\n')
        userInfoFile.write(' '.join([f'{book.id},{book.mark},{book.readCountOfPages}'for book in LibraryWillRead]) + '\n')
        userInfoFile.write(' '.join([f'{book.id},{book.mark},{book.readCountOfPages}'for book in LibraryNowRead]) + '\n')
        userInfoFile.write(' '.join([f'{book.id},{book.mark},{book.readCountOfPages}'for book in LibraryWasRead]) + '\n')
    root.destroy()

with open('UserInfo.txt',mode='r') as userInfoFile:
    countOfLaunches = userInfoFile.readline()
    LibraryWillRead = [Book.Book(*i.split(',')) for i in userInfoFile.readline().split()]
    LibraryNowRead = [Book.Book(*i.split(',')) for i in userInfoFile.readline().split()]
    LibraryWasRead = [Book.Book(*i.split(',')) for i in userInfoFile.readline().split()]

def show_frame(frame):
    my_library_frame.place_forget()
    recomendation_frame.place_forget()
    book_frame.place_forget()
    frame.place(x=328, y=47)

def makeFrameBook(book):
    book_frame = Frame(width=696, height=1077, border=0,)
    canvas = Canvas(book_frame, width=696, height=721, border=0)
    scrollbar = Scrollbar(book_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, width=696, height=1077, border=0)
    ttk.Label(scrollable_frame, image=book_maket,background='#DFD0B0').pack()

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    (Label(scrollable_frame, text=book.authors, font=("Montserrat Light", 24), bg="#5E9186", fg="#46402F")
     .place(relx=0.5, rely=0.05, anchor="center"))
    (Label(scrollable_frame, text=book.title.split('.')[0],font=("Montserrat Bold", 30),bg="#5E9186", fg="#46402F")
     .place(relx=0.5, rely=0.1, anchor="center"))
    (Label(scrollable_frame, text=book.authors, font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=370,y=178))
    (Label(scrollable_frame, text=book.categories[:24], font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=370, y=238))
    (Label(scrollable_frame, text=book.pageCount, font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=458, y=298))
    (Label(scrollable_frame, text=book.publishedDate, font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=460, y=358))
    #todo количество страниц должно быть изменяемым
    (Label(scrollable_frame, text=book.readCountOfPages, font=("Montserrat Regular", 16), bg="#CBBD91", fg="#46402F")
     .place(x=523, y=418))
    #todo добавить остальные параметры, вкл картинку



    canvas.place(x=0, y=0)
    scrollbar.place(x=680, y=0,height=721)
    return book_frame


def Ml_list_click_WillRead(event):
    global book_frame
    listbox = event.widget
    index = (str(listbox.curselection()).replace(",","")
             .replace("(","").replace(")",""))
    if len(index) == 0 or listbox.get(0) == "Пока тут пусто :(": return None
    book_frame = makeFrameBook(LibraryWillRead[int(index)])
    show_frame(book_frame)

def Ml_list_click_NowRead(event):
    global book_frame
    listbox = event.widget
    index = (str(listbox.curselection()).replace(",", "")
             .replace("(", "").replace(")", ""))
    if len(index) == 0 or listbox.get(0) == "Пока тут пусто :(": return None
    book_frame = makeFrameBook(LibraryNowRead[int(index)])
    show_frame(book_frame)

def Ml_list_click_WasRead(event):
    global book_frame
    listbox = event.widget
    index = (str(listbox.curselection()).replace(",", "")
             .replace("(", "").replace(")", ""))
    if len(index) == 0 or listbox.get(0) == "Пока тут пусто :(": return None
    book_frame = makeFrameBook(LibraryWasRead[int(index)])
    show_frame(book_frame)


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
ttk.Label(my_library_frame, image=my_library_bg_img,background='#DFD0B0').pack()
my_library_frame.place(x=328,y=47)

# Запланировано
ML_WillRead_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat Medium", 20), fg="#46402F",
                       selectbackground='#5E9186',selectforeground="#46402F")
ML_WillRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat Medium", 20), fg="#46402F",
                       selectbackground='#5E9186')
ML_WillRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click_WillRead(event))


if len(LibraryWillRead) == 0:
    ML_WillRead_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(LibraryWillRead,start=1):
        ML_WillRead_Mark_list.insert(END,book.mark)
        truncated_text = f"{index}. {book.title[:27]}..." if len(book.title) > 27 else f"{index}. {book.title}"
        ML_WillRead_list.insert(END, truncated_text.ljust(45))

scrollbar_willRead = Scrollbar(my_library_frame,orient="vertical")
scrollbar_willRead.config(command=lambda *args: (ML_WillRead_list.yview(*args), ML_WillRead_Mark_list.yview(*args)))

ML_WillRead_list.place(x=99, y=76, width=597,height=120)
ML_WillRead_Mark_list.place(x=590, y=76, width=30,height=120)
scrollbar_willRead.place(x=65,y=76+15,width=15,height=130-30)

ML_WillRead_list.config(yscrollcommand=scrollbar_willRead.set)
ML_WillRead_Mark_list.config(yscrollcommand=scrollbar_willRead.set)

ML_WillRead_list.bind("<MouseWheel>", on_mousewheel)
ML_WillRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

# Читаю
ML_NowRead_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat Medium", 20), fg="#46402F",
                       selectbackground='#5E9186')
ML_NowRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat Medium", 20), fg="#46402F",
                       selectbackground='#5E9186')
ML_NowRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click_NowRead(event))

if len(LibraryNowRead) == 0:
    ML_NowRead_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(LibraryNowRead,start=1):
        ML_NowRead_Mark_list.insert(END,book.mark)
        truncated_text = f"{index}. {book.title[:27]}..." if len(book.title) > 27 else f"{index}. {book.title}"
        ML_NowRead_list.insert(END, truncated_text.ljust(45))

scrollbar_NowRead = Scrollbar(my_library_frame,orient="vertical")
scrollbar_NowRead.config(command=lambda *args: (ML_NowRead_list.yview(*args), ML_NowRead_Mark_list.yview(*args)))

ML_NowRead_list.place(x=99, y=262, width=597,height=120)
ML_NowRead_Mark_list.place(x=590, y=262, width=30,height=120)
scrollbar_NowRead.place(x=65,y=262+15,width=15,height=130-30)

ML_NowRead_list.config(yscrollcommand=scrollbar_NowRead.set)
ML_NowRead_Mark_list.config(yscrollcommand=scrollbar_NowRead.set)

ML_NowRead_list.bind("<MouseWheel>", on_mousewheel)
ML_NowRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

# Прочитано

ML_WasRead_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat Medium", 20), fg="#46402F",
                       selectbackground='#5E9186')
ML_WasRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE,border=0,bg="#5E9186",
                       highlightthickness=0,font=("Montserrat Medium", 20), fg="#46402F",
                       selectbackground='#5E9186')

ML_WasRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click_WasRead(event))

if len(LibraryWasRead) == 0:
    ML_WasRead_list.insert(END, "Пока тут пусто :(")
else:
    for index, book in enumerate(LibraryWasRead,start=1):
        ML_WasRead_Mark_list.insert(END,book.mark)
        truncated_text = f"{index}. {book.title[:27]}..." if len(book.title) > 27 else f"{index}. {book.title}"
        ML_WasRead_list.insert(END, truncated_text.ljust(45))

scrollbar_WasRead = Scrollbar(my_library_frame,orient="vertical")
scrollbar_WasRead.config(command=lambda *args: (ML_WasRead_list.yview(*args), ML_WasRead_Mark_list.yview(*args)))

ML_WasRead_list.place(x=99, y=448, width=597,height=120)
ML_WasRead_Mark_list.place(x=590, y=448, width=30,height=120)
scrollbar_WasRead.place(x=65,y=448+15,width=15,height=130-30)

ML_WasRead_list.config(yscrollcommand=scrollbar_WasRead.set)
ML_WasRead_Mark_list.config(yscrollcommand=scrollbar_WasRead.set)

ML_WasRead_list.bind("<MouseWheel>", on_mousewheel)
ML_WasRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

#endregion

recomendation_frame = Frame(width=696,height=675,border=0)
ttk.Label(recomendation_frame, image=recomendation_bg_img,background='#DFD0B0').place(x=0, y=0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()