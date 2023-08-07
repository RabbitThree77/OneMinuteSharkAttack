import pygame, time, copy

class TimedTile(pygame.sprite.Sprite):
    def __init__(self, image, position, size, buildTime, buildType):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.oimage = copy.copy(self.image)
        self.darkimage = pygame.Surface(self.image.get_size()).convert_alpha()
        self.darkimage.fill((0,0,0, .50*255))
        self.image.blit(self.darkimage, (0, 0))
        #print(self.oimage)
        self.rect = self.image.get_rect(topleft=position)
        self.cr = copy.copy(self.rect)
        self.center = list(self.rect.center)

        self.time = buildTime
        #print(self.time)
        self.stime = time.time()
        self.finished = False

        self.buildType = buildType

        self.csize = 1
        self.size = size
        self.position = position

    def updateTime(self):
        #self.time ... height
        #time.time() - self.stime ... x

        self.image = copy.copy(self.oimage)
        self.csize = self.image.get_height() * (time.time() - self.stime) / self.time

        height = self.image.get_height()-self.csize
        if height < 0:
            height = 0
        print(self.csize)
        print((self.image.get_width(), int(height)))
        self.darkimage = pygame.Surface((self.image.get_width(), int(height))).convert_alpha()
        self.darkimage = pygame.transform.flip(self.darkimage, False, True)
        self.darkimage.fill((0, 0, 0, .50 * 255))

        self.image.blit(self.darkimage, self.darkimage.get_rect(bottomright = self.image.get_size()))

        if time.time() - self.stime > self.time:
            self.finished = True
            self.image = self.oimage


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, position, size):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = position)