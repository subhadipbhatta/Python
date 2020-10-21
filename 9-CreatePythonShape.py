## install pygame first by going to File > New Project Settings > Settings for New Projects... > python Interprator >
# Selectpython3.7 from the dropdown and search for pygame > once selected, go ahead and install

import pygame, sys

pygame.init() #initiate pygame
screen = pygame.display.set_mode((800,600)) #set up the screen size
screencolor = (0,0,0) #screencolor is typically RGB color. Range between (0,0,0) to (255,255,255)
screen.fill(screencolor)

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)

#coordinates
p1 = (40,40)
p2 = (100,100)
p3 = (200,150)
r1 = (100,300,120,190)

#blue rectangles
pygame.draw.rect(screen,blue,(200,200,150,80),0)
pygame.draw.rect(screen,blue,(310,170,40,40),0)
pygame.draw.rect(screen,blue,(250,130,100,40),0)
pygame.draw.circle(screen,white,(270,150),10,0)

#yellow rectangles
pygame.draw.rect(screen,yellow,(230,240,150,80),0)
pygame.draw.rect(screen,yellow,(230,310,40,40),0)
pygame.draw.rect(screen,yellow,(230,350,100,40),0)
pygame.draw.circle(screen,white,(300,370),10,0)

pygame.display.update()

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit();
            sys.exit();