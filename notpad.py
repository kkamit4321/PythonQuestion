from tkinter import *
from tkinter import ttk
win=Tk()
win.title("notepad")
# def file():
#     print("this is my file")
# win.rowconfigure(0,minsize=400)
# win.columnconfigure(1,minsize=400)
lbl1=Label(win,text="File")
lbl1.place(x=0, y=0)
lbl2=Label(win,text="Edit")
lbl2.place(x=30,y=0)
lbl1=Label(win,text="Format")
lbl1.place(x=60, y=0)
lbl2=Label(win,text="View")
lbl2.place(x=105,y=0)
lbl1=Label(win,text="Help")
lbl1.place(x=135, y=0)
win.mainloop()