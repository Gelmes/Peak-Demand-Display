import serial
from window import Window
from chart import Chart
from screen import Screen
from monitor import Monitor
from arduino import Arduino
from simulator import Simulator
import time
from cvx import DemandManagement


ard = Arduino()
sim = Simulator()
mon = Monitor()
dm  = DemmandManagement()

# Get data a few times to remove any initial value noise
data = ard.get_data()
data = ard.get_data()
data = ard.get_data()

counter = 2


"""
Data information description
0 - motor 1
1 - motor 2
2 - motor 3
3 - Light
4 - play 
5 - record/stop
6 - mode id
"""

memory = []

#Minutes in a day 24 * 60 = 1440 minutes
def create_array(length, fill=0.0):
    """
    Creates an array of length with elements initialiced to 'fill'
    """
    array = []
    for i in range(length):
        array.push(0)

def add_data(data):
    result = sim.add_data(data) 
    mon.set_soc(int(result/650.0*100))    
    mon.add_data([counter, result], [counter,result/2])

def resimulate(ogload, optimized, soc):
    for i in range(len(ogload)):
        mon.set_soc(int(soc))    
        mon.add_data(ogload[i], optimized[i])
        data = ard.get_data()
    
    

while(data[0] == 0): #while motor1 is not pressed
    add_data(data)
    data = ard.get_data()

    # Detect a button press on record and if pressed
    # Record all the presses for future use in memory
    if(data[5]):
        while(data[5]): #handle a continuous press               
            data = ard.get_data()
        sim.clear()
        mon.clear_charts()
        memory = []
        while(not data[5]):           
            add_data(data)            
            data = ard.get_data()
            counter += 1
            memory.append(data)        
        while(data[5]): #handle a continuous press               
            data = ard.get_data()
        solar = create_array(len(memory),0)
        dm.solar = solar
        dm.load = memory

        ogload, optimized, soc  = dm.demand_shave()
        while(not data[4]): #freeze code while play button is not pressed
            data = ard.get_data()

        while(data[4]): # Wait for the play button press                
            data = ard.get_data()
        #once the play button is depressed it will play back with optimzation   
        sim.clear()
        mon.clear_charts()
        resimulate(ogload, optimized, soc)

        while(not data[5]): # wait for the stop button press                      
            data = ard.get_data()

        

        
    
    counter += 1
    

ard.close()
mon.close()
