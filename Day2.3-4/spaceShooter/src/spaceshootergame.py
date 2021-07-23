# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:26:21 2019

@author: J. Tyler McGoffin
"""

import pygame, sys
import numpy as np
from pygame import draw
from pygame.locals import *
from pygame.time import Clock

from ship import Ship
from laser import Laser
from asteroid import Asteroid
from background import Background
from super_laser import SuperLaser

#Set up window and frame rate variables
FPS = 30
WINDOWWIDTH = 500
WINDOWHEIGHT = 700

#Set up some Color variables
BLACK = (0, 0, 0)
NAVYBLUE = (0, 0, 128)
DARKPURPLE = (100, 0, 100)
WHITE = (255, 255, 255)
DARKGRAY = (100, 100, 100)

#Start the game
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT #True globals
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Space Shooter")
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    showStartScreen()
    
    while True:
        runGame()
        showGameOverScreen()

def runGame():

    score = 0
    lives = 3
    levelUp = False

    levels = 1

    score_super_firing = 100

    playerShip = Ship(WINDOWWIDTH, WINDOWHEIGHT)
    leftHeld = False
    rightHeld = False
    upHeld = False
    downHeld = False
    firing = False
    super_firing = False

    lasers = initializeObjects(20)
    laserIndex = 0
    laserSpeed = 10
    fireRate = 4


    asteroids = initializeObjects(25)
    spawnRate = 1
    minAsteroidSpeed = 1
    maxAsteroidSpeed = 6
    asteroidIndex = 0


    

    backgroundObject =  Background("background", WINDOWHEIGHT)
    paralaxObject = Background("paralax", WINDOWHEIGHT)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_a or event.key == K_LEFT:
                    leftHeld = True
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = True
                elif event.key == K_w or event.key == K_UP:
                    upHeld = True
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = True
                elif event.key == K_SPACE:
                    firing = True
                elif event.key == K_RETURN:
                    super_firing = True
                
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    leftHeld = False
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = False
                elif event.key == K_w or event.key == K_UP:
                    upHeld = False
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = False
                elif event.key == K_SPACE:
                    firing = False
        #print(super_firing)

        if score % 10 == 0 and levelUp:
            minAsteroidSpeed += 2
            maxAsteroidSpeed += 2
            laserSpeed += 2
            spawnRate += 1

            levelUp = False
        elif score % 10 != 0:
            levelUp = True


        if firing:
            #print("i: " + str(laserIndex) + "; l: " + str(len(lasers)))

            lasers[laserIndex] = Laser(playerShip.rect, laserSpeed)
            firing = False
            laserIndex += 1
            if laserIndex >= len(lasers):
                laserIndex = 0
            

        if super_firing and score >= score_super_firing:
            for l in range(10):
                rect = playerShip.rect.copy()
                rect.x = 50*l 
                lasers[l] = Laser(rect, laserSpeed)
                rect.y -= 50 
                lasers[l + 10] = Laser(rect, laserSpeed)
            laserIndex = 0
            super_firing = False
            score_super_firing += 30
        
        if np.random.randint(0, FPS/spawnRate) == 0:
            asteroids[asteroidIndex] = Asteroid(WINDOWWIDTH, WINDOWHEIGHT, np.random.randint(minAsteroidSpeed,maxAsteroidSpeed))
            asteroidIndex += 1
            if asteroidIndex >= len(asteroids):
                asteroidIndex = 0

        if lives < 1 :
            showGameOverScreen()


        playerShip.move(left = leftHeld, right = rightHeld, up = upHeld, down = downHeld)

        backgroundObject.move()
        paralaxObject.move()
        
        for laser in lasers:
            if laser != None:
                laser.move()
        for asteroid in asteroids:
            if asteroid != None:
                asteroid.move()

        for currentAsteroidIndex, asteroid in enumerate(asteroids):
            if asteroid != None:
                for currentLaserIndex, laser in enumerate(lasers):
                    if laser != None:
                        if laser.rect.colliderect(asteroid.rect):
                            asteroids[currentAsteroidIndex] = None
                            lasers[currentLaserIndex] = None
                            score += 1

                if playerShip.rect.colliderect(asteroid.rect):
                    lives -= 1
                    if lives > 0:
                        playerHit()
                        playerShip.setStartPos()
                        asteroids = initializeObjects(25)
                        lasers = initializeObjects(20)
                    else:
                        return

                    break

        DISPLAYSURF.fill(BLACK)
        draw(backgroundObject.image, backgroundObject.rect)
        draw(paralaxObject.image, paralaxObject.rect)
        drawLasers(lasers)
        drawAsteroids(asteroids)
        draw(imageSurf = playerShip.image, imageRect =  playerShip.rect)

        drawHUD(lives, score)
        level_message(levels)


        powerGraphic(score, score_super_firing)

        
        if score > 155 :


            levels, asteroids, lasers, score = level(levels, playerShip, asteroids, lasers)
            minAsteroidSpeed = 1
            maxAsteroidSpeed = 6
            asteroidIndex = 0
            asteroids = initializeObjects(25)
            spawnRate = 1
            laserSpeed = 10
            lives = 3

            level_message(levels)

    
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def level_message(levels):
    level_font = BASICFONT.render("Level: "+ str(levels), True, WHITE)
    level_rect =  level_font.get_rect()
    level_rect.midtop = (50, 30)
    DISPLAYSURF.blit(level_font, level_rect)

    #pygame.display.update()
    #pygame.time.wait(2000)


def level(levels, playerShip, asteroids, lasers):
    levels += 1
    playerShip.setStartPos()
    asteroids = initializeObjects(25)
    lasers = initializeObjects(20)
    score = 0
        

    return levels, asteroids, lasers, score

def powerGraphic(score, score_super_firing):

    delta = score_super_firing - score

    power_rect_yellow = pygame.Rect(450, 400, 40, 50)
    power_rect_Surf_yellow = pygame.Surface((40, 50))
    power_rect_orange = pygame.Rect(450, 350, 40, 50)
    power_rect_Surf_orange = pygame.Surface((40,50))
    power_rect_red = pygame.Rect(450, 300, 40, 50)
    power_rect_Surf_red = pygame.Surface((40,50))

    power_rect_Surf_red.fill(pygame.Color(0,0,0))

    power_rect_Surf_orange.fill(pygame.Color(0,0,0))

    power_rect_Surf_yellow.fill(pygame.Color(0,0,0))

    if (delta < 1):

        power_rect_Surf_red.fill(pygame.Color(255,0,0))

        
    if (delta < 20):

        power_rect_Surf_orange.fill(pygame.Color(255,165,0))


    if delta < 40:

        power_rect_Surf_yellow.fill(pygame.Color(255,255,0))


    DISPLAYSURF.blit(power_rect_Surf_yellow, power_rect_yellow)
    DISPLAYSURF.blit(power_rect_Surf_orange, power_rect_orange)
    DISPLAYSURF.blit(power_rect_Surf_red, power_rect_red)

    

def drawHUD(lives, score):
    healthBarSurf = BASICFONT.render("Ships remaining: "+ str(lives), True, WHITE)
    healthBarRect =  healthBarSurf.get_rect()
    healthBarRect.topleft = (10,10)
    draw(healthBarSurf, healthBarRect)

    scoreSurf = BASICFONT.render(" Asteroids destroyed: "+str(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topright = (WINDOWWIDTH - 10, 10)
    draw(scoreSurf, scoreRect)


def playerHit():
    hitSurf = BASICFONT.render("You've been destroyed!", True, WHITE)
    hitRect = hitSurf.get_rect()
    hitRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
    draw(hitSurf, hitRect)

    pygame.display.update()
    pygame.time.wait(2000)


def drawLasers(lasers):
    for laser in lasers:
        if laser != None:
            draw(laser.image, laser.rect)

def drawAsteroids(asteroids):

    for asteroid in asteroids:
        if asteroid != None:
            image, rect = asteroid.draw()
            draw(image, rect)


def initializeObjects(number):
    objects = []
    for x in range(number):
        objects.append(None)

    return objects


def draw(imageSurf, imageRect):
    DISPLAYSURF.blit(imageSurf, imageRect)
    """pygame.display.update()
    FPSCLOCK.tick(FPS)
    #pygame.display.update()"""


def terminate():
    pygame.quit()
    sys.exit()
    
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, (255, 0, 0))
    overSurf = gameOverFont.render('over', True, (0,0,255))
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2, 20)
    overRect.midtop = (WINDOWWIDTH/2, gameRect.height + 20 +25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)

    pygame.display.update()
    pygame.time.wait(2000)


  
def showStartScreen():

    startScreen = pygame.font.Font("freesansbold.ttf", 50)
    startScreenSurf = startScreen.render('SPACE SHOOTER', True, (255,0,0))
    startScreenSurf_2 = startScreen.render("Try stay alive", True, WHITE)
    startScreenRect_2 = startScreenSurf_2.get_rect()
    startScreenRect_2.midtop = (WINDOWWIDTH/2, 500)
    startScreenRect = startScreenSurf.get_rect()
    startScreenRect.midtop = (WINDOWWIDTH/2, 100)

    DISPLAYSURF.blit(startScreenSurf, startScreenRect)
    DISPLAYSURF.blit(startScreenSurf_2, startScreenRect_2)

    pygame.display.update()
    pygame.time.wait(2000)


if __name__ == '__main__':
    main()