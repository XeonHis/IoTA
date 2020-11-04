# coding = utf-8
import face_recognition
import cv2
import numpy as np
import os, sys
import time

os.chdir('/home/pi/ZYDEMO/iota')


# 创建视频对象

# 加载当前目录下名为'yht.jpg'的照片，照片里需要有且仅有一张脸，这张脸将作为认识的脸


def face_rec(video_capture, camera_get, camera_get_locations):
    # print('loading...')
    # image = face_recognition.load_image_file('yht.jpg')
    # current_location = face_recognition.face_locations(image)
    # current_encoding = face_recognition.face_encodings(image, current_location)
    # video_capture = cv2.VideoCapture('http://192.168.123.122:8080/?action=stream')
    # print(os.getcwd())
    known = np.load('ecodinglist.npy')

    # print('Capturing image.')
    # 读取一帧照片
    # ret, frame = video_capture.read()
    # 把照片缩小一点，能加快处理速度
    # frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # 将cv2用的BGR颜色转换为face_recognition用的RBG颜色
    # camera_get = frame[:, :, ::-1]

    # 获取这一帧图片里所有人脸的位置和特征值
    # camera_get_locations = face_recognition.face_locations(camera_get)
    # print('Found {} faces in image.'.format(len(camera_get_locations)))
    camera_get_encodings = face_recognition.face_encodings(camera_get, camera_get_locations)

    for i in range(len(camera_get_encodings)):
        matches = face_recognition.compare_faces(known, camera_get_encodings[i], tolerance=0.4)

        if True in matches:
            print('I see')
            cv2.imwrite(r'/home/pi/ZYDEMO/iota/img/' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ".jpg",
                        known)
            return True

# if __name__ == '__main__':
#     face_rec(None)
