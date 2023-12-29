import random
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
import requests


import Book

root = Tk()
root.title("LibNote: твоя электронная библиотека")
root.geometry("1024x768")
root.resizable(False, False)
book_frame = Frame(root)

# region LoadImages
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
delete_book = PhotoImage(file='LibNote вёрстка/Моя библиотека/удалить книгу.png')
add_book = PhotoImage(file='LibNote вёрстка/Иконка добавить.png')
add_book_frame = PhotoImage(file='LibNote вёрстка/Моя библиотека/Добавьте книгу.png')
icon_voice_lib = PhotoImage(file="LibNote вёрстка/Моя библиотека/Иконка добавить книгу при помощи голоса.png")
voice_background = PhotoImage(file='LibNote вёрстка/Гс помощник/Голосовой помощник фон.png')
# endregion

background = ttk.Label(image=background_img)
background.place(x=0, y=0)


def on_mousewheel(event):
    return "break"


def on_closing():
    with open('UserInfo.txt', mode='w') as userInfoFile:
        userInfoFile.write(str(int(countOfLaunches) + 1) + '\n')
        userInfoFile.write(
            ' '.join([f'{book.id},{book.mark},{book.readCountOfPages}' for book in LibraryWillRead]) + '\n')
        userInfoFile.write(
            ' '.join([f'{book.id},{book.mark},{book.readCountOfPages}' for book in LibraryNowRead]) + '\n')
        userInfoFile.write(
            ' '.join([f'{book.id},{book.mark},{book.readCountOfPages}' for book in LibraryWasRead]) + '\n')
    root.destroy()


with open('UserInfo.txt', mode='r') as userInfoFile:
    countOfLaunches = userInfoFile.readline()
    LibraryWillRead = [Book.Book(*i.split(',')) for i in userInfoFile.readline().split()]
    LibraryNowRead = [Book.Book(*i.split(',')) for i in userInfoFile.readline().split()]
    LibraryWasRead = [Book.Book(*i.split(',')) for i in userInfoFile.readline().split()]

addBook_Frame = Frame()
def show_frame(frame):
    global book_frame
    global addBook_Frame
    my_library_frame.place_forget()
    recomendation_frame.place_forget()
    book_frame.place_forget()
    addBook_Frame.place_forget()
    voice_frame.place_forget()
    frame.place(x=328, y=47)


def makeFrameBook(book):
    global book_frame

    def saveReadPages():
        book.readCountOfPages = cOfp.get()

    def saveMark():
        book.mark = markBook.get()
        update_ML_WasRead()
        update_ML_NowRead()
        update_ML_WillRead()
    def deleteBook():
        show_frame(my_library_frame)
        if book in LibraryWasRead:
            ML_WasRead_list.delete(LibraryWasRead.index(book))
            ML_WasRead_Mark_list.delete(LibraryWasRead.index(book))
            LibraryWasRead.remove(book)
            update_ML_WasRead()

        elif book in LibraryWillRead:
            ML_WillRead_list.delete(LibraryWillRead.index(book))
            ML_WillRead_Mark_list.delete(LibraryWillRead.index(book))
            LibraryWillRead.remove(book)

        elif book in LibraryNowRead:
            ML_NowRead_list.delete(LibraryNowRead.index(book))
            ML_NowRead_Mark_list.delete(LibraryNowRead.index(book))
            LibraryNowRead.remove(book)

    def on_combobox_select(event):
        if book in LibraryWillRead and status.current() != 0:
            LibraryWillRead.remove(book)
            [LibraryWillRead,LibraryNowRead,LibraryWasRead][status.current()].append(book)
            status.set(['Запланировано',"Читаю","Прочитано"][status.current()])

        elif book in LibraryNowRead and status.current() != 1:
            LibraryNowRead.remove(book)
            [LibraryWillRead,LibraryNowRead,LibraryWasRead][status.current()].append(book)
            status.set(['Запланировано',"Читаю","Прочитано"][status.current()])

        elif book in LibraryWasRead and status.current() != 2:
            LibraryWasRead.remove(book)
            [LibraryWillRead,LibraryNowRead,LibraryWasRead][status.current()].append(book)
            status.set(['Запланировано',"Читаю","Прочитано"][status.current()])
        update_ML_WillRead()
        update_ML_NowRead()
        update_ML_WasRead()

    book_frame = Frame(width=696, height=1077, border=0, )
    canvas = Canvas(book_frame, width=696, height=721, border=0)
    scrollbar = Scrollbar(book_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, width=696, height=1077, border=0)
    ttk.Label(scrollable_frame, image=book_maket, background='#DFD0B0').pack()

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
    (Label(scrollable_frame, text=book.title.split('.')[0], font=("Montserrat Bold", 30), bg="#5E9186", fg="#46402F")
     .place(relx=0.5, rely=0.1, anchor="center"))
    (Label(scrollable_frame, text=book.authors, font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=370, y=178))
    (Label(scrollable_frame, text=book.categories[:24], font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=370, y=238))
    (Label(scrollable_frame, text=book.pageCount, font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=458, y=298))
    (Label(scrollable_frame, text=book.publishedDate, font=("Montserrat Regular", 16), bg="#5E9186", fg="#46402F")
     .place(x=460, y=358))
    cOfp = Entry(scrollable_frame, width=4, font=("Montserrat Regular", 16), bg="#CBBD91", fg="#46402F", border=0)
    cOfp.insert(END, book.readCountOfPages)
    cOfp.place(x=523, y=420)
    (Button(scrollable_frame, text="Сохранить", font=("Montserrat Light", 8), bg="#CBBD91", fg="#46402F", border=0, command=saveReadPages)
     .place(x=595,y=425))
    Label(scrollable_frame, image=book.icon,width=184,height=274,bg="#46402F",border=0).place(x=76,y=184)
    status = Combobox(scrollable_frame,state="readonly", values=['Запланировано',"Читаю","Прочитано"],width=14, font=("Montserrat Regular", 12), background="#CBBD91", foreground="#46402F")
    if book in LibraryWillRead: status.set('Запланировано')
    if book in LibraryNowRead: status.set("Читаю")
    if book in LibraryWasRead: status.set("Прочитано")
    status.bind("<<ComboboxSelected>>", on_combobox_select)
    status.place(x=289,y=426)

    def readBook():
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Select a TXT file"
        )

        if file_path:
            # Создаем новое окно для отображения текста
            display_window = Toplevel(root)
            display_window.title("Читалка")
            display_window.geometry("800x450")
            Label(display_window, background="#D2C2A4").pack(fill=BOTH, expand=True)

            current_page_label = Label(display_window, wraplength=750,font=("Montserrat Regular", 10), bg="#D2C2A4", fg="#46402F")
            current_page_label.place(relx=.5, rely=.5, anchor="c")
            file = open(file_path, "r")
            def next_page():
                # Читаем следующие 6 строк из файла и обновляем текст current_page_label
                current_page_label.config(text="\n".join([file.readline().strip() for _ in range(2)]))

            Button(display_window, text="Далее", command=next_page).pack()
            next_page()

        else:
            messagebox.showinfo("Info", "No file selected.")

    Button(scrollable_frame,text="Читать",font=("Montserrat Bold", 24), bg="#CBBD91", fg="#46402F", border=0,activebackground="#CBBD91",activeforeground="#46402F",command=readBook).place(x=245,y=556,width=204,height=50)

    Label(scrollable_frame,text=book.description[:1050], font=("Montserrat Regular", 10), bg="#5E9186", fg="#46402F",wraplength=550).place(x=99,y=727,width=550)

    Button(scrollable_frame,image=delete_book, bg="#5E9186", fg="#46402F", border=0,activebackground="#5E9186",activeforeground="#46402F",command=deleteBook).place(x=81,y=1025)

    markBook = Entry(scrollable_frame, width=4, font=("Montserrat Regular", 16), bg="#CBBD91", fg="#46402F", border=0)
    markBook.insert(END, book.mark)
    markBook.place(x=138, y=497)
    (Button(scrollable_frame, text="Сохранить", font=("Montserrat Light", 8), bg="#CBBD91", fg="#46402F", border=0,
            command=saveMark)
     .place(x=138, y=550))

    canvas.place(x=0, y=0)
    scrollbar.place(x=680, y=0, height=721)
    return book_frame


def Ml_list_click_WillRead(event):
    global book_frame
    listbox = event.widget
    index = (str(listbox.curselection()).replace(",", "")
             .replace("(", "").replace(")", ""))
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

def update_ML_WillRead():
    ML_WillRead_list.delete(0, END)
    ML_WillRead_Mark_list.delete(0, END)
    if len(LibraryWillRead) == 0:
        ML_WillRead_list.insert(END, "Пока тут пусто :(")
    else:
        for index, book in enumerate(LibraryWillRead, start=1):
            ML_WillRead_Mark_list.insert(END, book.mark)
            truncated_text = f"{index}. {book.title[:27]}..." if len(book.title) > 27 else f"{index}. {book.title}"
            ML_WillRead_list.insert(END, truncated_text.ljust(45))
def update_ML_NowRead():
    ML_NowRead_list.delete(0, END)
    ML_NowRead_Mark_list.delete(0, END)
    if len(LibraryNowRead) == 0:
        ML_NowRead_list.insert(END, "Пока тут пусто :(")
    else:
        for index, book in enumerate(LibraryNowRead, start=1):
            ML_NowRead_Mark_list.insert(END, book.mark)
            truncated_text = f"{index}. {book.title[:27]}..." if len(book.title) > 27 else f"{index}. {book.title}"
            ML_NowRead_list.insert(END, truncated_text.ljust(45))
def update_ML_WasRead():
    ML_WasRead_list.delete(0, END)
    ML_WasRead_Mark_list.delete(0, END)
    if len(LibraryWasRead) == 0:
        ML_WasRead_list.insert(END, "Пока тут пусто :(")
    else:
        for index, book in enumerate(LibraryWasRead, start=1):
            ML_WasRead_Mark_list.insert(END, book.mark)
            truncated_text = f"{index}. {book.title[:27]}..." if len(book.title) > 27 else f"{index}. {book.title}"
            ML_WasRead_list.insert(END, truncated_text.ljust(45))

def addBook():
    def findIdBook():
        id = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={nameAddBook.get().replace(' ', '_')}")
        if id.status_code == 200:
            id = id.json()['items'][0]['id']
            LibraryWillRead.append(Book.Book(id= id,mark='-',readCountOfPages='0'))
            update_ML_WillRead()
            show_frame(makeFrameBook(LibraryWillRead[-1]))

        else:
            print(f'Error: {id.status_code}')

    global addBook_Frame
    addBook_Frame = Frame(root,width=696, height=675)
    Label(addBook_Frame, image=add_book_frame,background='#DFD0B0').pack()
    nameAddBook = Entry(addBook_Frame, width=20,background='#5E9186',font=("Montserrat Medium", 20),foreground="#46402F")

    nameAddBook.place(x=170,y=338)

    (Button(addBook_Frame, text="Добавить", font=("Montserrat Light", 8), bg="#CBBD91", fg="#46402F", border=0,
            command=findIdBook)
     .place(x=80, y=348))

    Button(addBook_Frame, image=icon_voice_lib, bg="#5E9186", fg="#46402F", border=0,activebackground='#5E9186',activeforeground="#46402F",command=lambda: show_frame(voice_frame)).place(x=250, y=430)

    show_frame(addBook_Frame)

# region Menu
menu_frame = Frame(width=281, height=771, border=0)
menu_frame.place(x=-2, y=0)
ttk.Label(menu_frame, image=menu_img).place(x=0, y=0)

Button(menu_frame, image=my_library_button_img, border=0,
       bg="#CCB575", activebackground="#CCB575",
       command=lambda: show_frame(my_library_frame)).place(x=133, y=118)

Button(menu_frame, image=recomendation_button_img, border=0,
       bg="#C4AF72", activebackground="#C4AF72",
       command=lambda: show_frame(recomendation_frame)).place(x=133, y=293)

Button(menu_frame, image=achivement_button_img, border=0,
       bg="#C4AF72", activebackground="#C4AF72").place(x=133, y=466)

Button(menu_frame, image=voice_button_img, border=0,
       bg="#C4AF72", activebackground="#C4AF72").place(x=128, y=644)
# endregion

# region Моя библиотека

my_library_frame = Frame(width=696, height=675, border=0)
ttk.Label(my_library_frame, image=my_library_bg_img, background='#DFD0B0').pack()
my_library_frame.place(x=328, y=47)

# Запланировано
ML_WillRead_list = Listbox(my_library_frame, selectmode=SINGLE, border=0, bg="#5E9186",
                           highlightthickness=0, font=("Montserrat Medium", 20), fg="#46402F",
                           selectbackground='#5E9186', selectforeground="#46402F")
ML_WillRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE, border=0, bg="#5E9186",
                                highlightthickness=0, font=("Montserrat Medium", 20), fg="#46402F",
                                selectbackground='#5E9186')
ML_WillRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click_WillRead(event))

update_ML_WillRead()

scrollbar_willRead = Scrollbar(my_library_frame, orient="vertical")
scrollbar_willRead.config(command=lambda *args: (ML_WillRead_list.yview(*args), ML_WillRead_Mark_list.yview(*args)))

ML_WillRead_list.place(x=99, y=76, width=597, height=120)
ML_WillRead_Mark_list.place(x=590, y=76, width=30, height=120)
scrollbar_willRead.place(x=65, y=76 + 15, width=15, height=130 - 30)

ML_WillRead_list.config(yscrollcommand=scrollbar_willRead.set)
ML_WillRead_Mark_list.config(yscrollcommand=scrollbar_willRead.set)

ML_WillRead_list.bind("<MouseWheel>", on_mousewheel)
ML_WillRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

# Читаю
ML_NowRead_list = Listbox(my_library_frame, selectmode=SINGLE, border=0, bg="#5E9186",
                          highlightthickness=0, font=("Montserrat Medium", 20), fg="#46402F",
                          selectbackground='#5E9186')
ML_NowRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE, border=0, bg="#5E9186",
                               highlightthickness=0, font=("Montserrat Medium", 20), fg="#46402F",
                               selectbackground='#5E9186')
ML_NowRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click_NowRead(event))

update_ML_NowRead()

scrollbar_NowRead = Scrollbar(my_library_frame, orient="vertical")
scrollbar_NowRead.config(command=lambda *args: (ML_NowRead_list.yview(*args), ML_NowRead_Mark_list.yview(*args)))

ML_NowRead_list.place(x=99, y=262, width=597, height=120)
ML_NowRead_Mark_list.place(x=590, y=262, width=30, height=120)
scrollbar_NowRead.place(x=65, y=262 + 15, width=15, height=130 - 30)

ML_NowRead_list.config(yscrollcommand=scrollbar_NowRead.set)
ML_NowRead_Mark_list.config(yscrollcommand=scrollbar_NowRead.set)

ML_NowRead_list.bind("<MouseWheel>", on_mousewheel)
ML_NowRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

# Прочитано

ML_WasRead_list = Listbox(my_library_frame, selectmode=SINGLE, border=0, bg="#5E9186",
                          highlightthickness=0, font=("Montserrat Medium", 20), fg="#46402F",
                          selectbackground='#5E9186')
ML_WasRead_Mark_list = Listbox(my_library_frame, selectmode=SINGLE, border=0, bg="#5E9186",
                               highlightthickness=0, font=("Montserrat Medium", 20), fg="#46402F",
                               selectbackground='#5E9186')

ML_WasRead_list.bind('<<ListboxSelect>>', lambda event: Ml_list_click_WasRead(event))

update_ML_WasRead()

scrollbar_WasRead = Scrollbar(my_library_frame, orient="vertical")
scrollbar_WasRead.config(command=lambda *args: (ML_WasRead_list.yview(*args), ML_WasRead_Mark_list.yview(*args)))

ML_WasRead_list.place(x=99, y=448, width=597, height=120)
ML_WasRead_Mark_list.place(x=590, y=448, width=30, height=120)
scrollbar_WasRead.place(x=65, y=448 + 15, width=15, height=130 - 30)

ML_WasRead_list.config(yscrollcommand=scrollbar_WasRead.set)
ML_WasRead_Mark_list.config(yscrollcommand=scrollbar_WasRead.set)

ML_WasRead_list.bind("<MouseWheel>", on_mousewheel)
ML_WasRead_Mark_list.bind("<MouseWheel>", on_mousewheel)

(Button(my_library_frame,image=add_book, bg="#5E9186", fg="#46402F", border=0,activebackground='#5E9186',activeforeground="#46402F",command=addBook)
 .place(x=316,y=607))



# endregion

recomendation_frame = Frame(width=696, height=675, border=0)
ttk.Label(recomendation_frame, image=recomendation_bg_img, background='#DFD0B0').place(x=0, y=0)

voice_frame = Frame(width=696, height=675, border=0)
ttk.Label(voice_frame, image=voice_background, background='#DFD0B0').place(x=0, y=0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
