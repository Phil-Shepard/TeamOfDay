import tkinter as tk
from PIL import Image, ImageTk


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
    reader_window = tk.Toplevel()
    reader_window.title("Библиотека")
    reader_window.geometry("1920x1080")

    label = tk.Label(reader_window, text="Ваши книги:", font=("Arial", 24))
    label.pack(padx=50, pady=100)

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

