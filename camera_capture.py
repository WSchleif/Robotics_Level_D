import time, os
from tkinter import *

root = Tk()
root.title('Photos')

def quit():
    root.destroy()
    print('Program Exiting...')
    raise SystemExit()

def update():
    global img
    timestamp = (time.strftime('%Y-%m-%d_%h:%M:%S'))
    img_file = ('/home/pi/Pictures/%s.png' % timestamp)
    os.system('raspistill -o %s -e png -w 640 -h 480' % img_file)
    print('Image saved as %s' %img_file)
    img = PhotoImage(file='%s' % img_file)
    Label(root, image=img).grid(row=0, column=0)
    
img = PhotoImage(file='/home/pi/Pictures/init.png')
Label(root, image=img).grid(row=0, column=0)
Button(root, text='Capture', command=update).grid(row=1, column=0)
Button(root, text='Quit', command=quit).grid(row=2, column=0)

root.mainloop()