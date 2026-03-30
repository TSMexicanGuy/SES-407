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
        
        # Convert the collected data list into a 2D numpy array with 24 rows
        # The reshape automatically calculates columns based on total data points
        data_array = np.array(data).reshape(24, -1)
        
        # Print a label to the terminal
        print("Camera data:")
        
        # Display the 2D numpy array to the terminal so you can see the camera output
        print(data_array)
        
        # Close the serial connection to free up the COM port
        ser.close()
        
        # Return the numpy array so it can be used elsewhere in the program
        return data_array
        
    # If connection fails, catch the exception
    except:
        # Print error message to terminal
        print("could not connect to serial port")
        # Return None to indicate the function failed
        return None

# Call the function to execute it
read_IR_data()
    

    

