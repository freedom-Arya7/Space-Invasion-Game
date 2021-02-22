# Space Invasion Game
import pygame
import random

#initialize the pygame screen
pygame.init()

# screen initial set up
scr = pygame.display.set_mode((800, 600))
# Background | Title | Icon
bg = pygame.image.load('bg3.jpg')
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
dx = 0
dy = 0

# Alien
alienImg = pygame.image.load('alien1.png')
alienX = random.randint(10, 790)
alienY = random.randint(10, 190)
adx = 1/2
ady = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bdx = 0
bdy = 5
# Ready state : You can't see the bullet on the screen
# Fire state : Bullet is currently moving
bullet_state = "ready"

def player(x, y):
    scr.blit(playerImg, (x, y))

def alien(x, y):
    scr.blit(alienImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    scr.blit(bulletImg, (x + 16, y + 10))

# Game Loop
running = True
while running:
    # screen color : rgb - red, green, blue  <values range from 0 to 255>
    scr.fill((0, 0, 120))
    scr.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If any Keystroke is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
            elif event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        # If the keystroke is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0

    # checking to keep the player in boundary of the screen
    playerX += dx
    playerY += dy
    if playerX > 730:
        playerX = 730
    elif playerX < 0:
        playerX = 0
    elif playerY > 535:
        playerY = 535
    elif playerY < 0:
        playerY = 0

    # checking to keep the alien in boundary of the screen
    alienX += adx
    if alienX > 730:
        adx = -1/2
        alienY += ady
    elif alienX < 0:
        adx = 1/2
        alienY += ady

    # Movement of bullet
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bdy

    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()

