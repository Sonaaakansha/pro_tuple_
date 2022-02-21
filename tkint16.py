from tkinter import *
import tkinter .messagebox as tmsg
root = Tk()
root.title("pycharm")
root.geometry("623x345")


def myfunc():
    print("this is an tkinter software in laptop")

def help():
    print("I Will Help You")
    tmsg.showinfo("Help","Harry will help you with this gui")

def rate():
    print("rate us")
    value=tmsg.askquestion("How was your Experience?")
    print(value)
    if value== "yes":
        msg="Great.Rate us on appstore please"
    else:
        msg="Tell us what went wrong. we will call you soon"
        tmsg.showinfo("Experience",msg)

def divya():
            ans=tmsg.askretrycancel("Be friend of divya","sorry divya be not be your friend")
            if ans:
                print("retry")
            else:
                    print("good to be cancel")

# mymenu= Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="menu", menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="befriend divya",command=divya)
mainmenu.add_cascade(label="Help",menu=m3)

root.config(menu=mainmenu)
root.mainloop()
