import pygame as pg


# This is the HomePage class for the game. It will display the home page of the game and allow the user to start the game.
pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#Yo if you can change this to to activate when main is on, that'd be great.
Run = True

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while Run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False

pg.quit()
        
            


    

class HomePage:
    def __init__(self, screen):
        pass
        