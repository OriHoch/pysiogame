# -*- coding: utf-8 -*-

import pygame
import os

class LogoImg(pygame.sprite.Sprite):
    'holds the logo in top left corner'
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([123,123])
        self.image.fill((70,70,70))

        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
        self.img_src = "logo.png"
        self.img = self.image
        self.img_pos = (0,0)
        try:
            self.img = pygame.image.load(os.path.join('images', self.img_src)).convert_alpha()
        except:
            pass
        self.update()

    def update(self):
        self.image.blit(self.img, self.img_pos)