import RPi.GPIO as GPIO
import time
import requests
import acceleration
import threading


def open_door(current_time):
    open_thread = threading.Thread(target=open_door1(current_time))
    acc_thread = threading.Thread(target=acceleration.plt_data)
    open_thread.start()
    acc_thread.start()

    open_thread.join()
    acc_thread.join()


def open_door1(current_time):
    time_payload = '{{"open_time": "{}"}}'.format(str(current_time))
    requests.post(url='https://demo.thingsboard.io/api/v1/rL2hzO7of5BN0jk1JMuX/telemetry', data=time_payload)
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

    # GPIO.cleanup()
