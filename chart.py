"""
Author: Marco Rubio
Date Created: 9/10/2017
Description:
    This is a class obeject meant to make it easier fo r me to create renders
    using pygame thus reducing coding time. 
"""

import math

class Chart:
    def __init__(self):

        self.BLACK = (  0,   0,   0)
        self.GRAY = (  100,   100,   100)
        self.WHITE = (255, 255, 255)
        self.BLUE =  (  0,   0, 255)
        self.GREEN = (  0, 255,   0)
        self.RED =   (255,   0,   0)
        self.MARINE = (62, 128, 62)

        self.data = []
        self.conv_data = [] #converted version of the data
        self.max_label = "0"
        self.max_y = 1
        self.x_scale = 100
        self.y_scale = 100
        self.y_shift = 0
        self.y_margin = 0.1
        self.line_width = 10

        self.width = 2
        self.color = (100,100,100)
        self.convertion_function = 0

    def get_last_label(self):
        return self.max_label

    def convert(self):
        """
        This convertion function is really powerful as
        it allows a user to be able to convert a part of the
        data to a different value and thus be manipulated
        numerically as required by the wyndow.

        This was added as a method of allowing the user to
        pass any sort of date formmat and converted to a
        number for witch the window can use.
        """
        #needs to be optimized to only convert rightmost data
        if(self.convertion_function != 0):
            self.conv_data = []
            for point in self.data:
                self.conv_data.append(self.convertion_function(point))
        
        

    def set_conv_funct(self, function):
        """
        Sets a convertion function that is used to properly
        convert the data stored before returned
        """
        self.convertion_function = function

    def get_data(self):
        if (self.convertion_function == 0):
            return self.data
        else:
            return self.conv_data

    def get_rightmost_data(self, width, maxx=0):
        """
        Grabs the latest/rightmost data that is
        within the specified width. the datas
        x value is used in the comparison.

        a costum max is provided to allow external
        control of the maxpoint in a window. This
        can come from a chart with data that is more
        up to date
        """

        #if a convertion function is availlable then use it
        if(self.convertion_function == 0):
            self_data = self.data
        else:
            self_data = self.conv_data
        data = []
        i = -1
        max_x = self_data[-1][0]
        if (maxx):
            max_x = maxx
            
        length = len(self_data)
        while((max_x - self_data[i][0]) < width):
            #print max_x, self.data[i][0], width, i, length
            data.append(self_data[i])
            i -= 1
            if((i*-1) > length):
                break
            
        #print "done", max_x, self.data[i][0], width, i, length
        return data

    def get_color(self):
        return self.color

    def get_width(self):
        return self.width

    def set_color(self, color):
        """
        must be a tuple of the form:
        (r,g,b)
        where 'r,g,b' ar within the range of 0 - 255
        """
        self.color = color

    def set_width(self, width):
        self.width = width

    def get_max_values(self, width=0, right_most=1):
        """
        The width value just stops lookig for a max value
        after a certain point. 'right_most' sets this function
        to start from the end of the data. The values returned
        contain the maximum x and y values in all the points.
        """
        if(self.convertion_function == 0):
            self_data = self.data
        else:
            self_data = self.conv_data
            
        start = right_most * -1
        d = self_data[start]
        max_y = 0
        max_x = 0
        i = start #iterator
        #print self.data[-1][0], right_most, start, self.data[i][0], width
        length = len(self_data)
        while(((self_data[-1][0] * right_most) - self_data[i][0] * (2 * right_most - 1)) < width*2):
            #print i, self.data[-1][0], right_most, start, self.data[i][0], width
            if(max_y < abs(self_data[i][1])):
                max_y = abs(self_data[i][1])
            if(max_x < abs(self_data[i][0])):
                max_x = abs(self_data[i][0])
                self.max_label = self.data[i][0] #Pulls it from the original data
                
            if(right_most and i > (-1 * length)):
                i -= 1
            elif(not right_most and i < (length-1)):
                i += 1
            else:
                break
        return max_x, max_y

    def auto_scale_data(self, data, x_scale=1):
        """
        Auto Scales the data in the Y direction based on the highest spike.
        also shifts the data in the Y direction so ints centered on screen.

        inputs:
                x_scale - multipler for the x scale. does not auto scale since
                          there is no assumed reference
        
        """
        scaled = []         # final data container
        max_x = data[-1][0] # used for scaling and transforming
        for v in data:
            y = ((v[1]/self.max_y) * self.y_shift * (1 - self.y_margin) + self.y_shift)
            scaled.append([v[0], y])
        return scaled

    def get_newest_points(self):
        """
        Starting from the rightmost point the lastest point is retrieved
        up until the leftmost point goes out of bouns of the screen. This
        array will be a subset of the main data.
        """
        subset = []
        max_x = self.data[-1][0]
        self.max_y = self.data[-1][1]
        i = 1
        try:
            while ((max_x - self.data[-i][0]) < self.width):
                #This is where the scrolling magic happens
                new_x = self.width - (max_x - self.data[-i][0])
                subset.append([new_x,self.data[-i][1]])
                i += 1
                if(self.max_y < self.data[-i][1]):
                    self.max_y = self.data[-i][1]
        except IndexError:
            pass
        
        return subset
        

    def add_point(self, point):
        self.data.append(point)

    def draw_new_lines(self, auto_scale=True):
        """
        Draws a simple line on the screen
        """
        if (len(self.data) > 1):
            self.clear()
            points = self.get_newest_points()
            if(auto_scale):
                pygame.draw.lines(self.screen, self.RED, False, self.auto_scale_data(points), self.line_width)
            else:
                pygame.draw.lines(self.screen, self.RED, False, points, self.line_width)
            pygame.display.flip()

