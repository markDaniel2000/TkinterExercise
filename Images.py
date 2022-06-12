from tkinter import *
from PIL import ImageTk, Image

main_window=Tk()
main_window.title("Photo Browser")

img1=ImageTk.PhotoImage(Image.open("images/images.jpg"))
img2=ImageTk.PhotoImage(Image.open("images/download.jpg"))
img3=ImageTk.PhotoImage(Image.open("images/images (1).jpg"))

photoList=[img1, img2, img3]

imgNum=0

def next():
    global imgNum

    if imgNum<=len(photoList):
        imgNum+=1
        lbl.grid_forget()
        lbl1= Label(main_window, image=photoList[imgNum])
        lbl1.grid(row=0, column=0, columnspan=3)
    else:
        btnNext["state"] = DISABLED
def prev():
    global imgNum

    if imgNum >= 1:
        imgNum -= 1
        lbl.grid_forget()
        lbl1 = Label(main_window, image=photoList[imgNum])
        lbl1.grid(row=0, column=0, columnspan=3)
    else:
        btnPrev["state"] = DISABLED


lbl=Label(main_window, image=photoList[imgNum])
lbl.grid(row=0, column=0, columnspan=3)

btnNext=Button(main_window, text="next", padx=5, pady=3, command=next)
btnNext.grid(row=1,column=2)
btnPrev=Button(main_window, text="prev", padx=5, pady=3, command=prev)
btnPrev.grid(row=1,column=0)
btnExit=Button(main_window, text="exit", padx=10, pady=3, command=main_window.quit)
btnExit.grid(row=1,column=1)




main_window.mainloop()