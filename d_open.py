import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
tilt_pin = 27
GPIO.setup(tilt_pin, GPIO.OUT)
tilt = GPIO.PWM(tilt_pin, 50)
tilt.start(0)
time.sleep(0.2)
tilt.ChangeDutyCycle(12.5)
time.sleep(2)
tilt.ChangeDutyCycle(2.5)
time.sleep(2)
tilt.ChangeDutyCycle(0)
time.sleep(0.5)
tilt.stop()
GPIO.cleanup()
