import pygame
from settings import *

class Buttons:
    def __init__(self, parent, pos, size, text = "", font = "",sizeText = 14, color = BLACK, background = WHITE):
        #SET VIEW
        self.background = background
        self.default = background

        #SET PARENT 
        self.parent = parent

        #SET POS
        self.x= self.parent.x +pos[0]
        self.y= self.parent.y +pos[1]
        self.w = size[0]
        self.h= size[1]

    def draw(self,surface):
        #LISTEN USER
        self.mouseListener()
        #DRAW BACKGROUND
        pygame.draw.rect(surface, self.background, (self.x, self.y, self.w, self.h))

    def mouseListener(self):
        [x,y]=pygame.mouse.get_pos()
        if (self.x <= x and x <= self.x + self.w and self.y <= y and y <= self.y +self.h):
            self.background= BLACK
        else: self.background= self.default
