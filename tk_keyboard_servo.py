from tkinter import Tk
import RPi.GPIO as GPIO

servo = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

servo_pwm = GPIO.PWM(servo, 50)
servo_pwm.start(7)

def on_close():
    print('Quitting Program...')
    servo_pwm.stop()
    GPIO.cleanup()
    root.destroy()
    
def key_input(event):
    if event.char == 'a':
        print('a pressed')
        servo_pwm.ChangeDutyCycle(12.5)
    elif event.char == 's':
        print('s pressed')
        servo_pwm.ChangeDutyCycle(9.2)
    elif event.char == 'd':
        print('d pressed')
        servo_pwm.ChangeDutyCycle(5.8)
    elif event.char == 'f':
        print('f pressed')
        servo_pwm.ChangeDutyCycle(2.5)
    elif event.char == 'q':
        on_close()
    else:
        print('Invalid Input')
        
root = Tk()
root.bind('<KeyPress>', key_input)
root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()