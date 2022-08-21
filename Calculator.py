from tkinter import *
from tkinter import messagebox

root = Tk()

def getRes():
    messagebox.showinfo(message=eval(textField.get("1.0", "end-1c")))

textField = Text(root,width=20, height=3)
getResButton = Button(root, text='Get result',command=getRes)

textField.pack()
getResButton.pack()

root.mainloop()
