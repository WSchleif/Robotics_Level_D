from tkinter import Tk

def on_close():
    print('Quitting Program...')
    root.destroy()
    
def key_input(event):
    if event.char == 'a':
        print('a pressed')
    elif event.char == 's':
        print('s pressed')
    elif event.char == 'd':
        print('d pressed')
    elif event.char == 'f':
        print('f pressed')
    elif event.char == 'q':
        on_close()
    else:
        print('Invalid Input')
        
root = Tk()
root.bind('<KeyPress>', key_input)
root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()