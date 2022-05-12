from bottle import route, run
import RPi.GPIO as GPIO

red = 13
green = 19
blue = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def led_update(red_value,green_value,blue_value):
    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    GPIO.output(blue, blue_value)

@route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
    <body>
    <h1>RGB LED</h1>
    <p>Click the links below to change the LED color</p>
    <a href="/red_on">Red</a>
    <br>
    <a href="/green_on">Green</a>
    <br>
    <a href="/blue_one">Blue</a>
    <br>
    <br>
    <a href="/cleanup">GPIO Cleanup</a>
    </body>
</html>
'''

@route('/red_on')
def red_on():
    led_update(1,0,0)
    return "Red On"

@route('/green_on')
def green_on():
    led_update(0,1,0)
    return "Green On"

@route('/blue_on')
def blue_on():
    led_update(0,0,1)
    return "Blue On"

@route('/cleanup')
def cleanup():
    led_update(0,0,0)
    GPIO.cleanup()
    return "GPIO Cleanup Completed"

run(host='10.82.27.199', port 8080)