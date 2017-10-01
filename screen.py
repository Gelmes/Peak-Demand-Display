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
        
        self.clock = pygame.time.Clock()
        self.fps = 30

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 20)

    def get_size(self):
        return self.size

    def set_full_screen(self):
        pygame.display.quit()
        pygame.display.init()
        self.screen = pygame.display.set_mode(self.size, pygame.FULL_SCREEN)

    def draw_text(self, string, pos, color, vertical=0):
        """
        Position is a set of x and y coordinates
        color is a tuple of size 3 with values from 0 to 255
        representing red, green, and blue
        """
        text = self.font.render(string, False, color)
        if(not vertical):
            text = pygame.transform.rotate(text, 0)
            self.screen.blit(text, (pos[0]+5, pos[1]-(text.get_height()/2)))
        elif(vertical):
            text = pygame.transform.rotate(text, 90)
            self.screen.blit(text, (pos[0]-(text.get_width()/2), pos[1]+5))

    def set_fps(self, fps):
        self.fps = fps

    def get_screen(self):
        return screen

    def clear(self):
        self.screen.fill(self.BLACK)

    def draw_line(self, color, start, stop, width):
        pygame.draw.line(self.screen, color, start, stop, width) 

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
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
           self.close()
           return -1
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
           self.close()
           return -1
        #pygame.event.get()
        pygame.display.flip()
        self.clock.tick(self.fps)
        return 0
        

    
