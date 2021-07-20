import pygame, sys
from pygame.locals import*

pygame.init()

FPS = 30

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800,600))

WHITE = (255,255,255)

beardManImg = pygame.image.load("../ArtAssets5/beardManSmall.png")
beardManRect = beardManImg.get_rect()

beardManImgRight = beardManImg
beardManImgLeft = pygame.transform.flip(beardManImg, True, False)
currentBeardMan = beardManImgRight

direction = 'right'
SPEED = 5

while True:
    DISPLAYSURF.fill(WHITE)


    if direction == "right":
        beardManRect.left += 5
        if beardManRect.right >= 790:
            direction = "down"
    elif direction == 'down':
        beardManRect.top += 5
        if beardManRect.bottom >= 590:
            direction = 'left'
            currentBeardMan = beardManImgLeft
    elif direction == 'left':
        beardManRect.left -= 5
        if beardManRect.left <= 10:
            direction = 'up'
    elif direction == 'up':
        beardManRect.top -= 5
        if beardManRect.top <= 10:
            direction = 'right'
            currentBeardMan = beardManImgRight

    DISPLAYSURF.blit(currentBeardMan, beardManRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == K_DOWN:

    pygame.display.update()
    fpsClock.tick(FPS)