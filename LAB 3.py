import serial
import time
import matplotlib.pyplot as plt
from drawnow import*

voltage = []
plt.ion()

def create_plot():
    plt.plot(voltage)
    plt.title("voltage Graph")
    plt.grid(True)
    plt.xlabel("counts")
    plt.ylabel("voltage")

data = serial.Serial('COM6', 9600)
while True:
    while data.in_waiting==0:
        pass
    data1=data.readline()
print(data1)
    




