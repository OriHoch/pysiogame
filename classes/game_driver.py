# -*- coding: utf-8 -*-
import pygame
import classes.board
import random
import colorsys
import os
import classes.level_controller
import classes.layout
import classes.dialog
    
class GameBase:
    def __init__(self):
        self.screen_tick = 0 #screen frame count
        self.screen_speed = 3 #execute every 3 frames
        self.move_tick = 0 # object motion frame count
        self.move_speed = 5 # move every 3 frames
        self.ai_enabled = False
        self.ai_speed = 10 # move every ai_speed frames
        self.ai_tick = 0 #ai motion frame count
        self.show_msg = False
        self.auto_checking = False
        self.ships_count = 0

    def game_restart(self,screen):
        pass

    def handle(self, event):
        pass
            
    def display(self, screen):
        pass
        
        
class BoardGame(GameBase):
    def __init__(self,mainloop,speaker,config,screen_w,screen_h,x_count,y_count):
        GameBase.__init__(self)
        self.mainloop = mainloop
        self.speaker = speaker
        self.lang = self.mainloop.lang
        self.level.d = self.lang.d
        self.d = self.mainloop.lang.d
        self.dp = self.mainloop.lang.dp
        self.config = config
        self.move = False # used to start moving the square when pressed
        self.direction = [0,0]
        self.ship_id = -1
        self.drag = False #used to control draging objects around
        self.gridpos_now_top = (-1,-1)
        self.gridpos_prev_top = (-1,-1)
        self.x_diff = (-1,-1)
        self.y_diff = (-1,-1)
        self.circle_lock_pos = (0,0)
        self.game_type = "Board"
        self.layout = classes.layout.Layout(mainloop, screen_w, screen_h,x_count,y_count, game_type = self.game_type)
        self.dialog = classes.dialog.Dialog(self)
        self.screen_w=self.layout.screen_w
        self.screen_h=self.layout.screen_h
        self.mainloop.info.reset_buttons()
        self.changed_since_check = True
        self.mouse_entered_new = False
        
        self.active_game = self.mainloop.m.games[self.mainloop.m.active_game_id]
        #print(self.active_game.dbgameid)
        #self.saved_lvl = self.mainloop.m.saved_levels
        #self.saved_lvl[self.active_game.constructor]
        #xupdate        
        #self.level.lvl = self.mainloop.m.saved_levels[self.active_game.game_constructor][str(self.active_game.variant)]
        self.level.lvl = self.mainloop.m.saved_levels[self.active_game.dbgameid]
        #print("self.level.lvl: %d" % self.level.lvl)
        #self.level.lvl = 
        #if one game has more than one category of tasks on different levels - the beginning of a category
        #can be marked on chapter list and jumped between with right click on the next level button
        self.chapters = [1]
        
        #create game board
        self.board = classes.board.Board(self.mainloop,self.layout.x_count,self.layout.y_count,self.layout.scale)
        self.create_game_objects()
        
        #used for a line around game area
        self.line_color = (240, 240, 240)
        self.screen_w = self.board.x_count * self.board.scale
        self.screen_h = self.board.y_count * self.board.scale
        
        self.len_ships = len(self.board.ships)
        self.board.all_sprites_list.move_to_back(self.board.board_bg)
        self.board.board_bg.update(self.board)#in case colour of background changed during game creation
        self.movingsprites = pygame.sprite.RenderPlain((self.board.ship_list))
        self.staticsprites = pygame.sprite.RenderPlain((self.board.unit_list))
        self.cl_grid_line = (240, 240, 240)
        try:
            if self.mainloop.info.hidden == True:
                self.mainloop.info.title_only()
        except:
            pass
        #to make sure game gets updated after starting
        #self.mainloop.redraw_needed[0] = True
        self.mainloop.redraw_needed = [True,True,True]
        self.level.completed = self.mainloop.db.query_completion(self.mainloop.userid, self.active_game.dbgameid, self.level.lvl)
        self.level.update_level_dict()
        
    def board_layout_update(self):
        self.screen_w=self.layout.screen_w
        self.screen_h=self.layout.screen_h
        self.board.scale = self.layout.scale
    
    def say(self,text,voice="1"):
        self.speaker.say(text,voice)
        
    def get_x_count(self,y_count,even=None):
        'method used to calculate the number of horizontal squares needed'
        'to fill all available area making games wider on wide screens'
        'it may make games a little bit harder on larger screens,'
        'patches my mistake to make this game optimized for 1024x786 screens only'
        scale = self.layout.avail_game_h // y_count
        x_count = self.layout.avail_game_w // scale
        if even == None:
            #if number of squares does not matter make it fill whole width rather than height
            return x_count+1
        else:
            m = x_count % 2
            if even == True and m == 0 or even == False and m == 1:
                #if the number we have is the number we need -> return it
                return x_count
            else:
                #else: increase it to make it match the criteria set (why in- and not decrease -> see: even == None)
                return x_count+1
    
    def get_y_count(self,x_count,even=None):
        'method used to calculate the number of horizontal squares needed'
        'to fill all available area making games wider on wide screens'
        'it may make games a little bit harder on larger screens,'
        'patches my mistake to make this game optimized for 1024x786 screens only'
        scale = self.layout.avail_game_w // x_count
        y_count = self.layout.avail_game_h // scale
        if even == None:
            #if number of squares does not matter make it fill whole width rather than height
            return y_count+1
        else:
            m = y_count % 2
            if even == True and m == 0 or even == False and m == 1:
                #if the number we have is the number we need -> return it
                return y_count
            else:
                #else: increase it to make it match the criteria set (why in- and not decrease -> see: even == None)
                return y_count+1
                
    def outline_all(self,color,width,units=True,ships=True):
        #mark to draw outline around all units/ships on the board
        if units == True:
            for each in self.board.units:
                each.set_outline(color,width)
        if ships == True:
            for each in self.board.ships:
                each.set_outline(color,width)
           
    def handle(self, event):
        #if self.show_msg == False:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Change the x/y screen coordinates to grid coordinates
            pos = event.pos
            column = (pos[0] - self.layout.game_left) // (self.layout.width)
            row = (pos[1] - self.layout.top_margin) // (self.layout.height)
            
            if self.ships_count == 1:
                # if only one movable unit found - activate it
                self.board.active_ship = 0
            else:
                #check if we have clicked on any movable unit
                self.board.activate_ship(column,row)
            self.ship_id = self.board.active_ship
            self.mainloop.redraw_needed[0] = True
            if self.ship_id>=0:
                self.changed_since_check = True
                if self.board.ships[self.ship_id].draggable == True:
                    self.drag = True
                self.x_diff = column - self.board.active_ship_pos[0]
                self.y_diff = row - self.board.active_ship_pos[1]
                self.gridpos_prev_top = (column-self.x_diff,row-self.y_diff) #used to store the mouse coords on previous position in grid
                self.gridpos_now_top = (column-self.x_diff,row-self.y_diff)  #used to store current position on grid
                self.board.ships[self.board.active_ship].enable_circle() #dnable drawing circle aim on items
                self.circle_lock_pos = (self.x_diff*self.layout.scale, self.y_diff*self.layout.scale) 
                if self.board.active_val_len > 0 and self.board.ships[self.board.active_ship].readable:
                    if isinstance(self.board.ships[self.board.active_ship].speaker_val, list):                  
                        value = ', '.join(self.board.ships[self.board.active_ship].speaker_val)
                    else:
                        value = self.board.ships[self.board.active_ship].speaker_val
                    self.say(value,6)
 
        elif event.type == pygame.MOUSEMOTION:
            #make sure the current game title is displayed
            if self.mainloop.info.hidden == True:
                self.mainloop.info.buttons_restore()
            if self.mainloop.info.title != self.mainloop.m.games[self.mainloop.m.active_game_id].title:
                self.mainloop.info.reset_titles()
                #self.mainloop.info.title = self.mainloop.m.games[self.mainloop.m.active_game_id].title
                #self.mainloop.info.subtitle = self.mainloop.m.games[self.mainloop.m.active_game_id].subtitle                        
                #self.mainloop.redraw_needed[1] = True
                #print("ok", end=", ")
            if self.drag:
                pos = event.pos #pygame.mouse.get_pos()
                if pos[0] > self.layout.game_left and self.layout.top_margin < pos[1] < self.layout.game_h+self.layout.top_margin: #if still on game board
                    self.mouse_entered_new = False
                    # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0]-self.layout.game_left) // (self.layout.width)
                    row = (pos[1] - self.layout.top_margin) // (self.layout.height)
                    
                    mdir = [0,0] #mouse drag direction
                    
                    if self.gridpos_prev_top != (column-self.x_diff, row-self.y_diff): #on_mouse_enter on a grid square simulation 
                        #mouse entered a new square
                        self.mouse_entered_new = True
                        self.mainloop.redraw_needed[0] = True
                        self.gridpos_prev_top = (column-self.x_diff, row-self.y_diff)
                        column = column - self.x_diff
                        row = row - self.y_diff

                        x_change = column - self.gridpos_now_top[0]
                        y_change = row    - self.gridpos_now_top[1]
                        
                        if -1 <= x_change <= 1 and -1 <= y_change <= 1:
                            mdir = [x_change, y_change]
                        #else if mouse is out of the range try to follow in one direction
                        else:
                            if x_change >= 1 and (self.gridpos_now_top[0] != column-self.x_diff):
                                mdir[0] = 1
                            elif x_change <= -1: #is smaller than -1
                                mdir[0] = -1
                            if y_change >= 1 and (self.gridpos_now_top[1] != column-self.y_diff):
                                mdir[1] = 1
                            elif y_change <= -1: #is smaller than -1
                                mdir[1] = -1
                            
                        if mdir[0] != 0 or mdir[1] != 0:
                            self.board.move(self.ship_id,*mdir)
                            self.board.ships[self.ship_id].turn(mdir)
                            self.gridpos_now_top = self.board.active_ship_pos
                            #self.circle_lock_pos = ((self.board.active_ship_pos[0]+x_diff)*self.layout.scale,(self.board.active_ship_pos[1]+y_diff)*self.layout.scale) 
                            self.circle_lock_pos = (self.x_diff*self.layout.scale, self.y_diff*self.layout.scale)
                        #self.moved()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.drag:
                self.drag = False
                self.board.ships[self.board.active_ship].disable_circle()
                self.mainloop.redraw_needed[0] = True

        elif event.type == pygame.KEYDOWN and self.len_ships > self.ship_id >= 0 and self.board.ships[self.ship_id].keyable:
            if   event.key == pygame.K_LEFT:  self.direction[0] = -1
            elif event.key == pygame.K_RIGHT: self.direction[0] =  1
            elif event.key == pygame.K_UP:    self.direction[1] = -1
            elif event.key == pygame.K_DOWN:  self.direction[1] =  1
            
            self.check_direction_kdown()
            
                
        elif event.type == pygame.KEYUP:
            if   event.key == pygame.K_LEFT:  self.direction[0] = 0
            elif event.key == pygame.K_RIGHT: self.direction[0] = 0
            elif event.key == pygame.K_UP:    self.direction[1] = 0
            elif event.key == pygame.K_DOWN:  self.direction[1] = 0

            self.check_direction_kup()
            
                
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
            if self.changed_since_check or self.show_msg == True:
                self.mainloop.redraw_needed[0] = True
                self.mainloop.redraw_needed[1] = True
                if self.show_msg == False:
                    self.mainloop.info.btns[0].img = self.mainloop.info.btns[0].img_2
                    self.mainloop.redraw_needed[1] = True
                    self.check_result()
                else:
                    self.show_msg = False
                    self.level.next_board_load()
                self.changed_since_check = False

    def check_direction_kdown(self):
        if self.direction[0] != 0 or self.direction[1] != 0: 
            self.move = True
            self.changed_since_check = True
            self.board.ships[self.ship_id].turn(self.direction)
            self.mainloop.redraw_needed[0] = True
            
    def check_direction_kup(self):
        if self.direction == [0,0]:
            self.move = False
        else:
            self.board.ships[self.ship_id].turn(self.direction)
            self.mainloop.redraw_needed[0] = True
            
    def process_keydown(self):
        self.move_tick += 1 # if key pressed execute this every move_speed frames
        if self.move_tick > self.move_speed:
            if self.move:
                self.move_tick = 0
                self.board.move(self.ship_id,self.direction[0],self.direction[1])
                self.after_keydown_move()
                self.mainloop.redraw_needed[0] = True
            
        self.screen_tick += 1 # used to limit the display update rate, without limiting responsivenes to key presses
        if self.screen_tick >= self.screen_speed:
            self.screen_tick = 0
            
    def after_keydown_move(self):
        pass
        
    def process_ai(self):
        #process ai and move unit if arrow button is pressed
        if self.show_msg == False:
            self.process_keydown()
            if self.ai_enabled == True:
                self.ai_tick += 1 # if key pressed execute this every move_speed frames
                if self.ai_tick > self.ai_speed:
                    self.ai_walk()
                    self.mainloop.redraw_needed[0] = True
                    self.ai_tick = 0

    def update(self,game):
        self.mainloop.game_bg.fill((255,255,255))
        l = self.layout
        if self.show_msg == False:

            #update the grid with new locations and colours
            self.board.update_ships(self.circle_lock_pos)
            
            #Draw all the spites
            self.board.all_sprites_list.draw(game)
            #self.board.sprites_to_draw.draw(game)
        else:
            self.dialog.update(game)
            
        if self.board.draw_grid:
            pygame.draw.line(self.mainloop.game_bg,self.line_color,[self.screen_w+self.layout.game_left-self.layout.menu_w-0,0],[self.screen_w+self.layout.game_left-self.layout.menu_w-0,self.screen_h],1)
            pygame.draw.line(self.mainloop.game_bg,self.line_color,[self.layout.game_left-self.layout.menu_w,self.screen_h],[self.screen_w+self.layout.game_left-self.layout.menu_w-1,self.screen_h],1)
        

    def update_score(self, points):
        userid = self.mainloop.userid
        new_score = self.mainloop.db.increase_score(userid, points)
        if new_score != None:
            self.mainloop.sb.set_score(new_score)
            self.mainloop.sb.update_me = True
            
        
    def check_result(self):
        pass