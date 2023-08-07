import sys, time, os
import pygame
from data.code.player import Player
from threading import Timer
from data.code.island import Island
from data.code.button import Button
from data.code.crafting import CraftingMenu
from data.code.battle import finalBattle
from data.code.mainMenu import MainMenu

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((384, 500))
        pygame.display.set_caption("One Minute Shark Attack")
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.player = Player(self)

        self.stime = time.time()
        self.timeout = False

        print(pygame.font.get_fonts())
        self.font = pygame.font.SysFont("freesansbold", 32)
        self.timeText = self.font.render(f"{int(1 - round(time.time() - self.stime)/60)}:{60 - round(time.time() - self.stime)%60}", True, 'white')


        self.tiles = pygame.sprite.Group()

        self.island = Island(self)
        self.island.mapToTiles()

        self.wood = 0
        self.stone = 0

        self.woodText = self.font.render(f"wood: {self.wood}", True, 'white')
        self.stoneText = self.font.render(f"stone: {self.stone}", True, 'white')

        self.WoodButton = Button('Wood', (128, 50), (0, 450), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.font)
        self.StoneButton = Button('Stone', (128, 50), (128, 450), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.font)
        self.CraftButton = Button('Craft', (128, 50), (256, 450), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.font)

        self.woodSpears = 0
        self.stoneSpears = 0

        self.craft = CraftingMenu(self)

        self.sub = None
        self.battle = finalBattle(self)

        self.mainMenu = MainMenu(self)





    def timer(self):
        print('Shark attack')
        self.timeout = True


    def draw(self):
        self.screen.blit(self.island.islandImage, (0,0))
        self.tiles.draw(self.screen)
        if not self.timeout:
            self.screen.blit(self.timeText, self.timeText.get_rect(center=(192, 384)))
            self.screen.blit(self.woodText, (50, 400))
            self.screen.blit(self.stoneText, (250, 400))
            self.WoodButton.draw(self.screen)
            self.StoneButton.draw(self.screen)
            self.CraftButton.draw(self.screen)


    def updateButtons(self):
        if self.WoodButton.pressed:
            self.island.selection = 'tree'
        if self.StoneButton.pressed:
            self.island.selection = 'stone'
        if self.CraftButton.pressed:
            self.craft.draw()


    def events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self.mainMenu.draw()
        t = Timer(59, self.timer)
        t.start()
        while True:
            self.island.mouseCoords()
            self.timeText = self.font.render(
                f"{int(1 - round(time.time() - self.stime) / 60)}:{60 - round(time.time() - self.stime) % 60}", True,
                'white')
            self.woodText = self.font.render(f"wood: {self.wood}", True, 'white')
            self.stoneText = self.font.render(f"stone: {self.stone}", True, 'white')
            self.screen.fill((52, 177, 235))



            self.draw()
            #print(self.woodSpears)
            if self.timeout:
                #print('works')
                for t in self.tiles:
                    t.image = t.oimage
                    t.finished = True
                self.screen.fill((52, 177, 235))
                self.draw()
                #self.island.update()
                #print(self.woodSpears)
                pygame.image.save(self.screen, 'data/scr.png')
                self.sub = self.screen
                self.battle.draw(self)

            if not self.timeout:
                self.island.click()
                self.island.update()
            self.updateButtons()

            self.events()
            pygame.display.flip()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    g = Game()
    g.run()