import smbus
import time
import requests
import acceleration
import threading


def Print(value):
    if value == 0:
        print('no magnet')
    if value == 1:
        print('magnet north')
    if value == -1:
        print('magnet south')


def hall1():
    address = 0x48
    A0 = 0x40

    bus = smbus.SMBus(11)
    status = 0

    while True:
        bus.write_byte(address, A0)
        data = bus.read_byte(address)
        if 5 > data - 133 > -5:
            value = 0
        if data < 128:
            value = -1
        if data > 138:
            value = 1
        if value != status:
            if value != -1:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print('door opened at ', current_time)
                time_payload = '{{"open_time": "{}"}}'.format(str(current_time))
                requests.post(url='https://demo.thingsboard.io/api/v1/rL2hzO7of5BN0jk1JMuX/telemetry',
                              data=time_payload)
            # Print(value)
            status = value
        time.sleep(0.2)


def hall():
    pass


if __name__ == '__main__':
    hall()
