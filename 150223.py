import tkinter as tk

win = tk.Tk()

win.geometry("400x600+1200+200")
win.minsize(400, 600)
win.maxsize(400, 600)

photo = tk.PhotoImage(file='icon.png')
win.iconphoto(True, photo)

win.config(
    bg="grey"
)

counter = 0


label_1 = tk.Label(win, text=f'Counter: {counter}')
label_1.pack()


def decrement_counter():
    global counter
    counter -= 1
    label_1["text"] = f'Counter: {counter}'


def increment_counter():
    global counter
    counter += 1
    label_1["text"] = f'Counter: {counter}'


button_1 = tk.Button(win, text="Increment counter", command=increment_counter)
button_1.pack()

button_2 = tk.Button(win, text="Decrement counter", command=decrement_counter)
button_2.pack()

win.mainloop()
