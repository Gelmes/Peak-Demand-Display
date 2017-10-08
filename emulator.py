import serial
from window import Window
from chart import Chart
from screen import Screen
from monitor import Monitor
from arduino import Arduino
from simulator import Simulator
import time

ard = Arduino()
sim = Simulator()
mon = Monitor()


# Get data a few times to remove any initial value noise
data = ard.get_data()
data = ard.get_data()
data = ard.get_data()

counter = 2

memory = []

"""
Data information description
0 - motor 1
1 - motor 2
2 - motor 3
3 - Light
4 - play 
5 - stop
6 - mode id
"""

while(data[0] == 0): #while motor1 is not pressed

    result = sim.add_data(data)    
    mon.set_soc(int(result/650.0*100))    
    mon.add_data([counter, result], [counter,result/2])    
    data = ard.get_data()
    counter += 1
    

ard.close()
mon.close()
