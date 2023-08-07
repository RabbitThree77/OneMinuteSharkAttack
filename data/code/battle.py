import copy
import sys
import time
import pygame
from pygame.math import Vector2
import math
from data.code.bar import Bar
from data.code.win import Win
from data.code.bullet import Bullet

class Shark:
    def __init__(self):
        self.image = pygame.image.load('data/art/shark.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 92))
        #self.image.fill('white')
        self.rect = self.image.get_rect(center = (192, 250))

        self.oimage = self.image
        self.pos = Vector2((192, 250))
        self.offset = Vector2(0, -150)
        self.angle = 0

        self.hp = 75
        self.hpBar = Bar(384, self.hp, self.hp, (192, 50))


    def orbit(self):
        self.angle += 0.75
        self.image = pygame.transform.rotozoom(self.oimage, -self.angle-90, 1)
        #self.image.fill('white')
        offsetRot = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center = self.pos+offsetRot)

class finalBattle:
    def __init__(self, game):
        self.hp = 25
        s = copy.copy(game.screen)
        self.sub = game.screen.subsurface(0, 0, 384, 384)
        self.islandImg = pygame.image.load("data/scr.png").convert()
        self.islandImg = self.islandImg.subsurface((0, 0, 384, 384))
        self.islandImg = pygame.transform.scale(self.islandImg, (128, 128))
        self.islandRect = self.islandImg.get_rect(center = (192, 250))

        self.clock = pygame.time.Clock()

        self.game = game

        #ui setup
        self.mrect = pygame.Rect(0, 425, 384, 75)
        self.title = game.font.render("Spears", True, 'white')
        self.titleRect = self.title.get_rect(center = (self.mrect.midtop[0], self.mrect.midtop[1]+16))
        #print(game.woodSpears)
        self.wtext = game.font.render(f"wooden: {game.woodSpears}", True, 'white')
        self.stext = game.font.render(f"stone: {game.stoneSpears}", True, 'white')

        self.shark = Shark()
        self.bullets = pygame.sprite.Group()
        self.t = 0

        self.name = self.game.font.render("Shark", True, "white")




    def draw(self, game):
        run = True
        self.game = game
        #print(self.game.woodSpears)

        #time.sleep(1)
        self.islandImg = pygame.image.load("data/scr.png").convert()
        self.islandImg = self.islandImg.subsurface((0, 0, 384, 384))
        self.islandImg = pygame.transform.scale(self.islandImg, (128, 128))
        self.islandRect = self.islandImg.get_rect(center=(192, 250))
        self.wtext = self.game.font.render(f"wooden: {self.game.woodSpears}", True, 'white')
        self.stext = self.game.font.render(f"stone: {self.game.stoneSpears}", True, 'white')

        #self.islandImg = copy.copy(self.game.sub)#pygame.transform.scale(self.game.sub, (192, 192))
        print('battle start')
        while run:
            self.t += 1
            self.game.screen.fill((52, 177, 235))

            self.game.screen.blit(self.islandImg, self.islandRect)
            self.game.screen.blit(self.shark.image, self.shark.rect)
            self.shark.orbit()
            self.game.screen.blit(self.shark.hpBar.image, self.shark.hpBar.rect)
            #self.shark.hp -= 1
            self.shark.hpBar.update(self.shark.hp)
            self.bullets.draw(self.game.screen)
            #print(len(self.bullets))
            for b in self.bullets:
                if b.rect.left < 0 or b.rect.right > 384:
                    b.kill()
                if b.rect.top < 0 or b.rect.bottom > 500:
                    b.kill()
                b.move()
                if self.shark.rect.colliderect(b.rect):
                    m1 = pygame.mask.from_surface(b.image)
                    m2 = pygame.mask.from_surface(self.shark.image)
                    if m2.overlap(m1, (b.rect.x - self.shark.rect.x, b.rect.y - self.shark.rect.y)):
                        b.kill()
                        s = pygame.mixer.Sound("data/sound/sdmg.wav")
                        s.play()
                        if b.type == 'wood':
                            self.shark.hp -= 5
                        if b.type == 'stone':
                            self.shark.hp -= 10


            if self.shark.hp <= 0:
                self.win = Win(self.game, True)
                self.win.draw()

            if self.game.woodSpears <= 0 and self.game.stoneSpears <= 0 and len(self.bullets) <= 0:
                pygame.display.flip()
                time.sleep(1)
                self.win = Win(self.game, False)
                self.win.draw()




            pygame.draw.rect(self.game.screen, (245, 204, 127), self.mrect)
            self.game.screen.blit(self.title, self.titleRect)
            self.game.screen.blit(self.wtext, (10, 450))
            self.game.screen.blit(self.stext, self.stext.get_rect(topright = (374, 450)))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.MOUSEBUTTONDOWN and self.t > 60:
                    #print(ev.button)
                    if ev.button == 1 and self.game.woodSpears > 0:
                        self.t = 0
                        self.game.woodSpears -= 1
                        mpos = pygame.mouse.get_pos()
                        angle = math.atan2(mpos[1] - 250, mpos[0] - 192)
                        angle = math.degrees(angle)
                        b = Bullet((192, 250), angle, 'data/art/woodSpear.png', 'wood')
                        self.bullets.add(b)
                    if ev.button == 3 and self.game.stoneSpears > 0:
                        self.t = 0
                        self.game.stoneSpears -= 1
                        mpos = pygame.mouse.get_pos()
                        angle = math.atan2(mpos[1] - 250, mpos[0] - 192)
                        angle = math.degrees(angle)
                        b = Bullet((192, 250), angle, 'data/art/stoneSpear.png', 'stone')
                        self.bullets.add(b)
                    self.wtext = self.game.font.render(f"wooden: {self.game.woodSpears}", True, 'white')
                    self.stext = self.game.font.render(f"stone: {self.game.stoneSpears}", True, 'white')


            pygame.display.flip()
            self.clock.tick(60)
