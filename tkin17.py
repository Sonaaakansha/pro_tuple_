from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry()
root.title("Radiobutton tutorial")
def order():
    tmsg.showinfo("Order Recived!",f"we have recived your order for{var.get()}.thanks for ordering")
#var=IntVar()
var=StringVar()
var.set("Radio")
#var.set(1)
Label(root,text="what would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Idaly",padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="Kachori",padx=14,variable=var,value=5).pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value=5).pack(anchor="w")
Button(text="Order Now",command=order).pack()
root.mainloop()
