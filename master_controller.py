import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
#TO DO add auto scaling and scrolling

#np.where(a[:,0] > 3)

#get array of objects of the last 60 seconds
#a[np.where((a[:,0][-1] - a[:,0]) < 60)]#returns array of results

random_list = np.array([[0,0]])

#np.append(random_list,np.random.rand(1,2), axis=0)

x = 0.0
step = 0.1

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)


def update(a):
    selection = a[np.where((a[:,0][-1] - a[:,0]) < 10)]
    #line.set_data(selection[:,0], selection[:,1])
    line.set_data(np.arange(len(selection)), selection[:,1])
    print(np.array(len(selection)))
    return line,


def data_gen():
    global random_list
    while True:
        random_list = np.append(random_list,np.random.rand(1,2), axis=0)        
        #print random_list
        yield random_list

ani = animation.FuncAnimation(fig, update, data_gen, interval=1000)
plt.show()
