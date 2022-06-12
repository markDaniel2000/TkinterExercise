import tkinter
from tkinter import *


root = Tk()

def add():
    num1=int(txtField1.get())
    num2=int(txtField2.get())


    sum=num1+num2
    txt = Label(root, text="The sum is: "+str(sum))
    txt.pack()

txtField1=Entry(root)
txtField1.pack()

txtField2=Entry(root)
txtField2.pack()

btn1=Button(root, text="enter", command=add, background='blue', foreground='white', activebackground="cyan")
btn1.pack()

root.mainloop()
