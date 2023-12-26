import tkinter as tk

root = tk.Tk()

# Create a canvas
canvas = tk.Canvas(root, height=200, width=300, background="lightblue")
canvas.pack()

# Create a frame
scrollbar = tk.Scrollbar(canvas, orient="vertical",command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Add the frame to the canvas
canvas.create_window(50, 50, anchor="nw")

# Add a button to the frame
button = tk.Listbox(canvas)
button.insert(tk.END, "я качусь по миру со мной два чемодана")
button.pack(padx=20, pady=20)

root.mainloop()