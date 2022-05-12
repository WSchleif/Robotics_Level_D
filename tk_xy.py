from tkinter import Tk, Canvas

def click(event):
    print("Clicked at x=", event.x," y=",event.y)
    
def on_close():
    root.destroy()
    
root = Tk()
root.protocol("WM_DELETE_WINDOW", on_close)

project = Canvas(root)
project.configure(width=300, height=300)
project.bind("<Button-1>", click)
project.pack()

root.mainloop()