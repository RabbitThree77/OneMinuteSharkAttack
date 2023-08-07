import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle, img, type):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (9, 33))
        self.image = pygame.transform.rotate(self.image, -angle-90)
        self.type = type

        self.rect = self.image.get_rect(center = pos)
        self.pos = list(pos)
        self.angle = angle

        self.speed = 3

    def move(self):
        rad = math.radians(self.angle)
        dx = math.cos(rad) * self.speed
        dy = math.sin(rad) * self.speed
        self.pos[0] += dx
        self.pos[1] += dy
        self.rect.center = self.pos

