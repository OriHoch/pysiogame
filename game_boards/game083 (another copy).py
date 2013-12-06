# -*- coding: utf-8 -*-
import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import classes.board
import random
import os
#import colorsys


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,40,30)
        
        
    def create_game_objects(self, level = 1):
        self.board.draw_grid = True

        color = (234,218,225) #ex.hsv_to_rgb(225,15,235)
        self.color = color
        #font_color = ex.hsv_to_rgb(227,255,50)
        #font_color = (85,0,212)
        font_color = (50,0,150)
        ver_color = (63,45,247)
        border_color = (105,12,100)
        white = (255,255,255)
        data = [10,13]
        #stretch width to fit the screen size
        x_count = self.get_x_count(data[1],even=True)
        if x_count > data[0]:
            data[0] = x_count
            
        self.data = data
        
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        
        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        #self.board.board_bg.initcolor = color
        #self.board.board_bg.color = color
        #self.board.board_bg.update_me = True
        
        base_len = data[0] - 2#(img_left - 1) * 2 + img_size
        img_size = 4
        img_left = (base_len - img_size)//2 + 1
        img_top = 2
        
        self.words = ["caterpillar", "hippopotamus"]
        self.word = self.words[1]
        img_src = "hippopotamus.jpg"#"caterpillar.jpg"
        
        w_len = len(self.word)
        if w_len > 3:
            n_letters = w_len // 2
        else:
            n_letters = w_len
        
        #frame around image
        self.board.add_door(img_left - 1,1,img_size+2,img_size+3,classes.board.Door,"",white,"",font_size = 2)
        self.board.units[-1].image.set_colorkey(None)
        self.board.units[-1].set_outline(color = border_color, width = 1)
        
        #frame around image caption
        self.board.add_door(1,img_size+3,base_len,3,classes.board.Door,"",white,"",font_size = 2)
        self.board.units[-1].image.set_colorkey(None)
        self.board.units[-1].set_outline(color = border_color, width = 1)
        
        #temp frame around word
        w = len(self.word)
        l = (data[0] - w) // 2
        self.board.add_door(l,img_size + img_top + 2,w,1,classes.board.Door,"",white,"",font_size = 2)
        self.board.units[-1].image.set_colorkey(None)
        self.board.units[-1].set_outline(color = border_color, width = 1)
        
        #dummy frame hiding bottome line of the image frame
        self.board.add_door(img_left - 1,img_size + img_top + 1,img_size +2,1,classes.board.Door,"",white,"",font_size = 2)
        self.board.units[-1].image.set_colorkey(None)
        
        
        
        self.board.add_unit(img_left,img_top,img_size,img_size,classes.board.ImgShip,"",color,os.path.join('art4apps', 'animals',img_src))
        #self.board.ships[-1].set_outline(color = [200,0,0], width = 1)
        self.board.ships[-1].immobilize()
        
        for i in range(len(self.word)):
            self.board.add_unit(2+i,img_size + img_top + 5,1,1,classes.board.Letter,self.word[i],white,"",0)
            self.board.ships[-1].highlight = False
            self.board.ships[-1].outline_highlight = True
            self.board.ships[-1].set_outline(color = border_color, width = 1)
        
        """
        img_src = "hippopotamus.jpg"
        self.board.add_door(17,1,15,17,classes.board.Door,"",white,"",font_size = 2)
        self.board.add_unit(18,2,13,13,classes.board.ImgShip,"",color,os.path.join('art4apps', 'animals',img_src))
        for i in range(len(self.words[1])):
            self.board.add_unit(18+i,16,1,1,classes.board.Letter,self.words[1][i],white,"",0)
        """ 
        #self.outline_all(1,1)
        self.board.units[-1].outline_highlight = False
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up

    def update(self,game):
        game.fill(self.color)
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass