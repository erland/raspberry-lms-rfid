# raspberry-lms-rfid
RFID trigger for LMS based on Raspberry Pi

# Hardware
- Raspberry Pi Model B Rev 2
- YARONGTECH USB RFID Reader 125KHZ EM4100

# Installation
- Setup locale: sudo localedef -i en_US -f UTF-8 en_US.UTF-8
- Install Python libraries
  - sudo apt-get install python3-evdev
  - sudo apt-get install python3-requests
- Get id of RFID reader
  - ls /dev/input/by-id/
  - Adjust the id InputDevice row in lms_rfid.py to the identity from the above output
- Configure LMS IP
  - Run the following command but change 192.168.0.123 to your LMS server IP-address
    - sed -i s/LMS_IP_ADDRESS/192.168.0.123/ lms_rfid.py
- Install as service
  - sudo mkdir /usr/src/lms_rfid
  - sudp cp lms_rfid.py /usr/src/lms_rfid/.
  - sudo cp lms_rfid.service /lib/systemd/system/.
  - chmod 644 /lib/systemd/system/lms_rfid.service
  - sudo systemctl daemon-reload
  - sudo systemctl enable lms_rfid.service
  - sudo systemctl start lms_rfid.service
- Install RFID Play plugin in LMS
  - https://github.com/erland/lms-rfidplay

