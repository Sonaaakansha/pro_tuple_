from tkinter import *
def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
root= Tk()
root.geometry()
root.title("Status bar tutorial ")
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN ,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()