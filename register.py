import serial
import time

ser = serial.Serial('COM5')

seq_register_joycon = b'LE0000RI0100le0000ri0500AA0100aa0100LN0000RN0000'

ser.write(seq_register_joycon)
time.sleep(4)
