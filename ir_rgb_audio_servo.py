import socket
import RPi.GPIO as GPIO
import time
import os

red = 13
green = 19
blue = 26
servo = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

SOCKPATH = '/var/run/lirc/lircd'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print ('starting up on %s' % SOCKPATH)
sock.connect(SOCKPATH)

def next_key():
    while True:
        clear_socket = sock.recv(128)
        data = sock.recv(128)
        if data:
            break
    ir_data = data.split()
    btn_name = ir_data[2]
    btn_name = btn_name.decode("utf-8")
    return btn_name

def led_update(red_value,green_value,blue_value):
    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    GPIO.output(blue, blue_value)
    
servo_pwm = GPIO.PWM(servo, 50)
servo_pwm.start(7)
    
while True:
    button = next_key()
    if button == 'BTN_1':
        print('Red')
        led_update(1,0,0)
    elif button == 'BTN_2':
        print('Green')
        led_update(0,1,0)
    elif button == 'BTN_3':
        print('Blue')
        led_update(0,0,1)
    elif button == 'BTN_4':
        led_update(0,0,0)
        os.system("gpio -g mode 18 ALT5")
        os.system("aplay /home/pi/my_voice.wav")
        os.system("gpio -g mode 18 in")
    elif button == 'BTN_LEFT':
        print('Servo Left')
        led_update(0,0,0)
        servo_pwm.ChangeDutyCycle(12.5)
    elif button == 'BTN_UP':
        print('Servo Middle')
        led_update(0,0,0)
        servo_pwm.ChangeDutyCycle(7)
    elif button == 'BRN_RIGHT':
        print('Servo Right')
        led_update(0,0,0)
        servo_pwm.ChangeDutyCycle(2.5)
    elif button == 'BTN_OK':
        print('Program Exiting...')
        led_update(0,0,0)
        servo_pwm.stop()
        GPIO.cleanup()
        raise SystemExit()
    else:
        print('Button not recognized')
        led_update(0,0,0)