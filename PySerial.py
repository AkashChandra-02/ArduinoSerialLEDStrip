#!/usr/bin/env python
# coding: utf-8

# Use python -m serial.tools.list_ports to see what COM ports are open.

# In[41]:


import serial

import time

import serial.tools.list_ports

MAX_LED = 12

BRIGHTNESS = 0


# In[75]:


def checkCmd(cmd):
    cmd = cmd.upper()
    
    if(cmd == "CLS"):
        return True
    
    elif(cmd.find("I") == -1 or cmd.find("L") == -1 or cmd.find("R") == -1 or 
       cmd.find("G") == -1 or cmd.find("B") == -1):
        return False
    
    else: 
        index = int(cmd[1:cmd.find("L")])
        luminous = int(cmd[cmd.find("L")+1:cmd.find("R")]) 
        red = int(cmd[cmd.find("R")+1:cmd.find("G")])
        green = int(cmd[cmd.find("G")+1:cmd.find("B")])
        blue = int(cmd[cmd.find("B")+1:])
        
        if(0 <= index and index <= MAX_LED and 0 <= luminous and luminous <= 255 and 
           0 <= red and red <= 255 and 0 <= green and green <= 255 and 0 <= blue and blue <= 255):
            return True
        else:
            return False
        
def sendCmd(cmd, port):
    if(cmd == "CLS"):
        port.write(str.encode(cmd))
        port.write(str.encode("I10L0R0G0B0"))
    else:
        port.write(str.encode(cmd))
        
def testLEDs(num, port):
    for i in range(num):
        cmd = "I" + str(i) + "L50R100G100B100"
        if(checkCmd):
            sendCmd(cmd, port)
            print("LED " + str(i) + " is on")
            time.sleep(.5)
            sendCmd("CLS", port)
        else:
            print(cmd + " FAILED")
            
def openCOMPort(portNum):
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = portNum
    ser.open()
    return ser, ser.is_open

def closeCOMPort(port):
    port.close()
    return (not (port.is_open))

def listCOMPorts():
    ports = serial.tools.list_ports.comports()
    portName = [p.name for p in ports]
    return portName


# In[ ]:


BRIGHTNESS = input("Please put in a brightness for the LEDS:\n")
print("The set brightness is " + BRIGHTNESS)


# In[ ]:




