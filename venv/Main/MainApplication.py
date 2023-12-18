import tkinter as tk
from SideMenu import SideMenu
from MyLibrary import MyLibrary
from PageTwo import PageTwo
from Achievements import Achievements

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Мое приложение")

        # Полноэкранный режим
        self.attributes('-fullscreen', True)

        # Боковое меню
        side_menu = SideMenu(self, self)
        side_menu.pack(side="left", fill="y")

        # Основной контейнер для страниц
        container = tk.Frame(self)
        container.pack(side="right", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MyLibrary, PageTwo, Achievements):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MyLibrary")

    def show_frame(self, page_name):
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise()
        else:
            print(f"Страницы с именем {page_name} не существует.")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
