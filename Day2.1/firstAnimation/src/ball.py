import pygame, sys
from pygame import rect

from pygame.locals import*
from pygame.sprite import collide_rect

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((800,600))
pygame.display.set_caption('Ball game')


location = [100,100]

location2 = [400, 500]
    
speed_x = 10
speed_y = 5
speed_y2 = 12
speed_x2 = 5



play = False


Ball1 = pygame.Rect(100, 100, 60, 60)
Ball2 = pygame.Rect(200, 200, 60, 60)


while True:

    color = (255, 0, 0)
    color2 = (0,255, 130)

    SCREEN.fill((50,100,150))

    

    collisions = Ball1.colliderect(Ball2)


    if play == True :
        #color = (255, 0, 0)
        location[0] += speed_x
        location[1] += speed_y
        location2[0] += speed_x2
        location2[1] += speed_y2

        if collisions:

            #color = (255,255,255)

            if (location2[0] + 30 < location[0]):

                speed_x *= -1
                speed_y *= -1
                speed_x2 *= -1
                speed_y2 *= -1
            if (location2[1] < location[1] + 30):
                speed_x *= -1
                speed_y *= -1
                speed_x2 *= -1
                speed_y2 *= -1


                """if (location[0] < location2[0]) and (location[1] < location2[1]):
                    speed_x *= -1
                    speed_y *= -1
                    #speed_x2 *= -1
                    speed_y2 *= -1
                if (location[0] > location2[0]) and (location[1] > location2[1]):
                    speed_x *= -1
                    #speed_y *= -1
                    speed_x2 *= -1
                    speed_y2 *= -1

                #if (location[0] > location2[0]) and (location[1] < location2[1]):"""



        if (location[0] > 740):
            speed_x = -10
            #color = (155, 100, 155)
        elif (location[0] < 0):
            speed_x = 10
            #color = (0, 140, 255)
        elif (location[1] < 0):
            speed_y = 5
            #color = (190, 43, 100)
        elif (location[1] > 540):
            speed_y = -5
            #color = (255, 50, 130)
        elif (location2[0] > 740):
            speed_x2 = -12
        elif (location2[0] < 0):
            speed_x2 = 12
        elif (location2[1] < 0):
            speed_y2 = 5
        elif (location2[1] > 540) :
            speed_y2 = - 5


    Ball1.x = location[0]
    Ball1.y = location[1]
    Ball2.x = location2[0]
    Ball2.y = location2[1]



    pygame.draw.ellipse(SCREEN, color, Ball1)
    pygame.draw.ellipse(SCREEN, color2, Ball2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                location[0] += 50
                play = True
            if event.key == K_LEFT:
                location[0] -= 50

    pygame.display.update()
    clock.tick(60)
