import pygame as pg


# This is the HomePage class for the game. It will display the home page of the game and allow the user to start the game.
pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
#Yo if you can change this to to activate when main is on, that'd be great.
Run = True

#Images


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Anibat Verse')

# The Aesthetics :D
def draw_home_page():
        pg.draw.rect(screen, (45, 43, 76), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        Sign_In_Button = pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 150, 300, 75))
        Login_Button = pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 300, 300, 75))
        

def Login_In():
    # This function will handle the login process for the user. It will display a login form and allow the user to enter their username and password.
    pass
def Sign_Up():
    # This function will handle the sign up process for the user. It will display a sign up form and allow the user to enter their username, password, and email address.
    pass
def Home_Page():
    # This function will display the home page of the game. It will allow the user to start the game, view the leaderboard, and access the settings.
    pass

while Run:
    draw_home_page()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
    pg.display.update()
pg.quit()
        
            


    

class HomePage:
    def __init__(self, screen):
        pass
        