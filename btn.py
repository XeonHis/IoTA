import RPi.GPIO as GPIO
import time
from open import open_door

def btn_press():
    btn_pin = 26
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    if GPIO.input(btn_pin) == 0:
        print('press open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        open_door()
        with open('/home/pi/ZYDEMO/iota/open_detail.txt', 'a') as log_fp:
            log_fp.write('button open at ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
            log_fp.flush()
        time.sleep(2)