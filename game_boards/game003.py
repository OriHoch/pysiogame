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
        color = white #ex.hsv_to_rgb(h,s,v)
        self.file_data = self.mainloop.config.settings
        flag_files = self.mainloop.lang.flag_files # ["flag_uk.png","flag_us.png","flag_pl.png","flag_gr.png","flag_es.png","flag_pt.png","flag_fr.png","flag_it.png","flag_de.png","flag_ru.png","flag_fi.png"]
        self.lang_titles = self.mainloop.lang.lang_titles #["English","American English","Polski","Ελληνικά","Español","Português","Français","Italiano","Deutsch","Русский","Suomalainen"]
        self.all_lng = self.mainloop.lang.all_lng #["en_gb", "en_us", "pl", "gr", "es","pt","fr","it","de","ru","fi"]
        self.ok_lng = self.mainloop.lang.ok_lng #["en_gb", "en_us", "pl", "gr", "es"]
        if self.mainloop.config.google_trans_languages == True:
            self.languages = self.all_lng
        else:
            self.languages = self.ok_lng
            
        door_pos = []
        
        self.lang_count = len(self.languages)

        data = [22,15]
        
        max_x_count = self.get_x_count(data[1],even=True)
        if max_x_count > self.lang_count*2 and max_x_count > 24:
            data[0] = max_x_count
        self.data = data
        
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        
        self.layout.update_layout(data[0],data[1])
        
        self.center = self.data[0] // 2
        x = self.center - self.lang_count
        
        #determining the position of markers for current language and speaker settings
        for i in range(self.lang_count):
            if self.lang.lang == self.languages[i]:
                door_pos.append(i)
                self.file_data[0] = self.languages[i]
                break
        
        if self.mainloop.speaker.talkative:
            door_pos.append(1)
        else:
            door_pos.append(0)
            
        if self.mainloop.config.google_trans_languages:
            door_pos.append(1)
        else:
            door_pos.append(0)
            
        if self.mainloop.config.fullscreen:
            door_pos.append(1)
        else:
            door_pos.append(0)
            
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        
        self.board.add_door(x+door_pos[0]*2,3,2,2,classes.board.Door,"",white)
        self.board.add_door(self.center - door_pos[1]*2,7,2,2,classes.board.Door,"",white)
        #self.board.add_door(self.center - door_pos[2]*2,11,2,2,classes.board.Door,"",white)
        self.board.add_door(data[0]-1-door_pos[2],13,1,1,classes.board.Door,"",white)
        self.board.add_door(data[0]-1-door_pos[3],14,1,1,classes.board.Door,"",white)
        
        #username box frame
        self.board.add_door(self.center-4,11,8,1,classes.board.Door,self.file_data[4],white,font_size = 2)
        self.home_square = self.board.units[-1]
        self.home_square.font_color = (0,127,0)

        for i in range(5):
            self.board.units[i].door_outline = True
            
        self.board.add_unit(0,0,data[0],2,classes.board.Label,self.d["Preferences"],color,"",0)

        self.board.add_unit(0,6,data[0],1,classes.board.Label,self.d["Reader"]+":",color,"",2)
        self.board.add_unit(self.center - 2,7,2,2,classes.board.ImgShip,"",white,"flag_green.png")
        self.board.add_unit(self.center,7,2,2,classes.board.ImgShip,"",white,"flag_red.png")

        self.board.add_unit(0,10,data[0],1,classes.board.Label,self.d["UserName"]+":",color,"",2)

        self.board.add_unit(2,13,data[0]-4,1,classes.board.Label,self.lang.d["enable_untranslated"],color,"",3)
        self.board.add_unit(data[0]-2,13,1,1,classes.board.ImgShip,"",white,"flag_green.png")
        self.board.add_unit(data[0]-1,13,1,1,classes.board.ImgShip,"",white,"flag_red.png")

        self.board.add_unit(2,14,data[0]-4,1,classes.board.Label,self.lang.d["Fullscreen:"],color,"",3)
        self.board.add_unit(data[0]-2,14,1,1,classes.board.ImgShip,"",white,"flag_green.png")
        self.board.add_unit(data[0]-1,14,1,1,classes.board.ImgShip,"",white,"flag_red.png")

        self.board.add_unit(0,2,data[0],1,classes.board.Label,self.d["Language"]+":",color,"",2)
        
        
        

        for i in range(self.lang_count):
            self.board.add_unit(x+i*2,3,2,2,classes.board.ImgShip,"",white,flag_files[i])


        for each in self.board.ships:
            each.immobilize()
            each.readable = False
            each.outline = False
        
        for each in self.board.units:
            each.door_outline = True
            self.board.all_sprites_list.move_to_front(each)
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            active = self.board.active_ship
            if event.button == 1:
                toggle = False
                if active == 0:
                    #turn on espeak
                    self.mainloop.speaker.talkative = True
                    self.file_data[1] = 1
                    self.board.units[1].set_pos(self.board.active_ship_pos)
                elif active == 1:
                    #turn off espeak
                    self.mainloop.speaker.talkative = False
                    self.file_data[1] = 0
                    self.board.units[1].set_pos(self.board.active_ship_pos)
                elif active == 2:
                    #turn on google translated languages
                    self.mainloop.config.google_trans_languages = True
                    self.file_data[2] = 1
                    self.board.units[2].set_pos(self.board.active_ship_pos)
                elif active == 3:
                    #turn off google translated images - reset to English to avoid out of index problem
                    self.mainloop.config.google_trans_languages = False
                    self.file_data[2] = 0
                    self.board.units[2].set_pos(self.board.active_ship_pos)
                    if self.lang.lang not in self.ok_lng:
                        self.change_language(self.languages[0],self.lang_titles[0],0)
                elif active == 4:
                    #turn on fullscreen display
                    if self.mainloop.config.fullscreen == False:
                        toggle = True
                    else:
                        toggle = False
                        
                    #self.mainloop.config.fullscreen = True
                    self.file_data[3] = 1
                    self.board.units[3].set_pos(self.board.active_ship_pos)
                elif active == 5:
                    #turn off fullscreen display
                    if self.mainloop.config.fullscreen == True:
                        toggle = True
                    else:
                        toggle = False
                    #self.mainloop.config.fullscreen = False
                    self.file_data[3] = 0
                    self.board.units[3].set_pos(self.board.active_ship_pos)
                elif active > 5:
                    #change language
                    if self.lang.lang != self.languages[active - 6]:
                        self.change_language(self.languages[active - 6],self.lang_titles[active - 6],active-6)
                if active >= 0:
                    self.save_settings_file()
                    if toggle:                    
                        self.mainloop.fullscreen_toggle(self.mainloop.info)
                    else:
                        self.level.load_level()
            
        if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN:
            lhv = len(self.home_square.value)      
            self.changed_since_check = True   
            if event.key == pygame.K_BACKSPACE:
                if  lhv > 0:
                    self.home_square.value = self.home_square.value[0:lhv-1]
            else:
                char = event.unicode
                if len(char)>0 and lhv < 25:
                    self.home_square.value += char
            self.home_square.font_color = (127,0,0)
            self.home_square.update_me = True
            self.mainloop.redraw_needed[0] = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.file_data[4] = self.home_square.value
            self.home_square.font_color = (0,127,0)
            self.home_square.update_me = True
            self.mainloop.redraw_needed[0] = True
            self.mainloop.user_name = self.home_square.value
            self.save_settings_file()
                    
    def change_language(self,lng,lng_title,file_data_0):
        self.lang.lang = lng
        self.lang.get_lang_attr()
        self.d = self.lang.d
        self.mainloop.speaker.restart_server()
        self.mainloop.m.lang_change()
        self.file_data[0] = file_data_0
        self.board.units[0].set_pos(self.board.active_ship_pos)
        self.mainloop.redraw_needed = [True,True,True]
        self.say(lng_title)
        self.mainloop.info.update_fonts()
                        
    def save_settings_file(self):
        'save language settings to file'
        self.mainloop.config.settings = [self.lang.lang, self.file_data[1], self.file_data[2], self.file_data[3], self.file_data[4],self.file_data[5],self.file_data[6]]
        self.mainloop.config.save_settings()
                
    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass