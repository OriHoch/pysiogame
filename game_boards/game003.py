# -*- coding: utf-8 -*-
from __future__ import with_statement
import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import os, sys
import classes.board
import random
import pygame
import pickle

    
class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,2,2)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,11,9)
        
        
    def create_game_objects(self, level = 1):
        self.board.draw_grid = False

        s = 20 #random.randrange(20, 40)
        v = random.randrange(200, 255)
        h = random.randrange(0, 255)
        white = ((255,255,255))
        red = ((255,0,0))
        color = white #ex.hsv_to_rgb(h,s,v)
        #self.file_data = ["en_GB",1,0,0,"", 0, 0]
        
        #flag_files = self.mainloop.lang.flag_files
        self.lang_titles = self.mainloop.lang.lang_titles
        self.all_lng = self.mainloop.lang.all_lng
        self.ok_lng = self.mainloop.lang.ok_lng
        if self.mainloop.config.google_trans_languages == True:
            self.languages = self.all_lng
        else:
            self.languages = self.ok_lng
            
        door_pos = []
        
        self.lang_count = len(self.languages)

        data = [22,self.lang_count + 2]
        
        max_x_count = self.get_x_count(data[1],even=True)
        if max_x_count > self.lang_count*2 and max_x_count > 24:
            data[0] = max_x_count
        self.data = data
        
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        
        self.layout.update_layout(data[0],data[1])
        
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        
        self.center = self.data[0] // 2
        x = self.center - self.lang_count
        
        self.board.add_unit(0,0,data[0],2,classes.board.Label,self.d["Language"]+":",color,"",25)
        self.board.units[-1].font_color = (255,75,0,0)
        #self.board.units[-1].font_color = (136,201,255)
        #self.board.units[-1].color = (70,70,70)
        
        lang = self.mainloop.config.settings["lang"]
        lng_index = 0

        for i in range(self.lang_count):
            #self.board.add_unit(x+i*2,3,2,2,classes.board.ImgShip,"",white,flag_files[i])
            #self.board.add_unit(self.center-5,3+i,10,1,classes.board.Letter,self.lang_titles[i],red,"",2)
            self.board.add_unit(self.center-5,i+2,10,1,classes.board.Letter,self.lang_titles[i],white,"",2)
            if self.all_lng[i] == lang:
                lng_index = i
                


        for each in self.board.ships:
            each.immobilize()
            each.readable = False
            each.outline = False
            each.font_color = (55,105,5)
            
        self.reselect(lng_index)
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            active = self.board.active_ship
            if event.button == 1:
                toggle = False
                if active >= 0:
                    #change language
                    if self.lang.lang != self.languages[active]:
                        self.change_language(self.languages[active],self.lang_titles[active],active)
                
                    if toggle:                    
                        self.mainloop.fullscreen_toggle(self.mainloop.info)
                    else:
                        self.level.load_level()

    def change_language(self,lng,lng_title,lang_id):
        self.mainloop.db.save_user_lang(lng)
        self.mainloop.config.settings["lang"] = lng
        self.lang.lang = lng
        self.lang.get_lang_attr()
        self.d = self.lang.d
        self.mainloop.speaker.restart_server()
        self.mainloop.m.lang_change()
        #self.board.units[0].set_pos(self.board.active_ship_pos)
        self.mainloop.redraw_needed = [True,True,True]
        self.say(lng_title)
        self.mainloop.info.update_fonts()
        self.reselect(lang_id)
        self.mainloop.sb.resize()
        self.mainloop.sb.update_me = True
        
    def reselect(self,selectid):
        for each in self.board.ships:
            if each.unit_id != selectid:
                each.font_color = (40,40,40)
                each.font = self.board.font_sizes[2]
                #each.color = (255,255,255)
                #each.initcolor = (255,255,255)
            else:
                #each.color = (255,200,255)
                #each.initcolor = (255,0,0)
                each.font_color = (130,0,180)
                each.font = self.board.font_sizes[0]
            each.update_me = True

    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass