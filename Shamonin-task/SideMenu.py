import tkinter as tk
from PIL import Image, ImageTk

class SideMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="gray")  # Установите нужную ширину в пикселях
        self.controller = controller

        canvas = tk.Canvas(self)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Загружаем изображение
        img = Image.open("backgrond2.png")
        photo = ImageTk.PhotoImage(img)

        # Размещаем изображение на Canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # Сохраняем ссылку на изображение, чтобы избежать его удаления сборщиком мусора

        self.button1_img = ImageTk.PhotoImage(Image.open("backgrond2.png"))
        self.button2_img = ImageTk.PhotoImage(Image.open("backgrond2.png"))

        # Создаем кнопки с изображением
        button1 = tk.Button(self, image=self.button1_img, command=lambda: self.controller.show_frame("MyLibrary"),
                            border=0, relief='flat')
        button2 = tk.Button(self, image=self.button2_img, command=lambda: self.controller.show_frame("PageTwo"),
                            border=0, relief='flat')

        # Получаем размеры изображений
        button1_width, button1_height = self.button1_img.width(), self.button1_img.height()
        button2_width, button2_height = self.button2_img.width(), self.button2_img.height()

        # Размещаем кнопки на холсте
        canvas.create_window(133 + button1_width / 2, 118 + button1_height / 2, anchor=tk.CENTER, window=button1)
        canvas.create_window(133 + button2_width / 2, 293 + button2_height / 2, anchor=tk.CENTER, window=button2)


