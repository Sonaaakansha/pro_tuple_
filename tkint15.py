from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry()
root.title("Slider tutorial")
def getdollar():
    print(f"we have credited{myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited!",f"we have credited{myslider2.get()}dollars to your bank account")
Label(root,text="How many dollars do you want?").pack()
myslider2= Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(34)
myslider2.pack()
Button(root,text="Get dollers!",pady=10,command=getdollar).pack()
