#!/usr/bin/python3

from evdev import InputDevice, ecodes, list_devices
from select import select
import requests

keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice("/dev/input/by-id/usb-16c0_27db-event-kbd")

barcode = ""
while True:
    r,w,x = select([dev], [], [])

    for event in dev.read():
        if event.type != 1 or event.value != 1:
            continue
        if event.code == 28:
            print(barcode)
            r = requests.get('http://LMS_IP_ADDRESS:9000/plugins/RFIDPlay/play/'+barcode)
            print(r.status_code)
            barcode = ""
            break
        barcode += keys[event.code]
