from bottle import route, run
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

@route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
    <body>
    <h1>RGB LED</h1>
    <p>Click the links below to change the LED color</p>
    <a href="/red_on">Red On</a>
    <br>
    <br>
    <a href="/red_off">Red Off</a>
    </body>
</html>
'''

@route('/red_on')
def red_on():
    GPIO.output(13, GPIO.HIGH)
    return "Red On"

@route('/red_off')
def red_off():
    GPIO.output(13, GPIO.LOW)
    return "Red Off"

run(host='10.82.27.199', port 8080)