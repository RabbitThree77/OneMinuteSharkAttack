import sys

import pygame
from data.code.button import Button

class Win:
    def __init__(self, game, won):
        self.screen = game.screen
        self.game = game

        self.exit = Button("Exit", (128, 50), (128, 350), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.game.font)
        self.text = game.font.render("You Lost!", True, 'white')
        if won:
            self.text = game.font.render("You Won!", True, 'white')

    def draw(self):
        run = True

        while run:
            self.screen.fill((245, 204, 127))

            self.exit.draw(self.screen)
            self.screen.blit(self.text, self.text.get_rect(center = (192, 75)))
            self.game.events()

            if self.exit.pressed:
                pygame.quit()
                sys.exit()

            pygame.display.flip()