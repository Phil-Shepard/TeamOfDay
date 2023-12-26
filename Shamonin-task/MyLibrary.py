import tkinter as tk
from PIL import Image, ImageTk

class MyLibrary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Создаем Canvas для размещения фона
        canvas = tk.Canvas(self)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Загружаем изображение
        img = Image.open("backgrond2.png")
        photo = ImageTk.PhotoImage(img)

        # Размещаем изображение на Canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # Сохраняем ссылку на изображение, чтобы избежать его удаления сборщиком мусора

        # Ваш код интерфейса добавляется над фоновым изображением
        label = tk.Label(canvas, text="Страница 1", font=("Helvetica", 16))
        label.place(x=50, y=50)  # Установите абсолютные координаты x и y


