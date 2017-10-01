from window import Window
from chart import Chart
from screen import Screen
from math import sin
from time import sleep

c = Chart()
c.add_point([0,1])
c.add_point([20,1])
c.add_point([30,3])
c.add_point([40,1])
c.add_point([50,1])
c.add_point([60,5])
c.add_point([65,-40])
c.add_point([70,1])
c.add_point([75,-15])
c.add_point([80,10])
c.add_point([85,30])
c.add_point([90,30])
c.add_point([95,50])
c.add_point([100,1])

c2 = Chart()
c2.add_point([0,1])
c2.add_point([20,1])
c2.add_point([30,3])
c2.add_point([40,1])
c2.add_point([50,1])
c2.add_point([60,5])
c2.add_point([65,-30])
c2.add_point([70,1])
c2.add_point([75,-05])
c2.add_point([80,10])
c2.add_point([85,20])
c2.add_point([90,20])
c2.add_point([95,30])
c2.add_point([100,1])
c2.add_point([110,-70])
c2.set_color((255,255,0))

def conv(data):
    return [data[0] * 2, data[1]]
c.set_conv_funct(conv)

s = Screen()
s.set_fps(35)
w = Window(s,300,100,400,400)
w2 = Window(s,400,400,400,400)
w.set_zoom(0.5)
w.add_chart(c)
w.add_chart(c2)
w2.set_zoom(5)
w2.add_chart(c2)

counter = 110
step = 2
scale = 100
    
s.clear()
c.convert()
c2.convert()
w.draw()
w2.draw()

while(s.render() != -1):
    counter += step
    
    #sleep(0.1)
    s.clear()
    c.add_point([counter, sin(counter/20.0)*scale])  
    c.convert() #this is important to call every iteration
                #if you have a convertion function
                #otherwise the data will not be updated
    w.draw()
    w2.draw()
    
    #print counter
    

"""
s.clear()
c.add_point([110,100])
w.draw()
#w2.draw()
s.render()
"""



#pygame.time.delay(10)
#pygame.display.flip() 
