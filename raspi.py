
import serial

arduinoSerialData = serial.Serial('/dev/cu.usbmodem1421',9600)
arduinoSerialData.write(str.encode('3'))

# /dev/cu.usbmodem1421
# arduinoSerialData.write('3')