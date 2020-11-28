import RPi.GPIO as GPIO
import time
from open import open_door
# from ultrasonic import distance
import camera_servo
import nfc
import threading
import btn
import subprocess


def check_camera():
    camera_flag = str(subprocess.Popen(['ps -a | grep mjpg'], stdout=subprocess.PIPE, shell=True).communicate()[0],
                      encoding='utf8')
    if camera_flag == '':
        subprocess.Popen(['sh /home/pi/start/camera/640_480@15.sh'], stdout=subprocess.PIPE, shell=True)
        print("camera is not opened, now open at ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(5)
    else:
        print("camera is opened")


def main():
    check_camera()
    print("door monitor start at ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    nfc_thread = threading.Thread(target=nfc.nfc)
    btn_thread = threading.Thread(target=btn.btn_press)
    camera_thread = threading.Thread(target=camera_servo.start_camera)

    nfc_thread.start()
    btn_thread.start()
    camera_thread.start()

    nfc_thread.join()
    btn_thread.join()
    camera_thread.join()


# with open('/home/pi/ZYDEMO/iota/open_detail.txt', 'a') as fp:
#     while True:
# camera_servo.start_camera()
# time.sleep(1)
# btn_pin = 26
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# nfcid = nfc.nfc()
# nfc_flag = nfc.check(nfcid)
# if nfc_flag:
#     print('nfc open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     open_door()
#     fp.write('nfc ' + nfcid + ' open at ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
#     fp.flush()
#     time.sleep(2)
# if GPIO.input(btn_pin) == 0:
#     print('press open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     open_door()
#     fp.write('button open at ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
#     fp.flush()
#     time.sleep(2)

# if camera_servo.start_camera():
#     print('face open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     open_door()
# if distance() < 20:
#     print('ultrasonic open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     open_door()

if __name__ == '__main__':
    main()
