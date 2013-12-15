#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pySioGame - Educational Activity Pack
# Copyright (C) 2012-2013  Ireneusz Imiolek

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#standard lib modules
import os, sys
#make the window appear in the top left rather than bottom right
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
import pygame
import threading
import gc

#setting the working directory to the directory of this file
#os.chdir(os.path.dirname(__file__))
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
#local game modules
import classes.config
import classes.dbconn
import classes.loginscreen
import classes.game_driver
import classes.level_controller
import classes.board
import classes.menu
import classes.info_bar
import classes.speaker
import classes.colors
import classes.lang
import classes.logoimg
import classes.score_bar
            
class GamePlay(threading.Thread):
    'The top most class - subclasses the Thread to keep the game and speaker in two different processes'
    'holds main loop'
    def __init__(self,speaker,lang,configo):
        #Call parent's initialization
        threading.Thread.__init__(self)
        
        #Create / set additional top level game objects and mainloop variables
        self.speaker = speaker
        self.lang = lang
        self.config = configo
        
        self.cl = classes.colors.Color()
        
        self.userid = -1

        #!!!!!!!!!!!!!!TO REPLACE!!!!!!!!!!!!!!!!!!
        #'global' score holder used in one game so far
        self.score = 0
        
        
        self.window_states = ["LOG IN", "GAME"]
        self.window_state = self.window_states[0]
        
        
        #As long as this is False the main loop of a state will keep running. If some action sets it to True the loop ends and so does the current state.
        self.done = False
        
        #but if you log out you are still given a chance to log back in... 
        self.done4good = False
        
        self.logged_out = False
        
    def set_init_vals(self):
        self.redraw_needed = [True,True,True]
        self.game_redraw_tick = [0,0,0]
        self.flip_needed = True
        self.init_resize = True
        #menu scrolling speed
        self.menu_speed = 7
        self.menu_tick = 7
        self.done = False
        
        #self.counter = 0
        
    def create_subsurfaces(self,game_board):
        #create subsurfaces & set some of the initial layout constraints
        self.menu = self.screen.subsurface(self.game_board.layout.menu_pos)         #menu panel
        self.menu_l = self.menu.subsurface(self.game_board.layout.menu_l_pos)       #category menu
        self.menu_r = self.menu.subsurface(self.game_board.layout.menu_r_pos)       #game selection menu - games in a category
        self.game_bg = self.screen.subsurface(self.game_board.layout.game_bg_pos)
        self.game = self.screen.subsurface(self.game_board.layout.game_pos)         #game panel - all action happens here
        #self.info_bar_offset = self.screen.subsurface(self.game_board.layout.info_bar_offset_pos) #offset - empty area between game and bottom panel - if game is not high enough to fill all available area
        #self.info_bar = self.info_bar_offset.subsurface(self.game_board.layout.info_bar_pos) #info panel - level control, game info, etc.

        #self.info_bar_offset = self.screen.subsurface(self.game_board.layout.info_bar_offset_pos) #offset - empty area between game and bottom panel - if game is not high enough to fill all available area
        self.info_bar = self.screen.subsurface(self.game_board.layout.info_bar_pos) #info panel - level control, game info, etc.

        self.score_bar = self.screen.subsurface(self.game_board.layout.score_bar_pos)         #top panel - holding username, score etc.
        
        self.misio = self.screen.subsurface(self.game_board.layout.misio_pos)       #holds an image/logo in top left corner - over menu
        self.misio.set_colorkey((255,75,0))        
        self.sb.resize()
        #self.counter += 1
        
    def fs_rescale(self, info):
        'rescale the game after fullscreen toggle, this will restart the board'
        'could not get all the game objects to scale nicely'
        #pass new screen resolution
        self.game_board.layout.update_layout_fs(self.size[0], self.size[1],self.game_board.layout.x_count,self.game_board.layout.y_count)
        #load new game - create game objects        
        self.game_board.level.load_level()
        if self.game_board.game_type == "Board":
            #adjust the layout to accommodate changes to number of squares automatically added due to screen ratio change
            self.game_board.layout.update_layout(self.game_board.data[0],self.game_board.data[1])  
        else:
            self.game_board.layout.update_layout()
        self.create_subsurfaces(self.game_board)
        info.new_game(self.game_board,self.info_bar)
        self.m.reset_scroll()
        
        
    def fullscreen_toggle(self, info):
        'toggle between fullscreen and windowed version with CTRL + F'
        'current activity will be reset'
        self.redraw_needed = [True,True,True]
        if self.config.fullscreen == True:
            self.config.fullscreen = False
            self.size = self.wn_size[:]
            self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
            self.fs_rescale(info)
        else:
            self.config.fullscreen = True
            self.size = self.fs_size[:]
            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
            self.fs_rescale(info)
            
            pygame.display.flip()
    
    def on_resize(self, size, info):
        pygame.event.set_blocked(pygame.VIDEORESIZE)
        repost = False
        if size[0] < self.config.size_limits[0]:
            size[0] = self.config.size_limits[0]
            repost = True
        if size[0] > self.config.size_limits[2]:
            size[0] = self.config.size_limits[2]
            repost = True
            
        if size[1] < self.config.size_limits[1]:
            size[1] = self.config.size_limits[1]
            repost = True
        if size[1] > self.config.size_limits[3]:
            size[1] = self.config.size_limits[3]
            repost = True

        if size != self.fs_size:
            self.wn_size = size[:]
            self.size = size[:]
        self.config.settings["screenw"] = self.size[0]
        self.config.settings["screenh"] = self.size[1]
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        
        self.fs_rescale(info)
        self.config.settings_changed = True
        self.config.save_settings(self.db)
        pygame.event.set_allowed(pygame.VIDEORESIZE)
        if repost:
            pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, size=self.size[:], w=self.size[0], h=self.size[1]))
        self.info.rescale_title_space()

    def set_up_user(self):
        #load and set up user settings
        self.config.load_settings(self.db,self.userid)
        self.lang.load_language()
        self.speaker.talkative = self.config.settings["espeak"]
        self.speaker.start_server()
        self.config.google_trans_languages = self.config.settings["extra_langs"]
        if self.config.loaded_settings:
            self.config.fullscreen = self.config.settings["full_screen"]
        #message said at the start of the game
        
        if sys.version_info < (3, 0):
            try:
                self.welcome_msg = lang.d["Hello"] + " " + self.user_name.encode("utf-8") + "! " + lang.dp["Welcome back."]
            except:
                self.welcome_msg = lang.d["Hello"]
        else:
            self.welcome_msg = lang.d["Hello"] + " " + self.user_name + "! " + lang.dp["Welcome back."]
        self.speaker.say(self.welcome_msg) #say welcome message
    
    def set_icon(self,icon_src):
        icon_canvas = pygame.Surface((32,32))
        icon_canvas.set_colorkey((0,0,0))
        icon_img =  pygame.image.load(icon_src).convert()
        
        for i in range(0,32):
            for j in range(0,32):
                icon_canvas.set_at((i,j), icon_img.get_at((i,j)))
        
        pygame.display.set_icon(icon_canvas)
        
    def run(self):
        #start of this Thread
        self.speaker.join() #join speaker Thread
        self.speaker.start_server_en()
        #initialize pygame
        pygame.init()
        
        self.db = classes.dbconn.DBConnection(self.config.file_db, self)
        self.user_name = None
        self.display_info = pygame.display.Info()
        
        while self.done4good == False:
            if self.window_state == "LOG IN":
                self.done == False
                self.set_init_vals()
                os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
                if not self.logged_out:
                    self.size = [800,480]
                else:
                    self.size = self.wn_size
                self.screen = pygame.display.set_mode(self.size)
                self.set_icon(os.path.join('res', 'icon', 'window_icon.bmp'))
                pygame.display.set_caption(self.config.window_caption)
                self.loginscreen = classes.loginscreen.LoginScreen(self, self.screen, self.size)
                clock=pygame.time.Clock()
                while self.done == False and self.userid < 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            self.done = True #mark to finish the loop and the game
                            self.done4good = True
                        else:
                            self.loginscreen.handle(event)
                    
                    if (self.redraw_needed[0] and self.game_redraw_tick[0] < 3) and self.loginscreen.update_me:
                        self.loginscreen.update()
                        self.game_redraw_tick[0] += 1
                        if self.game_redraw_tick[0] == 2:
                            self.redraw_needed[0] = False
                            self.game_redraw_tick[0] = 0
                        self.flip_needed = True
                                
                    if self.flip_needed:
                        #update the screen with what we've drawn.
                        pygame.display.flip()
                        self.flip_needed = False
                    
                    clock.tick(30)
                        
            if self.window_state == "GAME":
                self.set_up_user()
                
                self.done == False
                #self.force_no_resize = True
                self.set_init_vals()
                os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
                self.config.fs_width  = self.display_info.current_w
                self.config.fs_height = self.display_info.current_h
                
                #check if there's a size available from previous session
                if self.config.settings["screenw"] >= self.config.size_limits[0] and self.config.settings["screenh"] >= self.config.size_limits[1] and self.config.settings["screenw"] <= self.config.size_limits[2] and self.config.settings["screenh"] <= self.config.size_limits[3]:
                    self.wn_size = [self.config.settings["screenw"], self.config.settings["screenh"]]
                else:
                    self.wn_size = [min(self.config.fs_width - self.config.os_panels_w, self.config.size_limits[2]), min(self.config.fs_height - self.config.os_panels_h, self.config.size_limits[3])]
                    self.config.settings["screenw"] = self.wn_size[0]
                    self.config.settings["screenh"] = self.wn_size[1]
                    
                self.fs_size = [self.config.fs_width, self.config.fs_height]
                
                if self.config.fullscreen == True:
                    self.size = self.fs_size[:]
                    flag = pygame.FULLSCREEN
                else:
                    self.size = self.wn_size[:]
                    flag = pygame.RESIZABLE
                
                #restarting the display to solve a bug causing some of the game area unresponsive after resizing (this bug affected the game only when it was set to start in fullscreen) 
                pygame.display.quit()
                pygame.display.init()
                self.screen = pygame.display.set_mode(self.size, flag)
                self.set_icon(os.path.join('res', 'icon', 'window_icon.bmp'))
                
                #Set title of the window
                pygame.display.set_caption(self.config.window_caption)
                
                #create a list of one sprite holding game image or logo
                self.sprites_list = pygame.sprite.RenderPlain()
                
                #create the logo object and add it to the list to render on update
                self.front_img = classes.logoimg.LogoImg()
                self.sprites_list.add(self.front_img)
                
                #create a dummy self.game_board variable to be deleted and recreated at the beginning of the main loop
                self.game_board = None
                
                #kind of a dirty workaround to avoid issues with anti-aliasing on devices not supporting aa compatible bit depths - hopefully it works (not tested - haven't got such device)
                if pygame.display.get_surface().get_bitsize() not in [32,24]:
                    pygame.draw.aalines = pygame.draw.lines
                    pygame.draw.aaline = pygame.draw.line
                    
                #create game menu / game manager
                m = classes.menu.Menu(self)
                self.m = m
                
                self.sb = classes.score_bar.ScoreBar(self) 
        
                #create info panel integrated with level control - holds current level/game and some buttons to change levels, etc.
                info = classes.info_bar.InfoBar(self)
                self.info = info
                
                #Used to manage how fast the screen updates
                clock=pygame.time.Clock()
                
                #test values
                #self.video_resize_count = 0
                #self.resize_func = 0
                # -------- Main Program Loop ----------- #
                while self.done==False:
                    # start, switch or continue a game
                    #not really an implementation of a State Machine but does the job
                    if m.active_game_id != m.game_started_id: #if game id changed since last frame
                        if self.game_board != None:
                            #if this is not the first start of a game - the self.game_board has been already 'created' at least once
                            self.game_board.board.clean() #empty sprite groups, delete lists
                            del(self.game_board) #delete all previous game objects
                        #recreate a new game and subsurfaces
                        self.game_board = m.game_constructor(self,self.speaker,self.config,self.size[0],self.size[1])
                        m.game_started_id = m.active_game_id
                        m.l = self.game_board.layout
                        self.create_subsurfaces(self.game_board)
                        info.new_game(self.game_board,self.info_bar)
                        #self.game_board.update_score(0)
                        """
                        if self.config.loaded_settings == False and self.init_resize:
                            if self.config.fullscreen == False:
                                self.on_resize(self.size, info)
                                self.init_resize = False
                        """
                        #self.fs_rescale(info)
                        gc.collect() #force garbage collection to remove remaining variables to free memory
                    
                    elif self.game_board.level.lvl != self.game_board.level.prev_lvl:
                        #if game id is the same but the level changed load new level
                        self.create_subsurfaces(self.game_board)
                        info.new_game(self.game_board,self.info_bar)
                        self.game_board.level.prev_lvl = self.game_board.level.lvl
                        gc.collect()
        
                    #Process or delegate events
                    #mods = pygame.key.get_mods()
                    for event in pygame.event.get(): #pygame.event.get(): # User did something
                                      
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            self.done = True #mark to finish the loop and the game
                            self.done4good = True
                        elif event.type == pygame.VIDEORESIZE:
                            if self.config.fullscreen == False:
                                self.on_resize(list(event.size), info)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f and (event.mod & pygame.KMOD_LCTRL):
                            #CTRL + F - pressed
                            self.fullscreen_toggle(info)
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F5:#refresh - reload level
                            self.game_board.level.load_level()
                        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                            pos = event.pos
                            if event.type == pygame.MOUSEBUTTONDOWN and self.game_board.show_msg == True:
                                #if dialog after completing the game is shown then hide it and load next game
                                self.game_board.show_msg = False
                                self.game_board.level.next_board_load()
                            elif pos[0] > self.game_board.layout.menu_a_w and self.game_board.layout.top_margin > pos[1]:
                                self.sb.handle(event)
                            elif pos[0] > self.game_board.layout.menu_a_w and self.game_board.layout.top_margin < pos[1] < self.game_board.layout.game_h + self.game_board.layout.top_margin:
                                #clicked on game board
                                self.game_board.handle(event)
                            elif pos[0] < self.game_board.layout.menu_a_w:
                                #clicked on menu panel
                                if pos[0] < self.game_board.layout.menu_l_w:
                                    #clicked on category menu
                                    m.handle_menu_l(event)
                                else:
                                    #clicked on game selection menu
                                    m.handle_menu_r(event,self.game_board.layout.menu_l_w)
                            else:
                                #clicked on info panel
                                info.handle(event,self.game_board.layout,self)
                        elif event.type == pygame.MOUSEBUTTONUP:
                            pos = event.pos
                            if pos[0] > self.game_board.layout.menu_a_w and self.game_board.layout.top_margin < pos[1] < self.game_board.layout.game_h + self.game_board.layout.top_margin:
                                self.game_board.handle(event)
                            elif pos[0] > self.game_board.layout.menu_a_w and pos[1] < self.game_board.layout.top_margin:
                                self.sb.handle(event)
                            else:
                                info.handle(event,self.game_board.layout,self)
                                self.game_board.handle(event)
                            pygame.mouse.set_cursor(*pygame.cursors.arrow)
                        else:
                            #let the game handle other events
                            self.game_board.handle(event)
                    
                    #trying to save the CPU - only update a subsurface entirely, (can't be bothered to play with dirty sprites)
                    #if anything has changed on the subsurface or it's size has changed
                    
                    #creating list of drawing functions and arguments for each subsurface
                    draw_func = [self.game_board.update,info.draw,m.draw_menu]
                    draw_func_args = [[self.game],[self.info_bar],[self.menu,self.menu_l,self.menu_r,self.game_board.layout]]
                    
                    if self.m.scroll_direction != 0:
                        if self.menu_speed == self.menu_tick:
                            self.m.scroll_menu()
                            self.menu_tick = 0
                        else:
                            self.menu_tick += 1
                        #self.redraw_needed[2] = True
                        
                    #checking if any of the subsurfaces need updating and updating them if needed
                    #in reverse order so the menu is being drawn first
                    for i in range(2,-1,-1):
                        if (self.redraw_needed[i] and self.game_redraw_tick[i] < 3):
                            draw_func[i](*draw_func_args[i])
                            self.game_redraw_tick[i] += 1
                            if self.game_redraw_tick[i] == 2:
                                self.redraw_needed[i] = False
                                self.game_redraw_tick[i] = 0
                                self.sb.update_me = True
                            self.flip_needed = True
                            if i == 2:
                                #draw the logo over menu - top left corner
                                self.front_img.update()
                                self.sprites_list.draw(self.misio)
                    if self.sb.update_me:
                        self.sb.draw(self.score_bar)
                        self.flip_needed = True
                        
                    if self.flip_needed:
                        #update the screen with what we've drawn.
                        pygame.display.flip()
                        self.flip_needed = False
        
                    #Limit to 30 frames per second but most redraws are made when needed - less often
                    #30 frames per second used mainly for event handling
                    self.game_board.process_ai()
                    clock.tick(30)
            
                #close eSpeak process, quit pygame, collect garbage and exit the game.
                #self.m.save_levels()
                if self.config.settings_changed:
                    self.config.save_settings(self.db)
                clock.tick(300)
        self.db.close()
        if self.speaker.process != None:
            self.speaker.stop_server()
        self.speaker.stop_server_en()
        pygame.quit()
        gc.collect()
        os.sys.exit()

if __name__ == "__main__":
    #create configuration object
    configo = classes.config.Config()
    
    #create the language object
    lang = classes.lang.Language(configo)
    #create the Thread objects and start the threads
    speaker = classes.speaker.Speaker(lang, configo)
    app = GamePlay(speaker, lang, configo)
    speaker.start()
    app.start()
