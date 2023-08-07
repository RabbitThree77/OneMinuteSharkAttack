import pygame

class Bar:
    def __init__(self, width, max, num, center):
        self.image = pygame.Surface((width, 25))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = center)
        self.num = num
        self.max = max
        self.width = width
        self.center = center

    def update(self, num):
        self.num = num
        #max ... width
        #num ... x
        w = self.width * num / self.max
        if num < 0:
            self.image = pygame.Surface((1, 25))
            self.image.fill('red')
            self.rect = self.image.get_rect(center=self.center)
        else:
            self.image = pygame.Surface((w, 25))
            self.image.fill('red')
            self.rect = self.image.get_rect(center=self.center)

