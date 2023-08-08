import pygame
from settings import *
from calendarManager import CalendarManager
from textviews import Textviews

# Init Pygame & applications
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(CAPTION)

#DECLARE OBJECTS

calendarManager = CalendarManager()




running = True

while running:
    #GET USERS' INFORMATIONS
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

    screen.fill(WHITE)

    #application
    calendarManager.draw(screen)

    pygame.display.flip()

pygame.quit()

