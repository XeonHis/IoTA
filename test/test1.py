from pynfc import Nfc, Desfire, Timeout, TimeoutException

n = Nfc("pn532_uart:/dev/ttyUSB0:115200")

DESFIRE_DEFAULT_KEY = b'\x00' * 8
MIFARE_BLANK_TOKEN = b'\xFF' * 1024 * 4

for target in n.poll():
    try:
        print(target.uid, target.auth(DESFIRE_DEFAULT_KEY if type(target) == Desfire else MIFARE_BLANK_TOKEN))
    except TimeoutException:
        pass