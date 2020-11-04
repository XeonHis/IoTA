import RPi.GPIO as GPIO
import time


def distance():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    trig, echo = 24, 23
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    # 发送高电平信号到 Trig 引脚
    GPIO.output(trig, True)

    # 持续 10 us
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start_time = time.time()
    stop_time = time.time()

    # 记录发送超声波的时刻1
    while GPIO.input(echo) == 0:
        start_time = time.time()

    # 记录接收到返回超声波的时刻2
    while GPIO.input(echo) == 1:
        stop_time = time.time()

    # 计算超声波的往返时间 = 时刻2 - 时刻1
    time_elapsed = stop_time - start_time
    # 声波的速度为 343m/s， 转化为 34300cm/s。
    distance = (time_elapsed * 34300) / 2

    GPIO.cleanup()

    return distance

# print(distance())
#
# if __name__ == '__main__':
#     try:
#         while True:
#             dist = distance()
#             print(dist)
#             print("Measured Distance = {:.2f} cm".format(dist))
#             time.sleep(1)
#
#         # Reset by pressing CTRL + C
#     except KeyboardInterrupt:
#         print("Measurement stopped by User")
#         GPIO.cleanup()
