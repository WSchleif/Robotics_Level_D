from tkinter import Tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

def on_close():
    print('Quitting Program...')
    root.destroy()
    GPIO.output(13, GPIO.LOW)
    GPIO.cleanup()
    
def key_input(event):
    if event.char == 'r':
        GPIO.output(13, GPIO.HIGH)
    elif event.char == 'q':
        on_close()
    else:
        print('Invalid Input')
        GPIO.output(13, GPIO.LOW)
        
root = Tk()
root.bind('<KeyPress>', key_input)
root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()