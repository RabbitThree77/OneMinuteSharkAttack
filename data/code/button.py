import pygame

class Button():
    def __init__(self, text, size, position,color, colorH, colorP, font):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)

        self.color = color
        self.colorH = colorH
        self.colorP = colorP
        self.font = font
        self.text = text

        self.pressed = False

    def isPressed(self):
        m = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        if m[0] and self.rect.collidepoint(mpos) and not self.pressed:
            self.pressed = True
            s = pygame.mixer.Sound("data/sound/click.wav")
            s.play()
        elif not m[0] and self.rect.collidepoint(mpos):
            self.pressed = False

    def draw(self, screen):
        mpos = pygame.mouse.get_pos()
        self.isPressed()
        if self.rect.collidepoint(mpos):
            self.image.fill(self.colorH)
        if self.pressed:
            self.image.fill(self.colorP)
        elif not self.rect.collidepoint(mpos):
            self.image.fill(self.color)


        screen.blit(self.image, self.rect)
        t = self.font.render(self.text, True, 'white')
        screen.blit(t, t.get_rect(center=self.rect.center))

