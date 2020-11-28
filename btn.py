import RPi.GPIO as GPIO
import time
from open import open_door

def btn_press():
    while True:
        # print('btn_start')
        btn_pin = 26
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        if GPIO.input(btn_pin) == 0:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print('press open at ', current_time)
            open_door(current_time)
            with open('/home/pi/ZYDEMO/iota/open_detail.txt', 'a') as log_fp:
                log_fp.write('button open at ' + str(current_time) + '\n')
                log_fp.flush()
            time.sleep(2)