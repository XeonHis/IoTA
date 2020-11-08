from adafruit_pn532.uart import PN532_UART
import busio
import serial
import board
import time

# uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=100)
uart = serial.Serial("/dev/ttyUSB0",baudrate=115200)
pn532 = PN532_UART(uart, debug=False)

ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
pn532.SAM_configuration()

print("Waiting for RFID/NFC card...")
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    print(".", end="")
    # Try again if no card is available.
    if uid is not None:
        print("Found card with UID:", [hex(i) for i in uid])
    pn532.power_down()
    time.sleep(1.0)
