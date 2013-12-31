# -*- coding: utf-8 -*-

import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import classes.board
import random


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,13,11)
        
        
    def create_game_objects(self, level = 1):
        self.board.draw_grid = False

        color = (255,255,255)#(234,218,225) #ex.hsv_to_rgb(225,15,235)
        self.color = color
        font_color = (50,0,150)
        ver_color = (63,45,247)
        data = [17,11]
        #stretch width to fit the screen size
        x_count = self.get_x_count(data[1],even=False)
        if x_count > 17:
            data[0] = x_count
            
        self.data = data
        
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        
        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        self.board.board_bg.initcolor = color
        self.board.board_bg.color = color
        self.board.board_bg.update_me = True
        
        self.board.add_unit(0,3,data[0],3,classes.board.ImgCenteredShip,"",color,'home_logo.png')
        self.canvas = self.board.ships[-1]
        self.canvas.immobilize()
        self.canvas.outline = False
        self.canvas.font = self.canvas.board.font_sizes[4]
        val = "v.%s" % (self.mainloop.config.version)
        text = self.canvas.font.render(val, 1, ver_color)
        y = 0
        x = self.canvas.img_rect.width - self.canvas.font.size(val)[0]-5
        self.canvas.img.blit(text, (x,y))
        
        self.board.add_unit(0,9,data[0],1,classes.board.Label,self.lang.d["Check for newer version..."],color,"",5)
        self.board.add_unit(0,10,data[0],1,classes.board.Label,"http://sourceforge.net/projects/pysiogame/",color,"",2)
        self.board.add_unit(0,8,data[0],1,classes.board.Label,["www.facebook.com/pysiogame",""],color,"",5)
        
        self.board.add_unit(0,7,data[0],1,classes.board.Label,"www.pysiogame.net",color,"",2)
        self.board.units[-1].font_color = (63,99,182)
        
        self.board.units[0].font_color = font_color
        self.board.units[1].font_color = (0,0,255)
        self.board.units[2].font_color = (63,99,182)
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up

    def update(self,game):
        game.fill(self.color)
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass