
from window import Window
from chart import Chart
from screen import Screen
from math import sin
from time import sleep



class Monitor:
    """
    This code Implements a very simple version of the
    display that is meant to be used by VNenergy. This
    includes a nice logo and a formatted configuration.
    """
    def __init__(self):
        # Create Screen with the provided resolution
        self.screen = Screen(1920,1080)
        #self.screen.set_fps(10)
        # NOTE: Remove comment on next line to add Full screen
        #self.screen.set_full_screen()

        size = self.screen.get_size()
        self.border = 10
        b = self.border # Just to make the next line more readable

        # Creates a wyndow with a margin to make it pritty <3
        self.window = Window(self.screen, b, b ,size[0]-(b*2+100) ,size[1]-(b*2+50))
        self.window.set_all_colors((100,100,100))
        self.chart = Chart()
        self.chart.set_width(8)
        self.chart.set_color((255,150,0))
        self.chart.add_point([0,0])
        self.chart.add_point([1,0])
        self.window.add_chart(self.chart)
        # Next we add a function that converts the X values to
        # something the window class can work with, simple numbers
        # the window class does not know how to handle dates
        # so they need to be converted to intigers. These X values
        # are still used as labels in the x axis so format them
        # wisely.
        # NOTE: Remove comment on the fallowing line to add convertion function
        #self.chart.set_conv_funct(self.convert)

    def convert(self, data):
        """
        onverts the data so that its in a format that can be
        later understood.
        """
        d = data.split(":")
        x = float(d[0]) * 60 + float(d[1])
        return [x, data[1]]
        
        
    def add_data(self, data):
        
        self.screen.clear()
        self.chart.add_point(data)
        # NOTE: Remove comment the fallowing line to add convertion function
        #self.convert() # This must be called if you have a convertion function
        self.window.draw()
        return self.screen.render()

    def close(self):
        self.screen.close()

###
    def test(self):
        counter = 1
        #TODO: exits for no reason
        while(self.add_data([counter, sin(counter*0.01) * 100]) != -1):
              counter += 1
        print "Closing"
        self.close()

m = Monitor()
# NOTE: Comment out the fallowing you dont need it. its just for testing
m.test()
# NOTE: use the next line as an example of how to add data
m.add_data(["h:m",value])
