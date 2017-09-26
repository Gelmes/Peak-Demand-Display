"""
Author: Marco Rubio
Date Created: 9/10/2017
Description:
    This is a class obeject meant to make it easier fo r me to create renders
    using pygame thus reducing coding time. 
"""

import pygame, math, random

class Display:
    def __init__(self):
        pygame.init()

        self.BLACK = (  0,   0,   0)
        self.GRAY = (  100,   100,   100)
        self.WHITE = (255, 255, 255)
        self.BLUE =  (  0,   0, 255)
        self.GREEN = (  0, 255,   0)
        self.RED =   (255,   0,   0)
        self.MARINE = (62, 128, 62)
        

        self.size = self.width, self.height = 1280, 800
        speed = [2, 2]
        black = 0, 0, 0

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Results")
        done = False
        clock = pygame.time.Clock()
        #handimage = pygame.image.load('hand.png').convert_alpha()
        #hand = GameObject.GameObject(handimage, 10, 5, size)

        self.data = []
        self.max_y = 1
        self.x_scale = 100
        self.y_scale = 100
        self.y_shift = self.height / 2
        self.y_margin = 0.1
        self.line_width = 10

    def clear(self):
        self.screen.fill(self.BLACK)

    def auto_scale_data(self, data):
        scaled = []
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
        self.data.append([point[0],point[1]])

    def draw_line(self, x1, y1, x2, y2):
        """
        Draws a simple line on the screen
        """

    def draw__lines(self):
        """
        Draws a simple line on the screen
        """
        self.clear()     
        pygame.draw.lines(self.screen, self.RED, False, self.data, self.line_width)
        pygame.display.flip() 

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

    def draw_data(self):
        pass

    def draw_grid(self):
        pass

    def draw_lables(self):
        pass

counter_y = 0.0
counter_x = 0.0
counter = 0.0
step = 0.02
amplitude = 200.0

d = Display()

while (True):
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
                
    counter += step
    counter_x += 1
    counter_y  = math.sin(counter)# + random.random()/2#* amplitude
    
    d.add_point([counter_x, counter_y])
    d.draw_new_lines()

    pygame.time.delay(10)
