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





data = serial.Serial('COM4', 9600)
while True:
    while data.in_waiting==0:
        pass
    data1=data.readline()
    
    data2 = str(data1, 'utf-8')
    niceData = int(data2.strip('\r\n'))
    
    volts = ((5-0)/(1023-0)) * niceData
    print(volts)
    voltage.append(volts)
    drawnow(create_plot)
    plt.pause(.0001)







