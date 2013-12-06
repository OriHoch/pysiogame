# -*- coding: utf-8 -*-
import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import classes.board
import random
#import colorsys


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,11,9)
        
        
    def create_game_objects(self, level = 1):        
        self.board.draw_grid = False
        
        self.color = (234,218,225)

        font_color = ex.hsv_to_rgb(227,255,50)
        data = [23,15]
        #stretch width to fit the screen size
        x_count = self.get_x_count(data[1],even=None)
        if x_count > 23:
            data[0] = x_count
            
        self.data = data
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        
        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        
        self.board.board_bg.initcolor = self.color
        self.board.board_bg.color = self.color
        self.board.board_bg.update_me = True
        
        self.board.add_unit(0,0,data[0],1,classes.board.Label,"Copyright (C) 2012 - 2013  Ireneusz Imiolek",self.color,"",1)
        self.board.add_unit(0,1,data[0],1,classes.board.Label,"Game ideas: Kamila Roszak-Imiolek, Ireneusz Imiolek",self.color,"",2)
        self.board.add_unit(0,2,data[0],1,classes.board.Label,"",self.color,"",2)
        self.board.add_unit(0,3,data[0],1,classes.board.Label,"Laby, 2010 by Mehdi Cherti(mehdidc)",self.color,"",2)
        self.board.add_unit(0,4,data[0],1,classes.board.Label,"Sounds by various authors who contributed their works to freesound.org",self.color,"",2)
        self.board.add_unit(0,5,data[0],1,classes.board.Label,"Images by various authors who contributed their works to openclipart.org",self.color,"",2)
        self.board.add_unit(0,6,data[0],1,classes.board.Label,"Please view credits.txt for more info about authors of media files used in this project",self.color,"",2)
        self.board.add_unit(0,7,data[0],1,classes.board.Label,"",self.color,"",2)
        self.board.add_unit(0,8,data[0],1,classes.board.Label,"Licence",self.color,"",1)
        self.board.add_unit(0,9,data[0],6,classes.board.Label,["This program is free software: you can redistribute it and/or modify",
        "it under the terms of the GNU General Public License as published by",
        "the Free Software Foundation, either version 3 of the License, or",
        "(at your option) any later version.",
        "You should have received a copy of the GNU General Public License",
        "along with this program.  If not, see <http://www.gnu.org/licenses/>."],self.color,"",2)

        #self.outline_all(1,1)
        for each in self.board.units:
            each.font_color = font_color
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up

    def update(self,game):
        game.fill(self.color)
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass