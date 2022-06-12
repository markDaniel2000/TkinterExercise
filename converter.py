from tkinter import *





root = Tk() #declare the window

def myClick():
    myLabel1=Label(root, text="daniel")
    myLabel1.pack()

#label widget
myLabel = Label(#declare a widget
    root, #put the widget on the root
    text="Hello World") #possible code myLabel1=Label(root, text="My name is Daniel").grid(row=2, column=2) same output
myLabel.pack() #Position Widgets using pack(), place() or grid()

Btn1=Button(root, #put the widget on the root
            text="clicked", #name of the button display in the window
            state=NORMAL, #Tkinter button has two states: normal and disabled
            padx=9,#change size using padx and pady
            pady=12,
            command=myClick
            )
Btn1.pack()




root.mainloop() #loop the the main window

