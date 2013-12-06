# -*- coding: utf-8 -*-
import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex

import classes.board
import random

class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self,mainloop,2,16)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,26,9)
        
        
    def create_game_objects(self, level = 1):
        
        self.vis_buttons = [1,1,1,1,1,1,1,1,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        s = random.randrange(190, 225)
        v = random.randrange(230, 255)
        h = random.randrange(0, 255)
        color0 = ex.hsv_to_rgb(h,40,230) #highlight 1
        color1 = ex.hsv_to_rgb(h,70,v) #highlight 2
        color2 = ex.hsv_to_rgb(h,s,v) #normal color
        color3 = ex.hsv_to_rgb(h,230,100)
        font_color = ex.hsv_to_rgb(h,255,140)
        #data = [x_count, y_count, letter_count, top_limit, ordered]
        if self.level.lvl == 1:
            data = [26,6,97,123,0,5,0]
        elif self.level.lvl == 2:
            data = [26,6,97,123,0,10,0]
        elif self.level.lvl == 3:
            data = [26,6,97,123,0,15,0]
        elif self.level.lvl == 4:
            data = [26,6,97,123,0,20,0]
            
        elif self.level.lvl == 5:
            data = [26,6,97,123,1,5,0]
        elif self.level.lvl == 6:
            data = [26,6,97,123,1,10,0]
        elif self.level.lvl == 7:
            data = [26,6,97,123,1,15,0]
        elif self.level.lvl == 8:
            data = [26,6,97,123,1,20,0]
            
        elif self.level.lvl == 9:
            data = [26,6,65,91,0,5,0]
        elif self.level.lvl == 10:
            data = [26,6,65,91,0,10,0]
        elif self.level.lvl == 11:
            data = [26,6,65,91,0,15,0]
        elif self.level.lvl == 12:
            data = [26,6,65,91,0,20,0]
            
        elif self.level.lvl == 13:
            data = [26,6,65,91,1,5,0]
        elif self.level.lvl == 14:
            data = [26,6,65,91,1,10,0]
        elif self.level.lvl == 15:
            data = [26,6,65,91,1,15,0]
        elif self.level.lvl == 16:
            data = [26,6,65,91,1,20,0]
            
        if self.level.lvl < 9:
            self.points = data[5] // 5 + (self.level.lvl+3) // 4
        else:
            self.points = data[5] // 5 + (self.level.lvl+3) // 8
        
        """
        if self.level.lvl == 17:
            data = [26,6,97,123,0,5,11]
        elif self.level.lvl == 18:
            data = [26,6,97,123,0,10,11]
        elif self.level.lvl == 19:
            data = [26,6,97,123,0,15,11]
        elif self.level.lvl == 20:
            data = [26,6,97,123,0,20,11]
            
        elif self.level.lvl == 21:
            data = [26,6,97,123,1,5,11]
        elif self.level.lvl == 22:
            data = [26,6,97,123,1,10,11]
        elif self.level.lvl == 23:
            data = [26,6,97,123,1,15,11]
        elif self.level.lvl == 24:
            data = [26,6,97,123,1,20,11]
            
        elif self.level.lvl == 25:
            data = [26,6,65,91,0,5,11]
        elif self.level.lvl == 26:
            data = [26,6,65,91,0,10,11]
        elif self.level.lvl == 27:
            data = [26,6,65,91,0,15,11]
        elif self.level.lvl == 28:
            data = [26,6,65,91,0,20,11]
            
        elif self.level.lvl == 29:
            data = [26,6,65,91,1,5,11]
        elif self.level.lvl == 30:
            data = [26,6,65,91,1,10,11]
        elif self.level.lvl == 31:
            data = [26,6,65,91,1,15,11]
        elif self.level.lvl == 32:
            data = [26,6,65,91,1,20,11]   
        """
        #self.chapters = [1,5,9,13,17,21,25,29,32]
        self.chapters = [1,5,9,13,16]
        self.data = data
        self.layout.update_layout(data[0],data[1])
        self.board.level_start(data[0],data[1],self.layout.scale)
        
        self.word = [chr(x) for x in range(data[2],data[3])]#self.words[random.randrange(0,len(self.words))]
        word_len = 26#len(self.word)

        shuffled = []
        choice_list = self.word[:]
        index_list = [x for x in range(26)]
        lowered = []
        for i in range(data[5]):#picking letters to lower
            index = random.randrange(0,len(index_list))
            lowered.append(choice_list[index_list[index]])
            del(index_list[index])
        random.shuffle(lowered)
        color = ((255,255,255))
        
        #create table to store 'binary' solution 
        self.solution_grid = [1 for x in range(data[0])]
        x = 0
        y = 0
        x2 = (data[0]-len(lowered))//2
        y2 = 3
        j = 0
        
        for i in range(len(self.word)):
            picked = False
            if self.word[i] in lowered:
                picked = True
            if data[4] == 1: 
                h = random.randrange(0, 255, 5)
            else:
                if picked:
                    letter = lowered[j]
                else:
                    letter = self.word[i]
                h = round(9.8*(ord(letter)-data[2]))
            number_color = ex.hsv_to_rgb(h,s,v) #highlight 1
            
            #change y 
            if picked:
                caption = lowered[j]
                self.board.add_unit(x2+j,y2,1,1,classes.board.Letter,caption,number_color,"",data[6])
                self.board.add_door(x,y,1,1,classes.board.Door,"",color,"")
                self.board.units[j].door_outline = True
                self.board.ships[i].highlight = False
                self.board.ships[i].outline_highlight = True
                
                j += 1         
            else:
                caption = self.word[i]
                self.board.add_unit(x,y,1,1,classes.board.Letter,caption,number_color,"",data[6])
                self.board.ships[i].draggable = False
            x += 1
            if x >= data[0]:
                x = 0
                y += 1
        for each in self.board.units:
            self.board.all_sprites_list.move_to_front(each)
        #instruction = self.d["Complete abc"]
        #self.board.add_unit(0,data[1]-2,data[0],2,classes.board.Letter,instruction,color0,"",0)
        #self.board.ships[-1].immobilize()
        #self.board.ships[-1].font_color = font_color
        #if self.lang.lang[0:2] != "en":
        #    self.board.ships[-1].readable = False
        self.outline_all(0,1)     
                 

    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up

    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        result = [" " for i in range(self.data[0])]
        if self.changed_since_check:
            if self.board.grid[0] == self.solution_grid:
                for i in range(len(self.board.ships)):
                    if self.board.ships[i].grid_y == 0:
                        result[self.board.ships[i].grid_x] = self.board.ships[i].value
                if self.word == result:
                    self.update_score(self.points)
                    self.level.next_board()
                else:
                    if self.points > 0:
                        self.points -= 1
                    self.level.try_again()
                    self.changed_since_check = False
            else:
                self.level.try_again(True)
                