import sqlite3
import bcrypt
from cryptography.fernet import Fernet
import pygame as pg
import requests
#Load encryption key from .env file

with open('.env', 'r') as key_file:
    key = key_file.read()
fernet = Fernet(key)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
def check_password(password, stored_hash):
    return bcrypt.checkpw(password.encode(), stored_hash)


# This is the HomePage class for the game. It will display the home page of the game and allow the user to start the game.
pg.init()
pg.font.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
#Yo if you can change this to to activate when main is on, that'd be great.
Run = True
    
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('AniCombat')

CLOCK = pg.time.Clock()

class HomePage:
    def __init__(self, Username, Password_hash , email_encrypyed, player_data_json):
        self.Username = Username
        self.Password_hash = Password_hash
        self.email_encrypyed = email_encrypyed
        self.player_data_json = player_data_json

# The Aesthetics :D
def start_up():
        Font = pg.font.SysFont('Comic Sans MS', 30)
        pg.draw.rect(screen, (136, 124, 116), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        Title = Font.render('Welcome to AniCombat!', True, (0, 0, 0))
        screen.blit(Title, (SCREEN_WIDTH//2 - Title.get_width()//2, SCREEN_HEIGHT//2 - 200))
        Sign_In_Button = (pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 150, 300, 75),
                                       border_radius= 50),
                          Font.render('Sign Up', True, (255, 255, 255)))
        Login_Button = (pg.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 300, 300, 75),
                                     border_radius= 50),
                        Font.render('Login', True, (255, 255, 255)))
        screen.blit(Sign_In_Button[1], (SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT - 135))
        screen.blit(Login_Button[1], (SCREEN_WIDTH//2 - 30, SCREEN_HEIGHT - 285))
        if pg.mouse.get_pressed()[0]:
            mouse_pos = pg.mouse.get_pos()
            if Sign_In_Button[0].collidepoint(mouse_pos):
                Sign_Up()
            elif Login_Button[0].collidepoint(mouse_pos):
                Login_In()

def Login_In(Username, Password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (Username,))
    result = cursor.fetchone()

    conn.close()

    if result is None:
        print("User not found.")
        return False

    stored_hash = result[0]

    if check_password(Password, stored_hash):
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False

def Sign_Up(username, password, email):
    password_hash = hash_password(password)
    encrypted_email = fernet.encrypt(email.encode())

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, encrypted_email, password_hash)
        )
        conn.commit()
        print("User created successfully!")

    except sqlite3.IntegrityError:
        print("Username or email already taken.")

    conn.close()

def Home_Page(Username):
    # This function will display the home page of the game. It will allow the user to start the game, view the leaderboard, and access the settings.
    pass
#Get the thing running
start_up()
while Run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
    CLOCK.tick(60)
    pg.display.update()
pg.quit()        