import RPi.GPIO as GPIO
import time
from open import open_door
# from ultrasonic import distance
import camera_servo
import nfc

print("door monitor start at ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
with open('/home/pi/ZYDEMO/iota/open_detail.txt', 'a') as fp:
    while True:
        # camera_servo.start_camera()
        time.sleep(1)
        btn_pin = 26
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # nfcid = nfc.nfc()
        # nfc_flag = nfc.check(nfcid)
        # if nfc_flag:
        #     print('nfc open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #     open_door()
        #     fp.write('nfc ' + nfcid + ' open at ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
        #     fp.flush()
        #     time.sleep(2)
        if GPIO.input(btn_pin) == 0:
            print('press open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            open_door()
            fp.write('button open at ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
            fp.flush()
            time.sleep(2)

        # if camera_servo.start_camera():
        #     print('face open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #     open_door()
        # if distance() < 20:
        #     print('ultrasonic open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #     open_door()
