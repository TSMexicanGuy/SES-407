import serial
import time
import numpy as np

PORT = "COM4"
BAUD_RATE = 115200
print("Starting IR data reader...")

#reads the data from the IR sensor and returns it as a numpy array
def read_IR_data():
   
   #trys ro connect to serial port
    try:
        ser = serial.Serial(PORT, BAUD_RATE,timeout=1)
        print("great success, we have connection!!")
        #send snap command to itsybitsy
        ser.write(b'snap\n')
        time.sleep(1)
        data = []
        for i in range(24):  # Loop 24 times for 24 rows
            line = ser.readline().decode('utf-8').strip()
            if line:  # Only process non-empty lines
                values = line.split(',')
                # Convert each value to float and add to data list
                data.extend([float(v) for v in values if v])



#if it cant, prints error message and returns nothing
    except:
        print("could not connect to serial port")
        return None
    

