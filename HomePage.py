import pygame as pg


# This is the HomePage class for the game. It will display the home page of the game and allow the user to start the game.
pg.init()
pg.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
#Yo if you can change this to to activate when main is on, that'd be great.
Run = True

#Images
Home_Page_images = pg.image.load("Homepage pot1.png").convert()
Home_Page_images.set_colorkey((0, 0, 0))



screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('AniCombat')


CLOCK = pg.time.Clock()

# The Aesthetics :D
def draw_home_page():
        Font = pg.font.SysFont('Comic Sans MS', 30)
        
        Sign_In_Button = (pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 150, 300, 75),
                                       border_radius= 50),
                          Font.render('Sign Up', True, (255, 255, 255)))
        Login_Button = (pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 300, 300, 75),
                                     border_radius= 50),
                        Font.render('Login', True, (255, 255, 255)))
        screen.blit(Sign_In_Button[1], (SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT - 135))
        screen.blit(Login_Button[1], (SCREEN_WIDTH//2 - 30, SCREEN_HEIGHT - 285))


        

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
    screen.bilt()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
    CLOCK.tick(60)
    pg.display.update()
pg.quit()
        

class HomePage:
    def __init__(self, screen):
        pass
        