import socket
import RPi.GPIO as GPIO
import time

red = 13
green = 19
blue = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

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
    elif button == 'BTN_OK':
        print('Program Exiting...')
        led_update(0,0,0)
        GPIO.cleanup()
        raise SystemExit()
    else:
        print('Button not recognized')
        led_update(0,0,0)