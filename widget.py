import pygame
from settings import *

class Widget:
    def __init__(self, parent,pos, size, align=0):
        #SET PARENT
        self.parent = parent
        #SET POS
        self.w = size [0]
        self.h = size [1] 
        match align:
            case 0:
                self.x = self.parent.x + pos[0]
                self.y = self.parent.y + pos[1]
            case 1:
                self.x = self.parent.x + (self.parent.w - self.w) //2
                self.y = self.parent.y + (pos[1])

        #SET RESTORE
        self.buttons = []
        self.textviews = []
        
    def draw(self,surface):
        #DRAW BACKGROUND
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.w, self.h))

        #DRAW SUBVIEW
        for button in self.buttons:
            button.draw(surface)
        for textview in self.textviews:
            textview.draw(surface)