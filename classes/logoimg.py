# -*- coding: utf-8 -*-

import pygame
import os

class LogoImg(pygame.sprite.Sprite):
    'holds the logo in top left corner'
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([140,123])
        self.image.fill((60,60,60))

        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
        self.img_src = "logo.png"
        self.img = self.image
        self.img_pos = (0,0)
        try:
            self.img = pygame.image.load(os.path.join('res', 'images', self.img_src)).convert_alpha()
        except:
            pass
        self.update()
        self.image.set_colorkey((255,75,0))
        

    def update(self):
        self.image.blit(self.img, self.img_pos) 