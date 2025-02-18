import pygame

class Ship:

    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT):
        self.image = pygame.transform.scale(pygame.image.load("ArtAssets7/ship.png"), (80,80))
        self.rect = self.image.get_rect()

        self.moveSpeed = 20
        self.leftLimit = 10
        self.rightLimit = WINDOWWIDTH - 10
        self.bottomLimit = WINDOWHEIGHT - 10
        self.topLimit = 10

        self.setStartPos()

    
    def move(self, left, right, up, down):
        if left and self.rect.left >= self.leftLimit:
            self.rect.left -= self.moveSpeed
        if right and self.rect.right <= self.rightLimit:
            self.rect.right += self.moveSpeed
        if up and self.rect.top >= self.topLimit:
            self.rect.top -= self.moveSpeed
        if down and self.rect.bottom <= self.bottomLimit:
            self.rect.bottom += self.moveSpeed
        
    def setStartPos(self):
        xCoord = (self.rightLimit + self.leftLimit)/2
        yCood = self.bottomLimit - self.rect.height /2

        self.rect.center = (xCoord, yCood)
         

