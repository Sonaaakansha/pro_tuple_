from tkinter import *
root =Tk()

root.geometry("655x444")
root.title("CodeWithHarry-title of mhy GUI")
root.wm_iconbitmap()
root.configure(background="gray")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close",command=root.destroy).pack()
root.mainloop()