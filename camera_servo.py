# coding = utf-8
import face_recognition
import cv2
import RPi.GPIO as GPIO
import time
from face_rec import face_rec
from open import open_door


def setServoAngle(servo, angle):
    '''
    :param servo 控制舵机的引脚编号，这取决于你，我用的分别是17和27
    :param angle 舵机的位置，范围是：0到180，单位是度
    return: None
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 2.
    pwm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.3)
    pwm.stop()
    GPIO.cleanup()


# x0, y0 = 80, 0
# setServoAngle(18, x0)  # x axis
# setServoAngle(17, y0)  # y axis

def start_camera():
    # while True:
    # 创建视频对象，打开摄像头
    video_capture = cv2.VideoCapture('http://192.168.123.122:8080/?action=stream')
    ret, pframe = video_capture.read()
    # print(ret,'image capture')
    # 释放视频对象
    # video_capture.release()
    if pframe is not None:
        frame = cv2.resize(pframe, (0, 0), fx=0.25, fy=0.25)  # 这里将分辨率缩小为1/4，故比例系数增大为4倍，现在是0.078125*4 = 0.3125
        # frame = pframe
        output = frame[:, :, ::-1]

        # 确定脸的位置
        face_locations = face_recognition.face_locations(output)
        if face_locations:
            x = (face_locations[0][1] + face_locations[0][3]) / 2
            y = (face_locations[0][0] + face_locations[0][2]) / 2
            print(x, y)  # 输出脸中心到右上顶点的水平和垂直距离
        # else:
        #     x, y = 80, 60  # 如果没有脸则让舵机保持不动，相当于脸在中央（这时的分辨率为160*120）

        # 计算出舵机应该移动的角度，正负与你舵机的安装方式有关
        # dx = (80 - x) * 0.2375
        # dy = -(y - 60) * 0.2375

        # if abs(dx) >= 3:  # 设置一个阈值，当角度大于3时，才移动，避免舵机一直在原地抖动，下同
        #     x0 += dx
        #     if x0 > 180:  # 设置界限，超出范围不再转动，下同
        #         x0 = 180
        #     elif x0 < 0:
        #         x0 = 0
        #     setServoAngle(18, x0)  # 水平方向的舵机控制
        #
        # if abs(dy) >= 3:  # 设置阈值
        #     y0 += dy
        #     if y0 > 180:
        #         y0 = 180
        #     elif y0 < 0:
        #         y0 = 0
        #     print('y0', y0)
        #     setServoAngle(17, y0)  # 垂直方向的舵机控制

        flag = face_rec(video_capture, output, face_locations)
        # print(flag)
        return flag
        # if flag is True:
        # open_door()
        # print('face open at ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
