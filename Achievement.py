from tkinter import ttk


class Achivement:
    def __init__(self, *achivements):
        self.achivements = list(achivements)

    def add_achivement(self, achivement):
        self.achivements.append(achivement)

    def display_achivements(self, frame):
        for index, achivement_text in enumerate(self.achivements, start=1):
            label_text = f"{index}. {achivement_text}"
            ttk.Label(frame, text=label_text, background='#DFD0B0').place(x=10, y=30 * index)
