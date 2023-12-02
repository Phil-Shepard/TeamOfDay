import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk


def search_books():
    query = entry.get().lower()  # Получаем текст из поля ввода и приводим к нижнему регистру

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

    label = tk.Label(reader_window, text="Рекомендации", font=("Arial", 24))
    label.pack(padx=50, pady=100)

def open_achievements():
    reader_window = tk.Toplevel()
    reader_window.title("Достижения")
    reader_window.geometry("1920x1080")

    label = tk.Label(reader_window, text="Ваши достижения:", font=("Arial", 24))
    label.pack(padx=50, pady=100)

def open_your_library():
    create_search_window()

def main():
    root = tk.Tk()
    root.title("Моя библиотека")
    root.geometry("1920x1080")

    # Запрещаем автоматическое растягивание основного окна
    root.pack_propagate(False)

    # Создаем фон
    background_image = Image.open("background_image.jpg")
    background_image = background_image.resize((1920, 1080), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Полоска сверху
    top_strip = tk.Label(root, text="TeamOfDay", font=("Arial", 36, "bold"), bg="gray", fg="white", pady=20)
    top_strip.pack(fill="x")

    # Создаем фрейм для размещения кнопок
    button_frame = tk.Frame(root, bg="white")
    button_frame.pack(side="left", fill="y")

    # Создаем кнопки и помещаем их во фрейм
    reader_button = tk.Button(button_frame, text="Читалка", command=open_reader, bg="lightblue", fg="black", font=("Arial", 24))
    reader_button.pack(fill="x", padx=20, pady=10)

    # book_card_button = tk.Button(button_frame, text="Карточка книги", command=open_book_card, bg="lightgreen", fg="black", font=("Arial", 24))
    # book_card_button.pack(fill="x", padx=20, pady=10)

    recommendations_button = tk.Button(button_frame, text="Рекомендации", command=open_recommendations, bg="lightyellow", fg="black", font=("Arial", 24))
    recommendations_button.pack(fill="x", padx=20, pady=10)

    achievements_button = tk.Button(button_frame, text="Достижения", command=open_achievements, bg="lightcoral", fg="black", font=("Arial", 24))
    achievements_button.pack(fill="x", padx=20, pady=10)

    your_library_button = tk.Button(button_frame, text="Ваша библиотека", command=open_your_library, bg="lightpink", fg="black", font=("Arial", 24))
    your_library_button.pack(fill="x", padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

