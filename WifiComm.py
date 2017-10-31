# -*- coding: utf-8 -*-
import time
from arserial import ArSerial


timer = time.time()  # Timer to see when we started

repeatTime=3
with ArSerial() as Uart1:

    Uart1.baudrate = 9600
    Uart1.bytesize = 8 #serial.EIGHTBITS
    Uart1.parity = 'N' #serial.PARITY_NONE
    Uart1.stopbits = 1 #serial.STOPBITS_ONE
    Uart1.timeout = 0.2
    Uart1.port = 'COM9'#ports[c].device '/dev/ttyUSB0'

    # homeWhiz_connected = bytearray([51, 0, 26, 4, 174])
    # Open = bytearray([51, 0, 34, 10, 160])
    # close = bytearray([51, 0, 34, 20, 150])
    # start = bytearray([51, 0, 34, 30, 140])
    # control = bytearray([51, 0, 30, 50, 124])
    # stop = bytearray([51, 0, 34, 40, 130])
    # wifiarray = bytearray([53, 0, 0, 0, 202])




    # homeWhiz ayar
    # Uart1.write(homeWhiz_connected)
#     time.sleep(0.2)
#     read_val = Uart1.read(size=3)


# print(Uart1.wifiArrayRead(25))
    Uart1.wifiArrayWrite(26, 4)    # homeWhiz_connected
    # print(Uart1.wifiArrayWrite(34, 10))   # Open
    # print(Uart1.wifiArrayWrite(30, 50))   # Control
    # print(Uart1.wifiArrayWrite(34, 30))   # Start
    # time.sleep(0.2)
    # print(Uart1.wifiArrayWrite(30, 50))   # Control
# time.sleep(15)
    print(Uart1.wifiArrayWrite(34, 40))   # Stop
    print(Uart1.wifiArrayWrite(30, 50))   # Control
# print(Uart1.wifiArrayWrite(34, 20))   # Close
# print(Uart1.wifiArrayWrite(30, 50))   # Control
# print(Uart1.getID())
# print(Uart1.publicArrayRead(5))
#
# print(Uart1.wifiArrayFullRead())
    while True:
        if (time.time() - timer) > repeatTime:
            print(Uart1.wifiArrayFullRead())
    Uart1.close()
