import pygame, sys, time
from data.code.button import Button

class Item:
    def __init__(self, name, costW, costS, item, font, game, pos):
        self.name = name
        self.costW = costW
        self.costS = costS
        self.item = item
        self.font = font
        self.game = game
        self.pos = pos

        self.craftPressed = False
        x,y = pos

        nameText = self.font.render(self.name, True, 'white')

        matText = self.font.render(f"{self.costW} wood, {self.costS} stone", True, 'white')
        countText = self.font.render(f"You have {self.item}x", True, 'white')

        backg = pygame.Surface((nameText.get_width() + 50, nameText.get_height() + 200))
        backg.fill((194, 142, 93))
        br = matText.get_rect(topleft=(x, y + 25)).center
        br = backg.get_rect(center=br)

        self.craftButton = Button('Craft', (128, 50), (br.midbottom[0] - 64, br.midbottom[1] - 55), (168, 94, 50),
                                  (196, 118, 71), (153, 87, 47), self.font)


    def draw(self, position, screen):
        x,y = position



        nameText = self.font.render(self.name, True, 'white')

        matText = self.font.render(f"{self.costW} wood, {self.costS} stone", True, 'white')
        countText = self.font.render(f"You have {self.item}x", True, 'white')

        backg = pygame.Surface((nameText.get_width()+50, nameText.get_height()+200))
        backg.fill((194, 142, 93))
        br = matText.get_rect(topleft = (x, y+25)).center
        br = backg.get_rect(center = br)



        nr = nameText.get_rect(center = (br.midtop[0], br.midtop[1]+16))



        screen.blit(backg, br)
        screen.blit(nameText, nr)
        screen.blit(matText, (x, y+25))
        screen.blit(countText, (x+15, y+50))
        self.craftButton.draw(screen)

        #self.checkCraft()

    def checkCraft(self, ):
        if self.craftButton.pressed and not self.craftPressed:
            self.craftPressed = True
            if self.game.wood >= self.costW and self.game.stone >= self.costS:
                self.game.wood -= self.costW
                self.game.stone -= self.costS
                self.item += 1
                #print(self.item is self.game.woodSpears)
        if not self.craftButton.pressed:
            self.craftPressed = False
        return self.item


class CraftingMenu:
    def __init__(self, game):
        self.game = game
        self.font = game.font
        self.stone = game.stone
        self.wood = game.wood

        self.buyW = Item("Wood spear", 2, 0, game.woodSpears, self.font, game, (25, 200))
        self.buyS = Item("Stone spear", 2, 2, game.stoneSpears, self.font, game, (200, 200))

        self.back = Button("Back", (128, 50), (0, 0), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.font)





    def draw(self):
        self.run = True
        self.back.pressed = False
        while self.run:
            self.game.woodText = self.font.render(f"wood: {self.game.wood}", True, 'white')
            self.game.stoneText = self.font.render(f"stone: {self.game.stone}", True, 'white')
            self.game.timeText = self.font.render(
                f"{int(1 - round(time.time() - self.game.stime) / 60)}:{60 - round(time.time() - self.game.stime) % 60}", True,
                'white')

            self.game.screen.fill((245, 204, 127))



            self.buyW.draw((25, 200), self.game.screen)
            self.buyS.draw((200, 200), self.game.screen)
            self.back.draw(self.game.screen)

            self.game.woodSpears = self.buyW.checkCraft()
            self.game.stoneSpears = self.buyS.checkCraft()

            if self.back.pressed:
                self.run = False
                self.game.CraftButton.pressed = False
                print(self.game.timeout)
            if self.game.timeout:
                self.game.CraftButton.pressed = False
                self.run = False

            self.game.screen.blit(self.game.woodText, (130, 16))
            self.game.screen.blit(self.game.stoneText, (225, 16))
            self.game.screen.blit(self.game.timeText, self.game.timeText.get_rect(center=(192, 490)))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.game.CraftButton.pressed = False
                        self.run = False

            pygame.display.flip()

