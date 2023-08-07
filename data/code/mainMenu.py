import pygame
from data.code.button import Button
from data.code.tutorial import Tutorial

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.title = self.game.font.render("One Minute\n Shark Attack", True, 'white')
        self.start = Button("Start", (128, 50), (192-64, 250), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.game.font)
        self.tutorial = Button("Tutorial", (128, 50), (192-64, 325), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.game.font)
        self.t = Tutorial(self.game)

    def draw(self):
        run = True

        while run:
            self.screen.fill((52, 177, 235))

            self.screen.blit(self.title, self.title.get_rect(center = (192, 100)))
            self.start.draw(self.screen)
            self.tutorial.draw(self.screen)

            if self.start.pressed:
                run = False

            if self.tutorial.pressed:
                self.t.draw()
                self.tutorial.pressed = False

            self.game.events()

            pygame.display.flip()
