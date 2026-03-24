# My IR Camera Reader Script
# Let's build this step by step

# Step 1: Import the modules we need
import serial  # For talking to the serial port
import time    # For waiting (delays)
import numpy as np  # For handling the 24x32 data as an array

# Step 2: Set up constants (things that don't change)
PORT = 'COM4'        # The serial port your M4 is on (from list_ports.py)
BAUD_RATE = 9600     # Speed of communication (check your M4 code)

# Step 3: Define a function to read the IR data
def read_ir_data():
    # This function will handle connecting, sending 'snap', and reading data
    try:
        # Try to do this code
        # Open the serial connection
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        print(f"Connected to {PORT} at {BAUD_RATE} baud.")

        # Send the 'snap' command to the M4
        ser.write(b'snap\n')
        print("Sent 'snap' command.")

        # Wait a bit for the M4 to respond
        time.sleep(1)

        # Read the data
        data = []
        while ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                # Split the line by commas and convert to floats
                values = line.split(',')
                data.extend([float(v) for v in values if v])

        # Close the serial connection
        ser.close()

        # Check if we got the right amount of data (24*32 = 768)
        if len(data) == 24 * 32:
            # Reshape into 24x32 array
            thermal_data = np.array(data).reshape(24, 32)
            print("Data received and reshaped to 24x32.")
            return thermal_data
        else:
            print(f"Expected 768 values, got {len(data)}.")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Step 4: Run the function when the script is executed
if __name__ == "__main__":
    data = read_ir_data()
    if data is not None:
        print(data)