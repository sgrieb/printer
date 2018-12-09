
import serial
import sys
import time

sent = False

connection = serial.Serial('/dev/cu.usbmodem1421', 9600)

while 1:
    print("waiting 2 sec")
    if sent != True:
        time.sleep(2)
        print("sending")
        connection.write(str.encode(sys.argv[1]))
        sent = True

    serial_line = connection.readline()
    print ("Got string: " + serial_line)

# print(sys.argv.)
# arduinoSerialData.write(str.encode(sys.argv[1]))