import serial
import csv
import time
import os
from datetime import datetime

PORT = "COM4"          # Change this to your serial port
BAUD = 115200
WIDTH = 32
HEIGHT = 24
SAVE_FOLDER = "thermal_snaps"

def is_data_row(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != WIDTH:
        return False
    try:
        [float(x) for x in parts]
        return True
    except ValueError:
        return False

def parse_row(line):
    return [float(x.strip()) for x in line.split(",")]

def read_frame(ser, timeout=10):
    ser.reset_input_buffer()
    ser.write(b"snap\n")

    rows = []
    start_time = time.time()

    while time.time() - start_time < timeout:
        raw = ser.readline()
        if not raw:
            continue

        line = raw.decode("utf-8", errors="ignore").strip()
        if not line:
            continue

        print(line)

        if is_data_row(line):
            rows.append(parse_row(line))
            if len(rows) == HEIGHT:
                return rows

    raise TimeoutError(f"Only got {len(rows)} valid rows before timeout.")

def save_csv(frame, folder):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join(folder, f"thermal_{timestamp}.csv")

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(frame)

    return csv_path

def main():
    print(f"Opening {PORT} at {BAUD} baud...")

    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        time.sleep(2)

        while True:
            cmd = input("Press Enter to capture, or type q to quit: ").strip().lower()

            if cmd == "q":
                break

            try:
                frame = read_frame(ser)
                csv_path = save_csv(frame, SAVE_FOLDER)
                print(f"\nSaved: {csv_path}\n")

            except Exception as e:
                print(f"Error: {e}\n")

if __name__ == "__main__":
    main()