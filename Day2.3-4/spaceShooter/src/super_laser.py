import pygame

class SuperLaser:
    def __init__(self, shipRect, laserSpeed_x, laserSpeed_y):
        self.image = pygame.image.load("ArtAssets7/laser.png")
        self.image_rect = self.image.get_rect()
        self.speed_x = laserSpeed_x
        self.speed_y = laserSpeed_y

    def move(self):

        self.image_rect.bottom -= self.speed_x
        self.image_rect.top -= self.speed_y



