import tkinter as tk
from PIL import Image, ImageTk

class SideMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="gray", width=250)  # Увеличиваем ширину боковой панели
        self.controller = controller

        # Создаем кнопки с цветом фона, увеличенным текстом и кнопками
        button1 = tk.Button(self, text="Моя библиотека", command=lambda: self.controller.show_frame("MyLibrary"),
                            bg="light gray", relief='flat', font=("Helvetica", 12))
        button2 = tk.Button(self, text="Рекомендации", command=lambda: self.controller.show_frame("PageTwo"),
                            bg="light gray", relief='flat', font=("Helvetica", 12))
        button3 = tk.Button(self, text="Достижения", command=lambda: self.controller.show_frame("Achievements"),
                            bg="light gray", relief='flat', font=("Helvetica", 12))
        button4 = tk.Button(self, text="Голосовой помощник", command=lambda: self.controller.show_frame("VoiceAssistant"),
                            bg="light gray", relief='flat', font=("Helvetica", 12))
        close_button = tk.Button(self, text="Закрыть приложение", command=self.close_app,
                            bg="light gray", relief='flat', font=("Helvetica", 12))

        # Размещаем кнопки на боковой панели
        button1.pack(pady=15, padx=10, fill=tk.X)
        button2.pack(pady=15, padx=10, fill=tk.X)
        button3.pack(pady=15, padx=10, fill=tk.X)
        button4.pack(pady=15, padx=10, fill=tk.X)
        close_button.pack(pady=15, padx=10, fill=tk.X, side=tk.BOTTOM)

    def close_app(self):
        self.controller.destroy()  # Закрыть окно приложения


