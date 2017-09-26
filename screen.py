"""
Author: Marco Rubio
Date Created: 9/10/2017
Description:
    This is a class obeject meant to make it easier fo r me to create renders
    using pygame thus reducing coding time. 
"""

import pygame, math, random

class Screen:
    def __init__(self, width=1280, height=800):
        
        pygame.init()
        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Results")

        self.BLACK = (  0,   0,   0)
        self.GRAY = (  100,   100,   100)
        self.WHITE = (255, 255, 255)
        self.BLUE =  (  0,   0, 255)
        self.GREEN = (  0, 255,   0)
        self.RED =   (255,   0,   0)
        self.MARINE = (62, 128, 62)

    def get_screen(self):
        return screen

    def clear(self):
        self.screen.fill(self.BLACK)

    def draw_lines(self, color, data, width):
        """
        Draws a simple line on the screen
        """
        pygame.draw.lines(self.screen, color, False, data, width)

    def draw_rectangle(self, color, rect, width=0):
        pygame.draw.rect(self.screen, color, rect, width)

    def close(self):
        pygame.quit()        

    def render(self):
        pygame.display.flip()
        

    
