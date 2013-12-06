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
        w_len = len(self.word)
        n2lower = w_len//2
        
        img_src = "hippopotamus.jpg"#"caterpillar.jpg"
        
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
        
        
        
        shuffled = []
        choice_list = self.word[:]
        index_list = [x for x in range(w_len)]
        lowered = []
        for i in range(n2lower):#picking letters to lower
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
        print(lowered)
        for i in range(w_len):
            picked = False
            if self.word[i] in lowered:
                picked = True
            """
            if data[4] == 1: 
                h = random.randrange(0, 255, 5)
            else:
                if picked:
                    letter = lowered[j]
                else:
                    letter = self.word[i]
                h = round(9.8*(ord(letter)-data[2]))
            """
            #number_color = ex.hsv_to_rgb(h,s,v) #highlight 1
            
            #change y 
            if picked:
                print(j)
                caption = lowered[j]
                #self.board.add_unit(x2+j,y2,1,1,classes.board.Letter,caption,number_color,"",data[6])
                self.board.add_door(2+i,img_size + img_top + 5,1,1,classes.board.Door,"",color,"")
                self.board.units[j].door_outline = True
                #self.board.ships[i].highlight = False
                #self.board.ships[i].outline_highlight = True
                self.board.add_unit(2+i,img_size + img_top + 5,1,1,classes.board.Letter,caption,white,"",0)
                self.board.ships[-1].highlight = False
                self.board.ships[-1].outline_highlight = True
                self.board.ships[-1].set_outline(color = border_color, width = 1)
                j += 1         
            else:
                caption = self.word[i]
                #self.board.add_unit(x,y,1,1,classes.board.Letter,caption,number_color,"",data[6])
                self.board.add_unit(2+i,img_size + img_top + 5,1,1,classes.board.Letter,caption,white,"",0)
                self.board.ships[-1].highlight = False
                self.board.ships[-1].outline_highlight = True
                self.board.ships[-1].set_outline(color = border_color, width = 1)
                self.board.ships[i].draggable = False
            x += 1
            if x >= data[0]:
                x = 0
                y += 1
        #for each in self.board.units:
        #    self.board.all_sprites_list.move_to_front(each)
            
            
        
        
        self.board.add_unit(img_left,img_top,img_size,img_size,classes.board.ImgShip,"",color,os.path.join('art4apps', 'animals',img_src))
        #self.board.ships[-1].set_outline(color = [200,0,0], width = 1)
        self.board.ships[-1].immobilize()
        """
        for i in range(len(self.word)):
            self.board.add_unit(2+i,img_size + img_top + 5,1,1,classes.board.Letter,self.word[i],white,"",0)
            self.board.ships[-1].highlight = False
            self.board.ships[-1].outline_highlight = True
            self.board.ships[-1].set_outline(color = border_color, width = 1)
        """
        """
        img_src = "hippopotamus.jpg"
        self.board.add_door(17,1,15,17,classes.board.Door,"",white,"",font_size = 2)
        self.board.add_unit(18,2,13,13,classes.board.ImgShip,"",color,os.path.join('art4apps', 'animals',img_src))
        for i in range(len(self.words[1])):
            self.board.add_unit(18+i,16,1,1,classes.board.Letter,self.words[1][i],white,"",0)
        """ 
        #self.outline_all(1,1)
        #self.board.units[-1].outline_highlight = False
        
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up

    def update(self,game):
        game.fill(self.color)
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass