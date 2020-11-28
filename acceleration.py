from mpu6050 import mpu6050
import time
import matplotlib.pyplot as plt
import numpy as np


def acceleration():
    sensor = mpu6050(0x68)
    time_dic = []
    start_time = time.time()
    # print(start_time)
    # print(start_time + 3)
    while True:
        if time.time() < (start_time + 5.1):
            # start_time = time.time()
            accelerometer_data = sensor.get_accel_data()
            time_dic.append(accelerometer_data)
            time.sleep(0.1)
            # end_time = time.time()
            # print(end_time-start_time)
            # print(time_dic)
        else:
            # print(time_dic)
            # break
            return time_dic


def data_handle(time_data):
    time_x_data = []
    time_y_data = []
    time_z_data = []

    count = len(time_data)

    for i in range(count):
        time_x_data.append(time_data[i]['x'])
        time_y_data.append(time_data[i]['y'])
        time_z_data.append(time_data[i]['z'])
    # print(time_x_data)
    # print(time_y_data)
    # print(time_z_data)
    return [count, time_x_data, time_y_data, time_z_data]


def plt_data():
    count, x_data, y_data, z_data = data_handle(acceleration())
    x_avg = sum(x_data) / count
    y_avg = sum(y_data) / count
    z_avg = sum(z_data) / count
    x = np.arange(0, count / 10, 0.1)
    y1 = np.array(x_data)
    y2 = np.array(y_data)
    y3 = np.array(z_data)

    plt.plot(x, y1, color='r', label='x_acc')
    plt.plot(x, y2, color='b', label='y_acc')
    plt.plot(x, y3, color='y', label='z_acc')

    plt.legend()

    plt.xlabel('time')
    plt.ylabel('m/s')

    plt.show()
    print('acc_avg',x_avg, y_avg, z_avg)


if __name__ == '__main__':
    plt_data()
