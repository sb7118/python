import pygame
import random
import math

#initializes the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800 ,600)) #(x,y)

#background
#background = pygame.image.load('background.png')

#Title and icon
pygame.display.set_caption('space invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('ship.png')
playerX = 370
playerY = 480
playerDX = 0

#enemy
enemyImg = []
enemyX =[]
enemyY =[]
enemyDX =[]
enemyDY =[]
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0 ,650))
    enemyY.append(random.randint(50 ,150))
    enemyDX.append(0.8)
    enemyDY.append(40)

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletDX = 0
bulletDY = 3
bullet_state = 'ready'

#player score
score =0

def player(x,y):
    screen.blit(playerImg , (x , y)) #blit is used to draw  , with parameters (image variable , (x , y ))

def enemy(x,y ,i):
    screen.blit(enemyImg[i] , (x , y)) #blit is used to draw  , with parameters (image variable , (x , y ))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg , (x+45 , y + 10))

def isCollision(enemyX , enemyY ,bulletX , bulletY):
    distance= math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY ,2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:

    #rgb = Red ,Green ,Blue
    screen.fill((0,0,0))
    #background image
    #screen.blit(background , (0,0))
    for event in pygame.event.get(): #pygame.event.get() inscludes all the events happening inside the pygame
        if event.type == pygame.QUIT: #pygame.QUIT is if a player quited the window or not
            running = False

        #if a keystroke is pressed check wether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #left arrow is pressed
                playerDX = -1
            if event.key == pygame.K_RIGHT: #right arrow is pressed
                playerDX = 1
            if event.key == pygame.K_SPACE: #fires bullet
                if bullet_state is 'ready':
                    #Gets the current x cordinate of the player/spaceship
                    bulletX = playerX
                    fire_bullet(bulletX , bulletY)

        if event.type == pygame.KEYUP:#if the keystroke is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerDX = 0

    #it changes the x-axis of the playerImage
    playerX += playerDX

    #boundaries for space ship ,so it don't go beyond screen (movements)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 678:
        playerX = 678

    #movements of enemy
    for i in range(num_of_enemies):
        enemyX[i] += enemyDX[i]
        if enemyX[i] <= 0:
            enemyDX[i] = 0.8
            enemyY[i] += enemyDY[i]
        elif enemyX[i] >= 678:
            enemyDX[i] =  -0.8
            enemyY[i] += enemyDY[i]
        
            #collision
        collision= isCollision(enemyX[i] , enemyY[i] , bulletX , bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0 ,650)
            enemyY[i] =random.randint(50 ,150)

    enemyX += enemyDX

    #bullet movement
    if bulletY <=0 :
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletDY
    
    enemy(enemyX[i] , enemyY[i] ,i)
    


    #always write after fill and before update
    player(playerX , playerY)


    #updates the screen and any changes done before it
    pygame.display.update()


