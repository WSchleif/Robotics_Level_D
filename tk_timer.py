from tkinter import *
import time

def update():
    display.delete(0,END)
    display.insert(0, time.time())
    root.after(300, update)

root = Tk()
root.title('Timer')
Label(root, text = 'Timer: ').grid(row=0, column=0)

display = Entry(root)
display.grid(row=0, column=1)

Button(root, text='Quit', comman=root.destroy).grid(row=1, column=0)

update()
root.mainloop()