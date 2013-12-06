# -*- coding: utf-8 -*-
import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex
import classes.simple_vector as sv
import pygame

import copy
import classes.board
import random
from math import pi,cos,acos,sin,asin,sqrt

class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self,mainloop,12,8)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,19,10)
        
        
    def create_game_objects(self, level = 1):
        self.vis_buttons = [1,1,1,1,1,1,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        
        self.hand_id = 0
        self.hand_coords = [[],[]]
        self.board.draw_grid = False
        #create non-movable objects
        color = (255,255,255)
        white = (255,255,255)
        gray = (100,100,100)
        """
        s = random.randrange(100, 150, 5)
        v = random.randrange(230, 255, 5)
        h = random.randrange(0, 255, 5)
        color0 = ex.hsv_to_rgb(h,40,230) #highlight 1
        color1 = ex.hsv_to_rgb(h,s,v) #highlight 2
        color2 = ex.hsv_to_rgb(120,s,v) #highlight 2
        """
        """
        color1 = ex.hsv_to_rgb(0,70,230)
        color3 = ex.hsv_to_rgb(0,255,255)
        color5 = ex.hsv_to_rgb(0,180,240)
        
        color2 = ex.hsv_to_rgb(160,70,230)
        color4 = ex.hsv_to_rgb(160,255,255)
        color6 = ex.hsv_to_rgb(160,180,240)
        """
        color1 = ex.hsv_to_rgb(225,70,230)
        color3 = ex.hsv_to_rgb(225,255,255)
        color5 = ex.hsv_to_rgb(225,180,240)
        color7 = ex.hsv_to_rgb(225,10,255)
        
        color2 = ex.hsv_to_rgb(170,70,230)
        color4 = ex.hsv_to_rgb(170,255,255)
        color6 = ex.hsv_to_rgb(170,180,240)
        color8 = ex.hsv_to_rgb(170,10,255)
        
        self.colors = [color1,color2]
        self.colors2 = [color3,color4]
        self.colors3 = [color5,color6]
        self.colors4 = [color7,color8]
        """
        color1 = pygame.Color(218,122,122,150) #ex.hsv_to_rgb(0,70,230)
        color3 = pygame.Color(200,0,0,200) #ex.hsv_to_rgb(0,255,200)
        
        color2 = pygame.Color(122,145,218,150)#ex.hsv_to_rgb(160,70,230)
        color4 = pygame.Color(0,47,200,200)#ex.hsv_to_rgb(160,255,200)
        """
        #self.color2 = ex.hsv_to_rgb(h,255,170) #contours & borders

        #data = [10,10]
        if self.level.lvl == 1:
            data = [19,10,True,True,False,False,True,False,False,True,True,15]
            h_pool = range(1,13)
            m_pool = range(0,60,15)
        elif self.level.lvl == 2:
            data = [19,10,True,True,False,False,False,True,False,True,True,15]
            h_pool = range(1,13)
            m_pool = range(0,60,5)
        elif self.level.lvl == 3:
            data = [19,10,True,True,False,False,False,False,False,True,True,15]
            h_pool = range(1,13)
            m_pool = range(0,60)
        elif self.level.lvl == 4:
            data = [19,10,True,True,False,False,False,False,False,False,True,20]
            h_pool = range(1,13)
            m_pool = range(0,60)
        elif self.level.lvl == 5:
            data = [19,10,True,True,False,False,False,True,False,False,True,20]
            h_pool = range(1,13)
            m_pool = range(0,60)
        elif self.level.lvl == 6:
            data = [19,10,True,True,False,False,True,False,False,False,True,20]
            h_pool = range(1,13)
            m_pool = range(0,60)
        elif self.level.lvl == 7:
            data = [19,10,True,False,False,False,False,False,False,False,True,25]
            h_pool = range(1,13)
            m_pool = range(0,60)
        elif self.level.lvl == 8:
            data = [19,10,True,False,False,True,False,False,False,False,True,25]
            h_pool = range(1,13)
            m_pool = range(0,60)
            
        self.points = self.level.lvl // 2 + 1
        
        #visual display properties
        self.show_outer_ring = data[2]
        self.show_minutes = data[3]
        self.show_24h = data[4]
        self.show_only_quarters_h = data[5]
        self.show_only_quarters_m = data[6]
        self.show_only_fives_m = data[7]
        self.show_only_spare_variable = data[8]
        self.show_highlight = data[9]
        self.show_hour_offset = data[10]
        
        self.level.games_per_lvl = data[11]
        
        tt = [random.choice(h_pool), random.choice(m_pool)]
        self.target_time = tt
        
        self.text_string = self.lang.time2str(tt[0],tt[1])
        self.time = [6,0]
        self.tm = self.time[:]
        

        self.digits = ["0","1","2","3","4","5","6","7","8","9"]
            
        x_count = self.get_x_count(data[1],even=False)
        if x_count > data[0]:
            data[0] = x_count
            
        self.font_size = 0
        self.data = data
        
        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],self.layout.scale)
        
        self.size = self.board.scale*10
        ans_offset = 10+(data[0]-15)//2
        self.board.add_unit(10,0,data[0]-10,2,classes.board.Label,self.lang.d["Set_clock"],white,"",2)
        self.board.units[-1].font_color = gray
        self.board.add_unit(10,4,data[0]-10,2,classes.board.Label,self.lang.d["Set_clock_instr"],white,"",2)
        self.board.units[-1].font_color = gray
        self.board.add_unit(ans_offset,2,2,1,classes.board.Label,"%02d" % self.target_time[0],white,"",0)
        self.ans_h = self.board.units[-1]
        
        self.board.add_unit(ans_offset+2,2,1,1,classes.board.Label,":",white,"",0)
        self.board.add_unit(ans_offset+3,2,2,1,classes.board.Label,"%02d" % self.target_time[1],white,"",0)
        self.ans_m = self.board.units[-1]
        
        """
        self.board.add_unit(0,10,data[0],1,classes.board.Label,"Quarter past twelve",white,"",2)
        self.time_text = self.board.units[-1]
        self.time_text.align = 1
        self.time_text.font_color = color4
        """
        #self.ans_h.set_outline(color3, 5)
        #self.ans_m.set_outline(color4, 5)
        self.ans_h.align = 2
        self.ans_m.align = 1
        
        self.ans_h.immobilize()
        self.ans_m.immobilize()
        
        self.ans_h.font_color = color3
        self.ans_m.font_color = color4
        
        self.center = [self.size//2,self.size//2]
        self.board.add_unit(0,0,10,10,classes.board.Ship,"",white,"",self.font_size)
        self.clock_canvas = self.board.ships[-1]
        self.board.active_ship = self.clock_canvas.unit_id 
        self.clock_canvas.font = self.clock_canvas.board.font_sizes[2]
        self.clock_canvas.font2 = self.clock_canvas.board.font_sizes[7]
        self.clock_canvas.font3 = self.clock_canvas.board.font_sizes[26]
        self.clock_canvas.immobilize()
        
        self.board.add_unit(10,3,data[0]-10,1,classes.board.Letter,self.text_string,white,"",4)
        self.board.ships[-1].immobilize()
        self.board.ships[-1].font_color = gray
        if self.lang.lang == "ru":
            spk_txt = self.lang.time2spk(tt[0],tt[1])
            self.board.ships[-1].speaker_val = spk_txt
            self.board.ships[-1].speaker_val_update = False
        self.canvas = pygame.Surface([self.size, self.size-1]) 
        self.canvas.fill((255,255,255))
        self.hands_vars()
        self.draw_hands()#data[7](data, canvas, i)
                             
        self.clock_canvas.hidden_value = [2,3]#numbers[i]
        self.clock_canvas.font_color = color2
        self.clock_canvas.painting = self.canvas.copy()
        
        
    def hands_vars(self):
        numbers = [2,2]
        self.angle_step_12 = 2*pi/12
        self.angle_step_60 = 2*pi/60
        
        self.angle_start= -pi/2
        angle_arc_start = -pi/2
        self.r = self.size//3+self.size//10
        
        #rs = [r*0.6, r*0.85,r*0.5]
        self.rs = [self.r*0.6, self.r*0.85,self.r*0.6]
        angle = self.angle_start
        angle_s = angle_arc_start
        angle_e = angle_arc_start + numbers[0]*2*pi/numbers[1]
        #a1 = angle_start + (2*pi/12)*time[0]
        
        
    def draw_hands(self):
        if self.show_hour_offset:
            a1 = self.angle_start + (2*pi/12)*self.time[0] + (self.angle_step_12*(2*pi/60)*self.time[1])/(2*pi)
        else:
            a1 = self.angle_start + (2*pi/12)*self.time[0]
        a2 = self.angle_start + (2*pi/60)*self.time[1]
        self.angles = [a1,a2]
        
        rs = self.rs
        time = self.time
        
        if self.show_outer_ring:
            pygame.draw.circle(self.canvas,self.colors4[1],self.center,int(rs[1]+10),0)
            pygame.draw.circle(self.canvas,self.colors2[1],self.center,int(rs[1]+10),1)
            
        pygame.draw.circle(self.canvas,self.colors4[0],self.center,int(rs[2]+10),0)
        pygame.draw.circle(self.canvas,self.colors2[0],self.center,int(rs[2]+10),1)
        
        if self.show_outer_ring:
            for i in range(60):
                val = str(i+1)
                if self.show_only_quarters_m:
                    if (i+1)%15 != 0:
                        val = ""
                elif self.show_only_fives_m:
                    if (i+1)%5 != 0:
                        val = ""
                if i == 59:
                    val = "0"
                a = self.angle_start + self.angle_step_60*(i+1)
                if self.show_minutes:
                    font_size = self.clock_canvas.font3.size(val)
                    #if self.show_highlight:
                    if not self.show_highlight or (i+1 == time[1] or (time[1] == 0 and i==59)):
                        text = self.clock_canvas.font3.render("%s" % (val), 1, self.colors2[1])
                    else:
                        text = self.clock_canvas.font3.render("%s" % (val), 1, self.colors[1])
                    x3=(rs[1]+30+font_size[1]//2)*cos(a)+self.center[0] - font_size[0] / 2
                    y3=(rs[1]+30+font_size[1]//2)*sin(a)+self.center[1] - font_size[1] / 2
                    #x3=(rs[0]+20 + self.clock_canvas.font.size(val)[0]//2)*cos(a)+center[0]
                    #y3=(rs[0]+20 + self.clock_canvas.font.size(val)[1]//2)*sin(a)+center[1] 
                    self.canvas.blit(text, (x3,y3)) 
                    if self.show_only_quarters_m or self.show_only_fives_m:
                        if (i+1)%15 == 0:
                            marklen = 30
                        elif (i+1)%5 == 0:
                            marklen = 25
                        else:
                            marklen = 15
                    else:       
                        marklen = 25
                else:
                    if (i+1)%15 == 0:
                        marklen = 30
                    elif (i+1)%5 == 0:
                        marklen = 25
                    else:
                        marklen = 15
                if self.show_outer_ring:
                    x1=(rs[1]+10)*cos(a)+self.center[0]
                    y1=(rs[1]+10)*sin(a)+self.center[1]
                    
                    x2=(rs[1]+marklen)*cos(a)+self.center[0]
                    y2=(rs[1]+marklen)*sin(a)+self.center[1]
                    
                    pygame.draw.aaline(self.canvas, self.colors2[1], [x1,y1],[x2,y2])
            
            
        
        for i in range(12):
            val = str(i+1)
            if self.show_only_quarters_h:
                if (i+1)%3 != 0:
                    val = ""
                    
            #a = angle_start + angle_step_12*(i+1)
            a = self.angle_start + self.angle_step_12*(i+1)
            x1=(rs[2]+10)*cos(a)+self.center[0]
            y1=(rs[2]+10)*sin(a)+self.center[1]
            
            x2=(rs[2]+20)*cos(a)+self.center[0]
            y2=(rs[2]+20)*sin(a)+self.center[1]
            
            pygame.draw.aaline(self.canvas, self.colors2[0], [x1,y1],[x2,y2])
            
            font_size = self.clock_canvas.font.size(val)
            if not self.show_highlight or i+1 == time[0]:
                text = self.clock_canvas.font.render("%s" % (val), 1, self.colors2[0])
            else:
                text = self.clock_canvas.font.render("%s" % (val), 1, self.colors[0])
            
            x3=(rs[2]+20+font_size[1]//2)*cos(a)+self.center[0] - font_size[0] / 2
            y3=(rs[2]+20+font_size[1]//2)*sin(a)+self.center[1] - font_size[1] / 2
            self.canvas.blit(text, (x3,y3))
            
            if self.show_24h:
                if i+13 == 24:
                    val = "0"
                    v = 0
                else:
                    val = str(i+13)
                    v = i + 13
                font_size = self.clock_canvas.font2.size(val)
                if not self.show_highlight or v == time[0]:
                    text = self.clock_canvas.font2.render("%s" % (val), 1, self.colors2[0])
                else:
                    text = self.clock_canvas.font2.render("%s" % (val), 1, self.colors[0])
                
                x3=(rs[0]+font_size[1]//2)*cos(a)+self.center[0] - font_size[0] / 2
                y3=(rs[0]+font_size[1]//2)*sin(a)+self.center[1] - font_size[1] / 2
                self.canvas.blit(text, (x3,y3))
        hand_width = [self.r//14,self.r//18]
        start_offset = [self.size//10,self.size//12] 
        
        for i in range(2):
            #angle for line
            angle = self.angles[i]#angle_start + angle_step*i

            x0=self.center[0] - start_offset[i]*cos(angle)
            y0=self.center[1] - start_offset[i]*sin(angle)
            
            # Calculate the x,y for the end point
            x1=rs[i]*cos(angle)+self.center[0]
            y1=rs[i]*sin(angle)+self.center[1]
            
            #x2=h_size[i]*cos(angle-pi/2)+center[0]
            #y2=h_size[i]*sin(angle-pi/2)+center[1]
            #x3=h_size[i]*cos(angle+pi/2)+center[0]
            #y3=h_size[i]*sin(angle+pi/2)+center[1]
            
            x2=hand_width[i]*cos(angle-pi/2)+self.center[0]
            y2=hand_width[i]*sin(angle-pi/2)+self.center[1]
            
            x3=hand_width[i]*cos(angle+pi/2)+self.center[0]
            y3=hand_width[i]*sin(angle+pi/2)+self.center[1]
            
            points = [[x0,y0],[x2,y2],[x1,y1],[x3,y3]]
            shadow = [[x0,y0],[x2,y2],[x1,y1]]
            self.hand_coords[i] = points
            #if i < numbers[0]:
            pygame.draw.polygon(self.canvas, self.colors[i], points, 0)
            pygame.draw.polygon(self.canvas, self.colors3[i], shadow, 0)
            # Draw the line from the center to the calculated end point
            line_through = [[x0,y0],[x1,y1]]

            pygame.draw.aalines(self.canvas, self.colors2[i], True, points)
            pygame.draw.aalines(self.canvas, self.colors2[i], True, line_through)
        pygame.draw.circle(self.canvas,self.colors[0],self.center,self.size//50,0)
        pygame.draw.circle(self.canvas,self.colors2[0],self.center,self.size//50,1)
        pygame.draw.circle(self.canvas,self.colors2[0],self.center,self.size//70,1)
        
        self.clock_canvas.update_me = True
        self.mainloop.redraw_needed[0] = True
        
    def vector_len(self,v):
        return sqrt(v[0]**2 + v[1]**2)
        
    def scalar_product(self,v1,v2):
        return sum([v1[i]*v2[i] for i in range(len(v1))])
        
    def angle(self,v1,v2):
        return self.scalar_product(v1,v2)/(self.vector_len(v1)*self.vector_len(v2))
        
    def is_contained(self, pos, coords_id = 0):
        v0 = sv.Vector2.from_points(self.hand_coords[coords_id][2], self.hand_coords[coords_id][1])
        v1 = sv.Vector2.from_points(self.hand_coords[coords_id][0], self.hand_coords[coords_id][1])
        
        v2 = sv.Vector2.from_points(self.hand_coords[coords_id][2], self.hand_coords[coords_id][3])
        v3 = sv.Vector2.from_points(self.hand_coords[coords_id][0], self.hand_coords[coords_id][3])
        
        v4 = sv.Vector2.from_points(pos, self.hand_coords[coords_id][1])
        v5 = sv.Vector2.from_points(pos, self.hand_coords[coords_id][3])
        
        a1 = 1 - self.angle(v0,v1) #corner 1
        a2 = 1 - self.angle(v2,v3) #corner 2
        
        a3 = 1 - self.angle(v0,v4)#point to arm1 of corner1
        a4 = 1 - self.angle(v1,v4)#point to arm2 of corner1
        
        a5 = 1 - self.angle(v2,v5)#point to arm1 of corner2
        a6 = 1 - self.angle(v3,v5)#point to arm2 of corner2
        
        if (a3+a4) < a1 and (a5+a6) < a2:
            return True
        return False
        
    def current_angle(self, pos,r):
        
        #print(r),
        #print(self.rs[0]),
        cosa = (pos[0] - self.center[0]) / r
        sina = (pos[1] - self.center[1]) / r
        
        if 0 <= cosa <= 1 and -1 <= sina <= 0:
            angle = pi/2 - acos(cosa)
        elif  0 <= cosa <= 1 and 0 <= sina <= 1:
            angle = acos(cosa)+pi/2 #ok
            
        elif  -1 <= cosa <= 0 and 0 <= sina <= 1:
            angle = acos(cosa)+ pi/2 #ok
        elif  -1 <= cosa <= 0 and -1 <= sina <= 0:
            angle = 2*pi+ pi/2 - acos(cosa)
        return angle
                    
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        self.tm = self.time[:]
        
        if event.type == pygame.MOUSEMOTION and self.hand_id > 0:
            pos = [event.pos[0]-self.layout.game_left,event.pos[1]-self.layout.top_margin]
            r = self.vector_len([pos[0]-self.center[0], pos[1] - self.center[1]])
            if r == 0: r = 0.1
            
            if self.hand_id == 1:
                h = (self.current_angle(pos, r)) / self.angle_step_12
                if int(h) == 0:
                    self.tm[0] = 12
                else:
                    self.tm[0] = int(h)
            elif self.hand_id == 2:
                m = (self.current_angle(pos, r)) / self.angle_step_60
                self.tm[1] = int(m)
                if 0 <= self.tm[1] < 5 and 55 <= self.time[1] <= 59:
                    if self.tm[0] == 12:
                        self.tm[0] = 1
                    else:
                        self.tm[0] += 1
                elif 0 <= self.time[1] < 5 and 55 <= self.tm[1] <= 59:
                    if self.tm[0] == 1:
                        self.tm[0] = 12
                    else:
                        self.tm[0] -= 1
                
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            active = self.board.active_ship
            pos = [event.pos[0]-self.layout.game_left,event.pos[1]-self.layout.top_margin]
            if active == 0:
                r = self.vector_len([pos[0]-self.center[0], pos[1] - self.center[1]])
                if r == 0: r = 0.1
                
                self.hand_id = 0
                if self.is_contained(pos, coords_id = 0):
                    self.hand_id = 1
                    #print("activated: %d" % self.hand_id)
                elif self.is_contained(pos, coords_id = 1):
                    self.hand_id = 2
                    #print("activated: %d" % self.hand_id)
                elif self.rs[0]*1.1 > r:
                    h = (self.current_angle(pos, r)) / self.angle_step_12
                    if int(h) == 0:
                        h = 12
                    self.tm[0] = int(h)
                else:
                    m = (self.current_angle(pos, r)) / self.angle_step_60
                    self.tm[1] = int(m)
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.hand_id = 0
            
                #self.is_contained(pos, 1)
        if self.tm != self.time:
            self.time = self.tm[:]
            self.draw_hands()
            self.clock_canvas.painting = self.canvas.copy()
                
                    
        """
        if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN and not self.correct:
            lhv = len(self.home_square.value)      
            self.changed_since_check = True   
            if event.key == pygame.K_BACKSPACE:
                if  lhv > 0:
                    self.home_square.value = self.home_square.value[0:lhv-1]
            else:
                char = event.unicode
                if (len(char)>0 and lhv < 2 and char in self.digits):
                    if lhv == 0:
                        self.home_square.value += char
                    elif lhv == 1:
                        if self.home_square == self.ans_h:
                            if self.show_24h:
                                n = int(self.home_square.value + char)
                                if n > 23:
                                    self.home_square.value = char
                                else: 
                                    self.home_square.value += char
                            else:
                                n = int(self.home_square.value + char)
                                if n > 12:
                                    self.home_square.value = char
                                else: 
                                    self.home_square.value += char
                        if self.home_square == self.ans_m:
                            n = int(self.home_square.value + char)
                            if n > 59:
                                self.home_square.value = char
                            else: 
                                self.home_square.value += char
                elif lhv == 2:
                    self.home_square.value = char
            if self.home_square == self.ans_h and self.time[0] == int(self.ans_h.value):
                self.next_field()
            self.home_square.update_me = True
            self.mainloop.redraw_needed[0] = True
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and self.board.active_ship == self.ans_h.unit_id:
            if self.time[0] == int(self.ans_h.value):
                self.next_field()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.home_square.update_me = True
            if self.board.active_ship == self.ans_h.unit_id:
                self.home_square.perm_outline_width = 5
                self.home_square = self.ans_h
                self.board.active_ship == self.ans_h.unit_id
            elif self.board.active_ship == self.ans_m.unit_id:
                self.home_square.perm_outline_width = 5
                self.home_square = self.ans_m
                self.board.active_ship == self.ans_m.unit_id
            self.home_square.update_me = True
            self.mainloop.redraw_needed[0] = True
        """
        
    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        if self.changed_since_check:
            if self.time == self.target_time:
                self.update_score(self.points)
                self.level.next_board()
            else:
                if self.points > 0:
                    self.points -= 1
                self.level.try_again()
                
                
                
