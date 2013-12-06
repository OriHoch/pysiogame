# -*- coding: utf-8 -*-

import os
import pygame
class Dialog:
    def __init__(self,game_board):
        self.lines = ["CONGRATULATIONS!!!", "YOU HAVE COMPLETED", "THIS LEVEL"]
        self.lines_game_over = ["GAME OVER!!!"]
        self.game_board = game_board
        self.color = (255,255,255)#(70,70,70)
        if self.game_board.lang.lang in ['en_gb','en_us']:
            self.img_src = "congrats.jpg"
        else:
            self.img_src = "congratsx.jpg"
            
        self.img_src2 = "game_over.jpg"   
        points = int(round((60 * 72 /96)*1.5,0))
        self.font = pygame.font.Font(None, (points))
        self.layout = game_board.layout
        self.layout_update()
        self.level = game_board.level
        
    def layout_update(self):
        self.width = self.layout.game_w
        self.height = self.layout.game_h
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        self.img = pygame.image.load(os.path.join('res', 'images', self.img_src)).convert()
        self.img2 = pygame.image.load(os.path.join('res', 'images', self.img_src2)).convert()
        
        #img2 has the same size
        img_pos_x = self.img.get_rect(centerx=self.image.get_width()//2)
        img_pos_y = self.img.get_rect(centery=self.image.get_height()//2)
        self.img_pos = (img_pos_x[0],img_pos_y[1])
    
    def image_swap(self,img_src):
        pass

        
    def display_lines(self, lines):
        y_pos = 190
        for each in lines:
            text = self.font.render("%s" % (each), 1, (0, 0, 0, 0))
            textpos = text.get_rect(centerx=self.image.get_width()//2)
            self.image.fill((255,255,255))
            self.image.blit(text, (textpos[0],y_pos))
            y_pos += 70

    """
    def display_game_over(self):
        y_pos = 190
        for each in self.lines_game_over:
            text = self.font.render("%s" % (each), 1, (255, 255, 255, 0))
            textpos = text.get_rect(centerx=self.image.get_width()//2)
            self.image.blit(text, (textpos[0],y_pos))
            y_pos += 70
    """

    def update(self,screen):
        self.image.fill(self.color)
        if self.level.dialog_type == 0:
            self.image.blit(self.img, (self.img_pos))
            
        elif  self.level.dialog_type == 1:
            self.image.blit(self.img2, (self.img_pos))
            
        elif  self.level.dialog_type == 2:
            pass
            #self.display_lines(self.lines_game_over)
        screen.blit(self.image, (0,0))