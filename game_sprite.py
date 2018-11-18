import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_RATE = 60
SPRITE_IMAGE = "./images/enemy2.png"
BACKGROUND_IMAGE = "./images/xingyun1.jpg"


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):
    """game background"""

    def update(self):
        super(BackGround, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
