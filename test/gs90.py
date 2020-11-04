import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT, initial=False)
p = GPIO.PWM(16, 50)  # 50HZ
p.start(0)
time.sleep(2)

for _ in range(1):
    for i in range(0, 181, 10):
        p.ChangeDutyCycle(2 + i / 18.)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.2)
    time.sleep(1)
    print("wait")
    for i in range(181, 0, -10):
        p.ChangeDutyCycle(2 + i / 18.)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.2)
