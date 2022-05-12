import RPi.GPIO as GPIO
import time

servo = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

servo_pwm = GPIO.PWM(servo, 50)
servo_pwm.start(7)
time.sleep(1)

servo_pwm.stop()
GPIO.cleanup()