import pygame as pg


# This is the HomePage class for the game. It will display the home page of the game and allow the user to start the game.
pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
#Yo if you can change this to to activate when main is on, that'd be great.
Run = True

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



while Run:
    # The Aesthetics :D
    def draw_home_page():
        pg.draw.rect(screen, (45, 43, 76), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        Sign_In_Button = pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 150, 300, 75))
        Login_Button = pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 300, 300, 75))

    draw_home_page()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
    pg.display.update()
pg.quit()
        
            


    

class HomePage:
    def __init__(self, screen):
        pass
        