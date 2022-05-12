import RPi.GPIO as GPIO
import time

d1 = 21
d2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(d1, GPIO.OUT)
GPIO.(d2, GPIO.OUT)

GPIO.output(d1, GPIO.HIGH)
time.sleep(1)
GPIO.output(d1, GPIO.LOW)
GPIO.output(d2, GPIO.HIGH)
time.sleep(1)
GPIO.output(d2, GPIO.LOW)

GPIO.cleanup()