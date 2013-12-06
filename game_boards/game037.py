# -*- coding: utf-8 -*-

#English Only Game

import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import pygame
import classes.board
import random


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,11,9)
        
        
    def create_game_objects(self, level = 1):
        #create non-movable objects
        self.board.draw_grid = False
        s = random.randrange(30, 80)
        v = random.randrange(200, 255)
        h = random.randrange(0, 225)
        #ex.hsv_to_rgb(h,s,v)
        #rgb = colorsys.hsv_to_rgb(h,s,v)
        self.letter_color = ex.hsv_to_rgb(h,s,v)
        font_color = ex.hsv_to_rgb(h,s,75)
        outline_color =  ex.hsv_to_rgb(h,s+50,v-50)
        frame_color = [255,255,255]
        card_color = ex.hsv_to_rgb(h+10,s-25,v)

        data = [14,10]
        #stretch width to fit the screen size
        data[0] = self.get_x_count(data[1],even=True)
        if data[0]<14:
            data[0]=14
        self.data = data
       
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        #self.prev_item = None
        self.word_list = ['Ant', 'Boat', 'Cat', 'Duck', 'Elephant', 'Fish', 'Grapes', 'House', 'Igloo', 'Jar', 'Key', 'Lion', 'Mouse', 'Notebook', 'Owl', 'Parrot', 'Queen', 'Rabbit', 'Sun', 'Teapot', 'Umbrella', 'Violin', 'Window', 'Xylophone', 'Yarn', 'Zebra']

        x = 0
        x2 = (data[0] - (26 - data[0]))//2
        y = 0
        
        for i in range(26):
            self.board.add_unit(x,y,1,1,classes.board.Letter,chr(i+65)+chr(i+97),self.letter_color,"",2)
            self.board.ships[i].readable = False
            self.board.ships[i].set_outline(outline_color,1)
            x += 1
            if x >= data[0]:
                x = x2
                y = data[1]-1

        x=(data[0]-4)//2
        y=1
        

        #Card
        self.board.add_unit(x,y+1,2,1,classes.board.Label,"A",card_color,"",0)
        self.board.add_unit(x+2,y+1,2,1,classes.board.Label,"a",card_color,"",0)
        self.board.add_unit(x-2,y+1,2,4,classes.board.Label,"A",card_color,"",18)

        #self.board.add_unit(x-2,y+3,2,2,classes.board.Label,"A",card_color,"",13)
        self.board.add_unit(x+4,y+1,2,4,classes.board.Label,"a",card_color,"",18)
        #self.board.add_unit(x+4,y+3,2,2,classes.board.Label,"a",card_color,"",13)
        self.board.add_unit(x,y+2,4,3,classes.board.MultiImgSprite,self.word_list[0],card_color,"flashcard_images.jpg",row_data=[10,8])
        self.board.add_unit(x-2,y+5,8,1,classes.board.Letter,self.word_list[0],card_color,"",2)
        self.board.add_unit(x-2,y+6,8,1,classes.board.Letter,self.word_list[0],card_color,"",15)
        if self.mainloop.lang.lang not in ['en_gb', 'en_us']:
            for i in range(-3,0):
                self.board.ships[i].readable = False
        self.board.add_door(x-2,y+1,8,6,classes.board.Door,"",card_color,"")
        self.board.units[4].door_outline = True
        self.board.all_sprites_list.move_to_front(self.board.units[4])
        self.slide = self.board.ships[26]
        self.slide.build_frame_flow(26) 
        self.slide.correction = True
        self.slide.perm_outline = True
        
        for each in self.board.ships:
            each.immobilize()
            each.font_color = font_color
        for each in self.board.units:
            each.font_color = font_color
        
        self.active_item = self.board.ships[0]
        self.active_item.color = (255,255,255)
        self.prev_item = self.active_item
            
            
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active_item = self.board.ships[self.board.active_ship]
            if self.active_item.unit_id < 26:
                if self.prev_item != None:
                    self.prev_item.color = self.letter_color
                    self.prev_item.update_me = True
                self.active_item.color = (255,255,255)
                self.create_card(self.active_item)
                self.prev_item = self.active_item
                self.mainloop.redraw_needed[0] = True

    def create_card(self, active):
        self.say(active.value[0])
        self.board.units[0].value = active.value[0]
        self.board.units[1].value = active.value[1]
        self.board.units[2].value = active.value[0]
        #self.board.units[3].value = active.value[0]
        self.board.units[3].value = active.value[1]
        #self.board.units[5].value = active.value[1]
        self.board.ships[26].value = self.word_list[active.unit_id]
        self.board.ships[27].value = self.word_list[active.unit_id]
        self.board.ships[28].value = self.word_list[active.unit_id]
        self.mainloop.redraw_needed[0] = True
        self.slide.set_frame(active.unit_id)
        self.board.active_ship = -1
        self.slide.update_me = True
        for i in [0,1,2,3]:
            self.board.units[i].update_me = True
        for i in [26,27,28]:
            self.board.ships[i].update_me = True
        
    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass