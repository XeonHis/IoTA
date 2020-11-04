import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
tilt_pin = 27
GPIO.setup(tilt_pin, GPIO.OUT)
tilt = GPIO.PWM(tilt_pin, 50)
tilt.start(0)
tilt.ChangeDutyCycle(2.5)
tilt.ChangeDutyCycle(0)

# while True:
#     tilt.ChangeDutyCycle(2.5)
#     tilt.ChangeDutyCycle(7.5)
#     tilt.ChangeDutyCycle(12.5)

# tilt.stop()
# GPIO.cleanup()
