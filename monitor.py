
from window import Window
from chart import Chart
from battery import Battery
from screen import Screen
from value import Value
from math import sin
from time import sleep



class Monitor:
    """
    This code Implements a very simple version of the
    display that is meant to be used by VNenergy. This
    includes a nice logo and a formatted configuration.
    """
    def __init__(self, width=1920, height=1080):
        # Create Screen with the provided resolution
        self.width = width #1920
        self.height = height #1080
        self.screen = Screen(width,height)
        self.logo = self.screen.load_image("logo.png")
        #self.logo = self.screen.scale(self.logo, 500,100)
        
        #self.screen.set_fps(10)
        # NOTE: Remove comment on next line to add Full screen
        #self.screen.set_full_screen()

        size = self.screen.get_size()
        self.border = 10
        b = self.border # Just to make the next line more readable

        self.battery = Battery(self.screen, x=20, y=self.height-355, width=140, height=300)

        # Creates a wyndow with a margin to make it pritty <3
        self.window = Window(self.screen, b+180, b+130 ,size[0]-(b*2+270) ,size[1]-(b*2+180))
        self.window.set_all_colors((100,100,100))
        self.window.set_border_color((200,200,200))
        self.window.set_border_width(10)
        self.chart_og = Chart()
        self.chart_og.set_width(8)
        self.chart_og.set_color((255,150,0))
        self.chart_og.add_point([1,1])
        self.chart_og.add_point([2,1])
        self.window.add_chart(self.chart_og)
        
        self.chart_optimised = Chart()
        self.chart_optimised.set_width(8)
        self.chart_optimised.set_color((0,150,255))
        self.chart_optimised.add_point([1,1])
        self.chart_optimised.add_point([2,1])
        self.window.add_chart(self.chart_optimised)
        # Next we add a function that converts the X values to
        # something the window class can work with, simple numbers
        # the window class does not know how to handle dates
        # so they need to be converted to intigers. These X values
        # are still used as labels in the x axis so format them
        # wisely.
        # NOTE: Remove comment on the fallowing line to add convertion function
        #self.chart.set_conv_funct(self.convert)

        self.data = Value(self.screen, 22, 150)

    def clear_charts(self):
        self.chart_og.clear()
        self.chart_optimised.clear()

    def convert(self, data):
        """
        onverts the data so that its in a format that can be
        later understood.
        """
        d = data.split(":")
        x = float(d[0]) * 60 + float(d[1])
        return [x, data[1]]

    def set_soc(self, value):
        self.data.set_value(value)
        self.battery.set_soc(abs(value))
        
        
    def add_data(self, data, data2):
        
        self.screen.clear()
        self.chart_og.add_point(data)
        self.chart_optimised.add_point(data2)
        # NOTE: Remove comment the fallowing line to add convertion function
        #self.convert() # This must be called if you have a convertion function
        self.window.draw()
        #self.battery.set_soc(abs(data[1]))
        self.battery.draw()
        self.data.draw()
        self.screen.draw_image(self.logo, [20,30])
        return self.screen.render()

    def close(self):
        self.screen.close()

###
    def test(self):
        counter = 1
        while(self.add_data([counter, sin(counter*0.01) * 100]) != -1):
              counter += 10
        print "Closing"
        self.close()

#m = Monitor()
# NOTE: Comment out the fallowing you dont need it. its just for testing
#m.test()
# NOTE: use the next line as an example of how to add data
#m.add_data(["h:m",value])
