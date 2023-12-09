import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk


def search_books():
    query = entry.get().lower()  # Получаем текст из поля ввода и приводим к нижнему регистру

    if query:  # Проверяем, есть ли текст в поле запроса
        result_text.delete('1.0', tk.END)  # Очищаем текстовое поле для вывода результатов

        with open('books.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.lower().startswith(query):  # Проверяем, начинается ли строка с введенных символов
                    result_text.insert(tk.END, line)  # Выводим


def create_search_window():
    search_window = tk.Tk()
    search_window.title("Поиск книг")

    # Поле для ввода запроса
    global entry
    entry = tk.Entry(search_window, font=("Arial", 14))
    entry.pack(padx=20, pady=10)

    # Кнопка для запуска поиска
    search_button = tk.Button(search_window, text="Искать", command=search_books, font=("Arial", 14))
    search_button.pack(padx=20, pady=10)

    # Текстовое поле для вывода результатов
    global result_text
    result_text = tk.Text(search_window, font=("Arial", 12), height=10, width=50)
    result_text.pack(padx=20, pady=10)

    search_window.mainloop()


# Вызываем функцию для создания окна с поиском книг



def open_reader():
    reader_window = tk.Toplevel()
    reader_window.title("Читалка")
    reader_window.geometry("1920x1080")

    label = tk.Label(reader_window, text="Читалка", font=("Arial", 24))
    label.pack(padx=50, pady=100)

def open_book_card():
    print("Открыть карточку книги")

def open_recommendations():
    reader_window = tk.Toplevel()
    reader_window.title("Рекомендации")
    reader_window.geometry("1920x1080")
    reader_window.state('zoomed')

    label = tk.Label(reader_window, text="Рекомендации", font=("Arial", 24))
    label.pack(padx=50, pady=100)

def open_achievements():
    reader_window = tk.Toplevel()
    reader_window.title("Достижения")
    reader_window.geometry("1920x1080")
    reader_window.state('zoomed')

    label = tk.Label(reader_window, text="Ваши достижения:", font=("Arial", 24))
    label.pack(padx=50, pady=100)

def open_your_library():
    create_search_window()

def run_layout():
    root = tk.Tk()
    root.title("Моя библиотека")
    root.geometry("1024x768")
    root.state('zoomed')

    # Запрещаем автоматическое растягивание основного окна
    root.pack_propagate(False)

    # Создаем фон
    background_image = Image.open("backgrond2.png")
    background_image = background_image.resize((1920, 1080), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Создаем изображение
    image = Image.open("LibraryIcon.png")
    image = image.resize((140, 140), Image.ANTIALIAS)  # Измените размер изображения на нужный
    photo = ImageTk.PhotoImage(image)

    # Создаем виджет-кнопку поверх изображения
    invisible_button = tk.Button(root, command=create_search_window, bd=0, relief="flat", highlightthickness=0)
    invisible_button.place(x=150, y=79)  # Укажите координаты для размещения кнопки
    invisible_button.config(image=photo, width=140, height=140)

    # Создаем изображение
    image1 = Image.open("AchiveIcon.png")
    image1 = image1.resize((140, 140), Image.ANTIALIAS)  # Измените размер изображения на нужный
    photo1 = ImageTk.PhotoImage(image1)

    # Создаем виджет-кнопку поверх изображения
    invisible_button1 = tk.Button(root, command=open_achievements, bd=0, relief="flat", highlightthickness=0)
    invisible_button1.place(x=150, y=505.5)  # Укажите координаты для размещения кнопки
    invisible_button1.config(image=photo1, width=140, height=140)

    # Создаем изображение
    image2 = Image.open("RecIcon.png")
    image2 = image2.resize((140, 140), Image.ANTIALIAS)  # Измените размер изображения на нужный
    photo2 = ImageTk.PhotoImage(image2)

    # Создаем виджет-кнопку поверх изображения
    invisible_button2 = tk.Button(root, command=open_recommendations, bd=0, relief="flat", highlightthickness=0)
    invisible_button2.place(x=150, y=300)  # Укажите координаты для размещения кнопки
    invisible_button2.config(image=photo2, width=140, height=140)

    root.mainloop()

def main():
    run_layout()

if __name__ == "__main__":
    main()