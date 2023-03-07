import tkinter as tk

win = tk.Tk()

win.title("Grid")

win.geometry("320x420+1200+200")
win.minsize(320, 420)
win.maxsize(320, 420)

photo = tk.PhotoImage(file='icon.png')
win.iconphoto(True, photo)

win.grid.columnconfigure(0, minsize=80)
win.grid.columnconfigure(1, minsize=80)
win.grid.columnconfigure(2, minsize=80)
win.grid.columnconfigure(3, minsize=80)

win.grid.row


class Button:
    def __init__(self, text, grid_props):
        button = tk.Button(text=text)
        button.grid(grid_props)


for i in range(4):
    btn = Button(f"BUTTON{i}", {'column': i, 'row': 0, 'minsize': 60})


win.config(
    bg="#FAFAFA"
)

win.mainloop()
