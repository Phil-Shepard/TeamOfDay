import tkinter as tk

class Achievements(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        # Ваш код интерфейса для страницы 2

        label = tk.Label(self, text="Страница 21331232", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)