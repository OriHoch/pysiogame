# -*- coding: utf-8 -*-

import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import pygame
import classes.board
import random
import os


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,11,9)
        
    def create_game_objects(self, level = 1):
        self.board.draw_grid = False
        s = random.randrange(30, 50)
        v = random.randrange(230, 255)
        h = random.randrange(0, 225)
        white = (255,255,255)
        card_color = ex.hsv_to_rgb(h+10,s-25,v)
        font_color = ex.hsv_to_rgb(h,255,140)
        scheme = "white"
        if self.mainloop.scheme is not None:
            if self.mainloop.scheme.dark:
                scheme = "black"

        data = [15,10]
        
        #stretch width to fit the screen size
        data[0] = self.get_x_count(data[1],even=False)
        if data[0]<15:
            data[0]=15
        self.data = data
        self.x_offset = (data[0]-9)//2
        
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        
        t_area = "½ah"
        self.shape_names = self.lang.solid_names
        
        if self.lang.lang in ["ru","he"]:
            self.shape_namesp = self.lang.dp["solid_names"]
        else:
            self.shape_namesp = self.shape_names
        #self.shape_names = ["Cube", "Square Prism","Triangular Prism", "Square Pyramid", "Triangular Pyramid",  "Sphere",    "Cylinder",    "Cone",      "Torus"]
        self.shape_areas = ["6a²",   "2a² + 4aH",   "ah + 3aH",         "a² + 2as",       "½ah + 3/2 × as",      "4πr²",      "2πr² + 2πrH", "πr² + πrs", "4π² × R × r"]
        self.shape_circ =  ["a³",    "a²H",         "½ah × H",          "⅓a² × H",        "ah/6 × H",            "4/3 × πr³", "πr²H",        "⅓πr²H",     "2π² × R × r²"]

        x = self.x_offset
        y = 0
        
        for i in range(9):
            self.board.add_unit(x,y,1,1,classes.board.Letter,self.shape_names[i],white,"",2)
            self.board.ships[-1].speaker_val = self.shape_namesp[i]
            self.board.ships[-1].speaker_val_update = False
            self.board.ships[-1].font_color=(255,255,255,0)
            x += 1

        x=(data[0]-4)//2
        y=1
        
        self.shape_count = len(self.board.ships) 
        
        #Card
        self.board.add_unit(x-2,y+1,9,2,classes.board.Letter,self.shape_names[0],card_color,"",2)

        self.board.ships[-1].speaker_val = self.shape_namesp[0]
        self.board.ships[-1].speaker_val_update = False
        
        self.board.add_unit(x+2,y+3,5,1,classes.board.Letter,self.d["surface area:"],card_color,"",3)
        self.board.add_unit(x+2,y+4,5,1,classes.board.Label,"6a"+chr(178),card_color,"",3)
        self.board.add_unit(x+2,y+5,5,1,classes.board.Letter,self.d["volume:"],card_color,"",3)
        self.board.add_unit(x+2,y+6,5,1,classes.board.Label,"a"+chr(179),card_color,"",3)

        #frame size 288 x 216        
        self.board.add_unit(x-2,y+3,4,4,classes.board.MultiImgSprite,self.shape_names[0],card_color,os.path.join("schemes",scheme,"flashcard_solids.jpg"),row_data=[9,1])
        self.board.ships[-1].speaker_val = self.shape_namesp[0]
        self.board.ships[-1].speaker_val_update = False
        
        self.board.add_door(x-2,y+1,9,6,classes.board.Door,"",card_color,"")
        
        self.board.add_door(x-2,0,9,1,classes.board.Door,"",card_color,os.path.join("schemes",scheme,"flashcard_solids_72.jpg"))
        self.board.units[2].door_outline = True
        self.board.units[2].perm_outline_color = font_color
        self.board.all_sprites_list.move_to_front(self.board.units[2])
        self.board.all_sprites_list.move_to_front(self.board.units[3])
        
        self.slide = self.board.ships[self.shape_count+3]
        self.slide.build_frame_flow(self.shape_count+3) 
        self.slide.correction = True
        self.slide.perm_outline = True
        self.slide.perm_outline_color = font_color
        
        for each in self.board.ships:
            each.immobilize()
            each.font_color = font_color
            
        for each in self.board.units:
            each.font_color = font_color
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        if event.type == pygame.MOUSEBUTTONUP:
            self.active_item = self.board.ships[self.board.active_ship]
            if self.active_item.unit_id < self.shape_count:
                self.create_card(self.active_item)

    def create_card(self, active):
        self.board.ships[self.shape_count].value = self.shape_names[active.unit_id]
        self.board.ships[self.shape_count].speaker_val = self.shape_namesp[active.unit_id]
        self.board.ships[self.shape_count].speaker_val_update = False
        self.board.units[0].value = self.shape_areas[active.unit_id]
        self.board.units[1].value = self.shape_circ[active.unit_id]
        self.slide.value = self.shape_names[active.unit_id]
        self.slide.speaker_val = self.shape_namesp[active.unit_id]
        self.slide.speaker_val_update = False

        self.mainloop.redraw_needed[0] = True
        self.slide.set_frame(active.unit_id)
        self.board.active_ship = -1
        
        self.slide.update_me = True
        for i in [0,1]:
            self.board.units[i].update_me = True
        self.board.ships[self.shape_count].update_me = True
        
    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass
