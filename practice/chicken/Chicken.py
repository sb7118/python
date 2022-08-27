from tkinter import Y
import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800 ,600))

#caption 
pygame.display.set_caption('egg-pie')
#icon
icon = pygame.image.load('chicken.png')
pygame.display.set_icon(icon)

#chicken
chicken = pygame.image.load('chicken.png')
chickenX = 300
chickenY = 400 
chickenDX = 0

#egg
egg = pygame.image.load('egg.png')
eggX = random.randint(0 ,650)
eggY = random.randint(50 , 60)
eggDX = 0.9
eggDY = 1

#score 
score = 0
font = pygame.font.Font('freesansbold.ttf' ,32)

textX = 10
textY = 10

def show_score(x,y):
    Score = font.render('score : ' + str(score) , True , (255,255,255))
    screen.blit(Score , (x,y))


def hen(x,y):
    screen.blit(chicken , (x,y))

def Egg(x,y):
    screen.blit(egg , (x, y))

def fetch(eggX , eggY , chickenX , chickenY):
    distance = math.sqrt((math.pow(eggX - chickenX ,2)) + (math.pow(eggY - chickenY ,2)))
    if distance < 40:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keystroke for chicken's movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                chickenDX = -3
            if event.key == pygame.K_RIGHT:
                chickenDX = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                chickenDX = 0

    #1D movement
    chickenX += chickenDX
    eggY += eggDY

    #fetch
    fetch_egg = fetch(eggX , eggY , chickenX , chickenY)
    if fetch_egg:
        eggY = random.randint(50 , 60)
        eggX = random.randint(0 ,650)
        score += 1

    #boundaries for chicken
    if chickenX <= 0:
        chickenX = 0
    elif chickenX >= 640:
        chickenX = 640

    hen(chickenX ,chickenY)
    Egg(eggX , eggY)
    show_score(textX ,textY)
    #updates da screen
    pygame.display.update()