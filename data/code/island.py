import pygame
from data.code.tile import Tile, TimedTile

class Island:
    def __init__(self, game):
        self.map = [[0, 0, 0] for i in range(3)]
        self.tiles = {
            'house': ['data/art/house.png', 0.1],
            'tree': ['data/art/tree.png', 5],
            'stone': ['data/art/stone.png', 10]
        }

        print(self.map)
        self.islandImage = pygame.image.load('data/art/tileset.png').convert_alpha()
        self.islandImage = pygame.transform.scale(self.islandImage, (384, 384))
        self.islandRect = self.islandImage.get_rect(topleft=(0,0))
        self.map[1][1] = 'house'
        self.game = game

        self.mx = 0
        self.my = 0

        self.selection = 'tree'

        self.mdown = False
        self.initClick = True

    def update(self):
        m = pygame.mouse.get_pressed()
        if m[0]:

            self.mdown = True
        if not m[0]:
            self.mdown = False
            self.initClick = False
        for t in self.game.tiles:
            if isinstance(t, TimedTile):
                if not t.finished:
                    t.updateTime()
                if t.finished and m[0] and self.islandRect.collidepoint(pygame.mouse.get_pos()):
                    self.mdown = True
                    if t.rect.collidepoint(pygame.mouse.get_pos()):
                        s = pygame.mixer.Sound("data/sound/pickupCoin.wav")

                        match t.buildType:
                            case 'tree':
                                s.play()
                                self.game.wood += 1
                                t.kill()
                                self.map[self.my][self.mx] = 0
                                #print(f'wood: {self.game.wood}')
                            case 'stone':
                                s.play()
                                self.game.stone += 1
                                t.kill()
                                self.map[self.my][self.mx] = 0



    def click(self):
        try:
            m = pygame.mouse.get_pressed()
            if m[0] and self.map[self.my][self.mx] == 0 and self.islandRect.collidepoint(pygame.mouse.get_pos()) and not self.mdown and not self.initClick:
                s = pygame.mixer.Sound("data/sound/hitHurt.wav")
                s.play()
                self.map[self.my][self.mx] = self.selection
                self.mapToTiles()
        except:
            pass


    def mouseCoords(self):
        mpos = pygame.mouse.get_pos()
        self.mx = int(mpos[0]/128)
        self.my = int(mpos[1]/128)

    def mapToTiles(self):
        #print(len(self.game.tiles))
        #self.game.tiles.empty()
        #print(len(self.game.tiles))
        for y,row in enumerate(self.map):
            for x, tile in enumerate(row):
                brk = False
                if tile != 0:
                    t = TimedTile(self.tiles[tile][0], (x*128, y*128), 128, self.tiles[tile][1], tile)
                    for tt in self.game.tiles:
                        if tt.cr.topleft == (x*128, y*128):
                            brk = True
                    if not brk:
                        if not self.game.tiles.has(t):
                            self.game.tiles.add(t)

