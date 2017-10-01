
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
        self.screen = Screen()
        self.screen.set_full_screen()

        size = self.screen.get_size()
        self.border = 10
        b = self.border # Just to make the next line more readable

        # Creates a wyndow with a margin to make it pritty <3
        self.window = Window(Self.screen, b, b ,size[0]-(b*2) ,size[1]-(b*2))
        self.chart = Chart()
        # Next we add a function that converts the X values to
        # something the window class can work with, simple numbers
        # the window class does not know how to handle dates
        # so they need to be converted to intigers. These X values
        # are still used as labels in the x axis so format them
        # wisely.
        self.chart.set_conv_funct(self.convert)
                        
        

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
        self.convert() # This must be called if you have a convertion function
        self.window.draw()
        s.render()
