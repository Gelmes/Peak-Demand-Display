import serial
from window import Window
from chart import Chart
from screen import Screen

m1 = 0.0
m2 = 0.0
m3 = 0.0
light = 0.0

m1_kw = 200
m2_kw = 200
m3_kw = 200
light_kw = 50
total_kw = 0

array = []

sma_array = []
sma_length = 10
sma_index = 0

def create_array(length):
    global sma_array, sma_length, sma_index
    for i in range(length):
        sma_array.append(0.0)
    sma_length = length

def sma(value):
    global sma_index, sma_array, sma_length
    sma_array[sma_index % sma_length] = value
    sma_index += 1
    total = 0
    for v in sma_array:
        total += v
        
    return total/float(sma_length )

def simulator(msg):
    global total_kw, m1, m2, m3, light
    if(msg != ''):
        val = msg.split(",")
        m1 = float(val[0]) * m1_kw
        m2 = float(val[1]) * m2_kw
        m3 = float(val[2]) * m3_kw
        light = float(val[3]) * light_kw
        total_kw = m1 + m2 + m3 + light
        val = sma(total_kw)
        return val 
    else:
        
        total_kw = m1 + m2 + m3 + light
        val = sma(total_kw)
        return val 
    
create_array(10)
try:
    ser = serial.Serial("COM7", 9600, timeout=0.01)
except SerialException:
    print "Error"
    
msg = "0,0,0,0"
m1 = 0

c = Chart()

c.add_point([0,0])
c.add_point([1,1])
c.set_color((200,200,0))
c.set_width(6)

s = Screen()
w = Window(s,0,0,1280,800)
w.add_chart(c)
w.set_zoom(2)
w.set_y_shift(0)

s.clear()
w.draw()
s.render()

counter = 2;
while(not m1):
    msg = ser.readline()
    try:
        m1 = int(msg.split(",")[0])
    except ValueError:
        m1 = 0

    result = simulator(msg)
    #print result
    s.clear()
    c.add_point([counter, result])
    w.draw()
    s.render()
    
    counter += 1
print "done"
s.close()
ser.close()

