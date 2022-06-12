from tkinter import *

root = Tk()
root.title("calculator")
root.geometry("200x300")



def clicked(num):
    curr=txtField.get()
    txtField.delete(0, END)
    txtField.insert(0, str(curr)+ str(num))

def clear():
    txtField.delete(0, END)
def add():
    num1=txtField.get()
    global fnum
    fnum=int(num1)
    txtField.delete(0, END)
def equal():
    seconNum=int(txtField.get())
    txtField.delete(0, END)
    txtField.insert(0, str(fnum+seconNum))
    return

txtField=Entry(root, width=35, borderwidth=5)
txtField.place(x=0, y=0)

btn1=Button(root, text="1", pady=15, padx=15, command=lambda: clicked(1)).place(x=1, y=25)
btn2=Button(root, text="2", pady=15, padx=15, command=lambda: clicked(2)).place(x=45, y=25)
btn3=Button(root, text="3", pady=15, padx=15, command=lambda: clicked(3)).place(x=90, y=25)
btn4=Button(root, text="4", pady=15, padx=15, command=lambda: clicked(4)).place(x=1, y=80)
btn5=Button(root, text="5", pady=15, padx=15, command=lambda: clicked(5)).place(x=45, y=80)
btn6=Button(root, text="6", pady=15, padx=15, command=lambda: clicked(6)).place(x=90, y=80)
btn7=Button(root, text="7", pady=15, padx=15, command=lambda: clicked(7)).place(x=1, y=135)
btn8=Button(root, text="8", pady=15, padx=15, command=lambda: clicked(8)).place(x=45, y=135)
btn9=Button(root, text="9", pady=15, padx=15, command=lambda: clicked(9)).place(x=90, y=135)
btn0=Button(root, text="0", pady=15, padx=15, command=lambda: clicked(0)).place(x=1, y=190)

btnClear=Button(root, text="<", pady=15, padx=15, command=clear).place(x=45, y=190)
btnEqual=Button(root, text="=", pady=15, padx=15, command=equal).place(x=95, y=190)


btnAdd=Button(root, text="+", pady=15, padx=15, command=add).place(x=1, y=245)
btnSub=Button(root, text="-", pady=15, padx=35, command=lambda: clicked(1)).place(x=49, y=245)


root.mainloop()

