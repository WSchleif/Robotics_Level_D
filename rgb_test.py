import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(13, GPIO.HIGH)
time.sleep(1)
GPIO.output(13, GPIO.LOW)
GPIO.output(19, GPIO.HIGH)
time.sleep(1)
GPIO.output(19, GPIO.LOW)
GPIO.output(26, GPIO.HIGH)
time.sleep(1)
GPIO.output(26, GPIO.LOW)
GPIO.cleanup()