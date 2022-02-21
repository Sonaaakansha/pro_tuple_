exit()
from tkinter import *
def update():
    print("Updating the gui")
    root.geometry(f"{width.get()}*{width.get()}")
    root=Tk()
    root.geometry()
    Label(text="Width:",font="comicsansms 11").grid(row=1,column=1)

    Label(text="Height:", font="comicsansms 11").grid(row=2, column=1)

    width=StringVar()
    height=StringVar()
    width_entry = Entry(root, textvariable=width).grid(row=1, column=2)
    height_entry = Entry(root, textvariable=height).grid(row=2, column=2)
    Button(root, text="Apply", command=resize, pady=2, font="comicsansms 11").grid(column=2)

    Entry(root,textvariable=width).pack()
    Entry(root,textvariable=height).pack()
    Button(root,text="Apply",command=update).pack()
    root.mainloop()