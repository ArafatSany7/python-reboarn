from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)  # <-- Frame (capital F)
frm.grid()  # place the frame in the window
ttk.Label(frm, text="Hello World").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

setx PYTHONHOME ""
setx PYTHONPATH ""
