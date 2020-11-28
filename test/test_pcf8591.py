import smbus
import time


def Print(value):
    if value == 0:
        print('no magnet')
    if value == 1:
        print('magnet north')
    if value == -1:
        print('magnet south')


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
    if data != status:
        Print(value)
        status = value
    time.sleep(0.2)
