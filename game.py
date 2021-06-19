import pygame
from pygame import mixer
import random
import math
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#asset_url = resource_path('assets/chars/hero.png')
#hero_asset = pygame.image.load(asset_url)

pygame.init()
# initialising the object pygame

#creating the screen
screen = pygame.display.set_mode((800,600))
# add clock to limit the frame rate 
# sounds url
laser_url = resource_path('asset/laser.wav')
backgroundwav_url = resource_path('asset/background.wav')
explosion_url = resource_path('asset/explosion.wav')

## background for game
background_url = resource_path('asset/background.png')
background = pygame.image.load(background_url)
## background sound
mixer.music.load(backgroundwav_url)
mixer.music.play(-1)

#title and icon
pygame.display.set_caption("Invasion")
icon_url = resource_path('asset/alien.png')
icon= pygame.image.load(icon_url)
pygame.display.set_icon(icon)

# playericon and position
player_url = resource_path('asset/player.png')
playerimg=pygame.image.load(player_url)
playerX=370
playerY=480
playerX_change=0

enemy_url = resource_path('asset/ufo.png')
#enemy icon and  position
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(enemy_url))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3)
    enemyY_change.append(40)

#Bullet icon and  position
#bullet state - Ready means bullet is not seen on screen
#bullet state - Fire mean bullet is fired and can be seen on screen
bullet_url = resource_path('asset/bullet.png')
bulletimg=pygame.image.load(bullet_url)
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=13
bullet_state="ready"

#scorecount
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# making player function
def player(x,y):
    screen.blit(playerimg, (x,y))

# making enemy function
def enemy(x,y,i):
    screen.blit(enemyimg[i], (x,y))

# making bullet function
def bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,((x+16),(y+10)))

# check collison
def iscollison(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX , 2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    return False



# game window loop...
running = True
while running:
    # screen background color
   # print("In loop")
    screen.fill((0,0,0))
    #bcakground
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
        #if keystroke is pressed check whether it is right or left
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change= 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound(laser_url)
                    bullet_sound.play()
                    bulletX=playerX
                    bullet(bulletX,bulletY)
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                playerX_change =0


    # call the player function to contnously draw it on screen
    playerX += playerX_change 
    # checking spaceship boundary
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    

    # change in enemy
    for i in range(num_of_enemies):

        #game over
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
            

        enemyX[i] += enemyX_change[i] 

        if enemyX[i]<=0:
            enemyX_change[i]=3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-3
            enemyY[i] += enemyY_change[i]
        #call the enemy function
        #collison
        collison= iscollison(enemyX[i],enemyY[i],bulletX,bulletY)
        if collison:
            collison_sound=mixer.Sound(explosion_url)
            collison_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)

    #logic of bullets
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state=="fire":
        bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    
    #calling score
    show_score(textX,textY)
    #calling player function
    player(playerX,playerY)
    # update the screen after the end of while everytime.
    pygame.display.update()