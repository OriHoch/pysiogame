# -*- coding: utf-8 -*-

import os.path
import pygame.mixer
sounds = pygame.mixer
sounds.init()

sound_12 = '188043__antumdeluge__mouse.ogg'
s12 = sounds.Sound(os.path.join('res', 'sounds', sound_12))

voice = {

    'שלום': sounds.Sound(os.path.join('i18n', 'custom', 'voice', 'he', 'He-Shalom.ogg')),
    'ברכות על החזרה למשחק': sounds.Sound(os.path.join('i18n', 'custom', 'voice', 'he', 'He-Shalom.ogg')),

}