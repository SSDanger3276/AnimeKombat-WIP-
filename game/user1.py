#Maybe make projectiles a class for future attacks

import pygame as pg


class player():
    def __init__(self,scrn,x,y,col):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 200
        self.col = col
        self.p_vel = 5
        self.rect = pg.Rect(self.x,self.y,self.width,self.height)
        if (self.col == "red"):
            self.dir = "right"
        if (self.col == "blue"):
            self.dir = "left"
        #Specific vars
        #Graviy
        self.grav = 0
        self.jumpH = self.y - 100
        self.jumping = False
        self.can_jump = True
        self.multiple_jumps = 0
        self.in_air = False #self.can_jump = False and self.jumping = True/False
        #Health bar
        self.health = 100
        self.can_be_hurt = True
        # create health bars
        if (self.col == "blue"):
            self.old_hth_bar = pg.Rect(10,0,scrn.get_width() - 600, 70)
            self.hth_bar = pg.Rect(self.old_hth_bar)
        if (self.col == "red"):
            self.old_hth_bar = pg.Rect(scrn.get_width() - 400,0,scrn.get_width() - 10, 70)
            self.hth_bar = pg.Rect(self.old_hth_bar)
        #Attacks
        # Shoot
        self.projectiles = []
        self.prot_col = "red"
        self.did_shoot = False
        self.shoot_cc = 0
        self.shoot_add_inc = 30
        self.shot_vel = 3
        self.shot_damage = 20
        # Punch
        self.attacks = []
        self.did_punch = False
        self.pnh_add_inc = 20 #time punch is left out
        self.pnh_cc = 0
        self.pnh_dec_inc = 50 #time till next punch
        self.pnh_damage = 40


    def move_1(self,scrn):
        keys = pg.key.get_pressed()
        if (keys[pg.K_a] and self.x > 0):
            self.x -= self.p_vel
        if (keys[pg.K_d] and self.x + self.width < scrn.get_width()):
            self.x += self.p_vel


    def move_2(self,scrn):
        keys = pg.key.get_pressed()
        if (keys[pg.K_LEFT] and self.x > 0):
            self.x -= self.p_vel
        if (keys[pg.K_RIGHT] and self.x + self.width < scrn.get_width()):
            self.x += self.p_vel


    def gravity(self,plat):
        #Falling
        if (self.jumping == False):
            if (self.y + self.height < plat.y):
                self.grav += 1
                self.y += self.grav
            #Still
            if (self.y + self.height > plat.y):
                self.grav = 0
                self.rect.bottom = plat.top
                self.can_jump = True


    def jump(self):
        keys = pg.key.get_pressed()
        if (self.jumping == False):
            #Specific jump button
            if (self.can_jump):
                if (self.col == "red"):
                    if (keys[pg.K_w]):
                        self.can_jump = False
                        self.jumping = True
                if (self.col == "blue"):
                    if (keys[pg.K_UP]):
                        self.can_jump = False
                        self.jumping = True
        if (self.jumping):
            if (self.y > self.jumpH): 
                self.grav += 10
                self.y -= self.grav
            else:
                self.grav = -5
                self.jumping = False


    def attack(self,scrn,players): 
        keys = pg.key.get_pressed()
        if (self.did_punch == False):
            if (self.col == "red"):
                if (keys[pg.K_p]):
                    punch = pg.Rect(self.x + self.width, self.y + self.height/2 - 50, 100, 100)
                    self.attacks.append(punch)
                    self.did_punch = True
            if (self.col == "blue"):
                if (keys[pg.K_COMMA]):
                    punch = pg.Rect(self.x + self.width, self.y + self.height/2 - 50, 100, 100)
                    self.attacks.append(punch)
                    self.did_punch = True
            # Delete if multiple punches
            for punch in self.attacks:
                if (len(self.attacks) > 1):
                    self.attacks.remove(punch)
        if (self.did_punch):
            self.p_vel = 2
            # delete punch
            self.pnh_cc += 1
            if (self.pnh_cc >= self.pnh_add_inc):
                self.pnh_cc = 0
                self.p_vel = 5
                self.did_punch = False
            #Show punch 
            for punch in self.attacks:
                    # update coords
                    # got hit
                    for player in players:
                        if (player.rect != self.rect): #might use this in the future
                                if (self.can_be_hurt == True):
                                    if (punch.colliderect(player.rect)):
                                        if (self.col == "red"):
                                            self.hth_bar.x += self.pnh_damage
                                            #print("blue was hit")
                                        if (self.col == "blue"):
                                            self.hth_bar.width -= self.pnh_damage
                                            #print("red was hit")
                    # draw
                    pg.draw.rect(scrn,"red",punch)


    def shoot(self,scrn,players):
        keys = pg.key.get_pressed()
        #Shooter gunna shoot
        if (self.col == "red"):
            if (self.did_shoot == False):
                if (keys[pg.K_o]):
                    shot = pg.Rect(self.x + self.width,self.y + self.height/2,50,50)
                    self.projectiles.append(shot)
                    self.did_shoot = True
        if (self.col == "blue"):
            if (self.did_shoot == False):
                if (keys[pg.K_SLASH]):
                    shot = pg.Rect(self.x - self.width,self.y + self.height/2,50,50)
                    self.projectiles.append(shot)
                    self.did_shoot = True
        #Time between each shot
        if (self.did_shoot):
            self.p_vel = 2
            self.shoot_cc += 1
            if (self.shoot_cc > self.shoot_add_inc):
                self.shoot_cc = 0
                self.p_vel = 5
                self.did_shoot = False
        #Update shots
        for prot in self.projectiles:
            #if (self.did_shoot == True): Maybe add this line back 
            if (self.col == "red"):
                prot.x += self.shot_vel
                self.prot_col = self.col
                pg.draw.rect(scrn,self.prot_col,prot)
            if (self.col == "blue"):
                prot.x -= self.shot_vel
                self.prot_col = self.col
                pg.draw.rect(scrn,self.prot_col,prot)
            #! got hit (favorite code really like how we made it, its even simplified :0)
            for player in players:
                if (player.rect != self.rect): #might use this in the future
                        if (self.can_be_hurt == True):
                            if (prot.colliderect(player.rect)):
                                if (self.col == "red"):
                                    self.hth_bar.x += self.shot_damage
                                    #print("blue was hit")
                                if (self.col == "blue"):
                                    self.hth_bar.width -= self.shot_damage
                                    #print("red was hit")
                                self.projectiles.remove(prot) 


    def health_bar(self,scrn):
        if (self.col == "red"):
            pg.draw.rect(scrn,"yellow",self.hth_bar)
            pg.draw.rect(scrn,"black",self.old_hth_bar,5)
        if (self.col == "blue"):
            pg.draw.rect(scrn,"yellow",self.hth_bar)
            pg.draw.rect(scrn,"black",self.old_hth_bar,5)


    def draw(self,scrn,players,plat):
        #Update
        self.rect = pg.Rect(self.x,self.y,self.width,self.height)
        pg.draw.rect(scrn,self.col,self.rect)
        #Functions
        self.jump()
        self.gravity(plat)
        self.health_bar(scrn)
        self.shoot(scrn,players)


class Projectile():
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = self.width
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.vel = 3

    def draw(self):
        pass
