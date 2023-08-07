import pygame
from data.code.button import Button


class Tutorial:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.f = pygame.font.Font(None, 16)

        self.text = [
            "A shark is approaching your island!",
            "You need to gather wood and stone to craft spears.",
            "Click on one of the buttons\n at the bottom of the screen to select a material and",
            "wait until it finishes construction. Then collect it by clicking.",
            "Go into the crafting menu to create a spear and repeat the process.",
            "Good Luck."

        ]
        self.back = Button("Back", (128, 50), (0, 0), (168, 94, 50), (196, 118, 71), (153, 87, 47), self.game.font)
        self.run = True

    def draw(self):
        self.run = True
        self.back.pressed = False
        while self.run:
            self.screen.fill((245, 204, 127))

            self.game.events()
            for y,d in enumerate(self.text):
                t = self.f.render(d, True, 'white')
                self.screen.blit(t, t.get_rect(center = (192, y*32+100)))
            self.back.draw(self.screen)
            if self.back.pressed:
                print(self.run)
                self.run = False
                break

            pygame.display.flip()