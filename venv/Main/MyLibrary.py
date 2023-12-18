import tkinter as tk
from PIL import Image, ImageTk

class MyLibrary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="light gray")
        self.controller = controller

        # Верхняя надпись "Моя библиотека"
        label_top = tk.Label(self, text="Моя библиотека", font=("Helvetica", 16), bg="light gray")
        label_top.pack(padx=50, pady=10, anchor='n')  # 'n' - север, для размещения сверху

        # Фрейм для списка пунктов
        options_frame = tk.Frame(self, bg="lightblue")  # Изменен цвет фрейма с пунктами
        options_frame.pack(padx=50, pady=(0, 50), fill='both', expand=True)  # Заполнение всего доступного пространства

        # Список пунктов с пустыми строками между ними
        planned = tk.Label(options_frame, text="Запланировано", bg="lightblue", font=("Helvetica", 18, "bold"))
        planned.pack(padx=10, pady=5, anchor='w')  # 'w' - запад, для размещения слева

        empty_line1 = tk.Label(options_frame, text="", bg="lightblue", height=1)
        empty_line1.pack()

        postponed = tk.Label(options_frame, text="Отложил", bg="lightblue", font=("Helvetica", 18, "bold"))
        postponed.pack(padx=10, pady=5, anchor='w')

        empty_line2 = tk.Label(options_frame, text="", bg="lightblue", height=1)
        empty_line2.pack()

        rating = tk.Label(options_frame, text="Оценка", bg="lightblue", font=("Helvetica", 18, "bold"))
        rating.pack(padx=10, pady=5, anchor='w')

        empty_line3 = tk.Label(options_frame, text="", bg="lightblue", height=1)
        empty_line3.pack()

        reading = tk.Label(options_frame, text="Читаю", bg="lightblue", font=("Helvetica", 18, "bold"))
        reading.pack(padx=10, pady=5, anchor='w')


