# -*- coding: utf-8 -*-
from __future__ import with_statement
import pygame
import classes.game_driver as gd
from game_boards import *
import classes.colors
import pickle
import copy
import os, sys
import pygame.mixer
if sys.version_info < (2, 6):
    pass
sounds = pygame.mixer
sounds.init()

sound_7 = '140508__blackstalian__click-sfx2.ogg'
sound_9 = '140509__blackstalian__click-sfx1.ogg'


s3 = sounds.Sound(os.path.join('res', 'sounds', sound_7))
s4 = sounds.Sound(os.path.join('res', 'sounds', sound_9))

cl = classes.colors.Color()

class MenuCategory(pygame.sprite.Sprite):
    def __init__(self, cat_id, title, subtitle, cat_icon_size,img_src):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.cat_id = cat_id
        if sys.version_info < (3, 0):
            try:
                self.title = unicode(title, "utf-8")
                self.subtitle = unicode(subtitle, "utf-8")
            except UnicodeDecodeError:
                self.title = title
                self.subtitle = subtitle
        else:        
            self.title = title
            self.subtitle = subtitle
            
        self.color = (245, 0, 245)

        self.image = pygame.Surface([cat_icon_size, cat_icon_size])
        self.image.fill(self.color)
        self.img_src = img_src
        if len(self.img_src) > 0:
            self.img = self.image
            self.img_pos = (0,0)
            try:
                self.img_org = pygame.image.load(os.path.join('res', 'icons', self.img_src)).convert()
                self.img_pos = (0,0)
                self.img = self.img_org
            except:
                pass

        #self.image.set_colorkey(self.color)
        
        # Make our top-left corner the passed-in location. The +1 is the margin
        self.rect = self.image.get_rect()
        
    def update(self):
        self.image.fill(self.color)
        if len(self.img_src) > 0:
            self.image.blit(self.img, self.img_pos)
            
class MenuItem(pygame.sprite.Sprite):
    def __init__(self, dbgameid, item_id, cat_id, title, subtitle, constructor, icon_size, img_src,variant = 0):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.item_id = item_id
        self.cat_id = cat_id
        self.game_constructor = constructor
        self.variant = variant
        self.dbgameid = dbgameid
        if sys.version_info < (3, 0):
            try:
                self.title = unicode(title, "utf-8")
                self.subtitle = unicode(subtitle, "utf-8")
            except UnicodeDecodeError:
                self.title = title
                self.subtitle = subtitle
        else:        
            self.title = title
            self.subtitle = subtitle

        self.color = (245, 0, 245)

        self.image = pygame.Surface([icon_size, icon_size])
        self.img_src = img_src
        if len(self.img_src) > 0:
            self.img = self.image
            self.img_pos = (0,0)
            try:
                self.img_org = pygame.image.load(os.path.join('res', 'icons', self.img_src)).convert()
                self.img_pos = (0,0)
                self.img = self.img_org
            except:
                pass

        self.image.set_colorkey(self.color)
 
        # Make our top-left corner the passed-in location. The +1 is the margin
        self.rect = self.image.get_rect()

    def update(self):
        self.image.fill(self.color)
        if len(self.img_src) > 0:
            self.image.blit(self.img, self.img_pos)

class MenuBookmark(pygame.sprite.Sprite):
    def __init__(self, bm_id, bm_icon_size, img_src):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.bm_id = bm_id
        self.color = (245, 0, 245)

        #self.image = pygame.Surface([61, 63])
        self.image = pygame.Surface([65,70])
        self.image.fill(self.color)
        self.img_src = img_src
        if len(self.img_src) > 0:
            self.img = self.image
            self.img_pos = (0,0)
            try:
                self.img_org = pygame.image.load(os.path.join('res', 'icons', self.img_src)).convert()
                self.img_pos = (0,0)
                self.img = self.img_org
            except:
                pass

        #self.image.set_colorkey(self.color)
        
        # Make our top-left corner the passed-in location. The +1 is the margin
        self.rect = self.image.get_rect()

    def update(self):
        self.image.fill(self.color)
        if len(self.img_src) > 0:
            self.image.blit(self.img, self.img_pos)

class MenuScrollBtn(pygame.sprite.Sprite):
    def __init__(self, sb_id, sb_icon_size, img_src):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.sb_id = sb_id
        self.color = (255, 255, 255)
        self.image = pygame.Surface(sb_icon_size)
        self.image.fill(self.color)
        self.img_src = img_src
        if len(self.img_src) > 0:
            self.img = self.image
            self.img_pos = (0,0)
            try:
                self.img_org = pygame.image.load(os.path.join('res', 'icons', self.img_src)).convert()
                self.img_pos = (0,0)
                self.img = self.img_org
            except:
                pass
        self.image.set_colorkey(self.color)
        
        
        # Make our top-left corner the passed-in location. The +1 is the margin
        self.rect = self.image.get_rect()

    def update(self):
        #self.image.fill(self.color)
        if len(self.img_src) > 0:
            self.image.blit(self.img, self.img_pos)
    
class Menu:
    def __init__(self,mainloop):        
        self.mainloop = mainloop
        self.lang = self.mainloop.lang

        self.create_lists()
        
        self.mouseenter = -1
        self.mouseenter_cat = -1
        self.l = None
        self.active_game_id = 0
        self.game_started_id = -1
        self.active_cat = 0
        self.tab_game_id = 0
        self.prev_cat = -1
        self.game_constructor = game000.Board
        self.game_variant = 0
        self.icon_size = 50
        self.cat_icon_size = 50
        #self.x_margin = 6 #6
        #self.y_margin = 7 #5
        self.x_margin = 6+4 #6
        self.y_margin = 10 #5
        #self.ttow = self.mainloop.game_board.layout.menu_l_w *2#width to trigger title only
        self.scroll_l = 0
        self.scroll_r = 0
        self.tab_l_scroll = 0
        self.tab_r_scroll = 0
        self.scroll_direction = 0
        self.active_pane = None
        self.en_list = [] #list of games that need the speaker to be switched to English
        self.scroll_step = self.cat_icon_size + self.y_margin
        
        # This is a list of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'RenderPlain.'
        self.categories_list = pygame.sprite.LayeredUpdates()
        self.games_in_current_cat = pygame.sprite.LayeredUpdates()
        self.bookmarks_list = pygame.sprite.LayeredUpdates()
        self.create_menu()
        
    def load_levels(self):
        if self.mainloop.config.save_levels:
            temp = dict()
            #try:
            """
            file_name = self.mainloop.config.file_level
            with open(file_name,"rb") as level_file:
                temp = pickle.load(level_file)
            #checking if there are any games that have not been saved in the pickle previously and adding them to the dictionary
            """
            temp = self.mainloop.db.load_all_cursors(self.mainloop.userid)
            for key in self.saved_levels.keys():
                if key not in temp.keys():
                    temp[key] = self.saved_levels[key]
                """
                for innerkey in self.saved_levels[key].keys():
                    if innerkey not in temp[key].keys():
                        temp[key][innerkey] = self.saved_levels[key][innerkey]
                """
                    
            self.saved_levels = temp
            #except:
            #    pass #print("Error loading level data")
    """
    def load_levels(self):
        if self.mainloop.config.save_levels:
            temp = dict()
            try:
                file_name = self.mainloop.config.file_level
                with open(file_name,"rb") as level_file:
                    temp = pickle.load(level_file)
                #checking if there are any games that have not been saved in the pickle previously and adding them to the dictionary

                for key in self.saved_levels.keys():
                    if key not in temp.keys():
                        temp[key] = self.saved_levels[key]
                    " ""
                    for innerkey in self.saved_levels[key].keys():
                        if innerkey not in temp[key].keys():
                            temp[key][innerkey] = self.saved_levels[key][innerkey]
                    " ""
                        
                self.saved_levels = temp
            except:
                pass #print("Error loading level data")
    """

    def save_levels(self):
        pass
        """        
        if self.mainloop.config.save_levels:
            try:
                file_name = self.mainloop.config.file_level
                self.commit_save(file_name)
            except:
                print('Sorry could not save levels...')
        """
                
    def commit_save(self, file_name):
        pass
        """
        with open(file_name,"wb") as level_file:
            pickle.dump(self.saved_levels, level_file)
        """
            
    def create_lists(self):
        self.categories = []
        self.games = []
        self.games_current = []
        self.bookmarks = []
        #self.scroll_btns = []
        
        self.saved_levels = dict()
        
    def create_menu(self):
        self.add_categories()
        self.add_games()
        self.add_bookmark("","tab_l.png")
        self.categories_list.add(self.bookmarks[0])
        self.categories_list.move_to_back(self.bookmarks[0])
        self.add_bookmark("","tab_r.png")
        #self.add_scroll_btns()
        self.update_scroll_pos()
        #self.categories_list.add(self.scroll_btns[0])
        #self.categories_list.move_to_front(self.scroll_btns[0])
        #reload level
        self.load_levels()
        
    def empty_menu(self):
        self.create_lists()
        self.categories_list.empty()
        self.games_in_current_cat.empty()
        self.bookmarks_list.empty()
        
    def lang_change(self):
        self.empty_menu()
        self.create_menu()
        self.change_cat(self.active_cat)
        
    def reset_scroll(self):
        self.scroll_r = 0
        self.tab_r_scroll = 0
        self.scroll_l = 0
        self.tab_l_scroll = 0
        
    def handle_menu_l(self,event):
        try: #this is to avoid errors with mouse events when mouse is over the menu when game is not yet created
            if event.type == pygame.MOUSEMOTION:
                self.mainloop.sb.update_me = True
                pos = event.pos
                if self.mainloop.info.hidden == False and pos[0] < 124:
                    self.mainloop.info.title_only()
                if self.x_margin < pos[0] < self.cat_icon_size + self.x_margin:
                    
                    if self.y_margin+self.l.misio_pos[3] < pos[1] < self.cat_h+self.l.misio_pos[3]:
                        self.active_pane = 0;
                        row = (pos[1]-3-self.l.misio_pos[3]-self.scroll_l) // (self.cat_icon_size + self.y_margin)
                        if row != self.mouseenter_cat:
                            self.mouseenter_cat = row
                            self.mouseenter = -1
                            self.mainloop.info.title = self.categories[row].title
                            self.mainloop.info.subtitle = self.categories[row].subtitle
                            self.mainloop.redraw_needed[1] = True
                            self.mainloop.redraw_needed[2] = True
                            #self.save_levels()  
                    else:
                        self.reset_titles()
                        
                    if pos[1] > self.mainloop.size[1]-30:# and self.scroll_l == 0:
                        self.scroll_direction = 1
                    #elif self.l.misio_pos[3]-20 < pos[1] < self.l.misio_pos[3]+5:# and self.scroll_l < 0:
                    elif 0 < pos[1] < self.l.misio_pos[3]+5:# and self.scroll_l < 0:
                        self.scroll_direction = -1
                    else:
                        self.scroll_direction = 0
                else:
                    self.reset_titles()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mainloop.sb.update_me = True
                pos = event.pos
                #if y is within category size
                if self.x_margin < pos[0] < self.cat_icon_size + self.x_margin:
                    if self.y_margin+self.l.misio_pos[3] < pos[1] < self.cat_h+self.l.misio_pos[3]+self.scroll_l:
                        row = (pos[1]-3-self.l.misio_pos[3]-self.scroll_l) // (self.cat_icon_size + self.y_margin)
                        self.active_cat = row
                        self.tab_l_scroll = (self.scroll_l // self.scroll_step)
                        if self.mainloop.config.settings["sounds"]:
                            s3.play()
                        self.mainloop.redraw_needed[1] = True
                        self.mainloop.redraw_needed[2] = True
            elif event.type  == pygame.MOUSEBUTTONDOWN and event.button == 4:
                self.scroll_menu(direction = -1, pane = 0)
            elif event.type  == pygame.MOUSEBUTTONDOWN and event.button == 5:
                self.scroll_menu(direction = 1, pane = 0)
        except:
            pass
            
    def handle_menu_r(self,event,mlw):
        try:
            if event.type == pygame.MOUSEMOTION:
                self.mainloop.sb.update_me = True
                pos = event.pos
                #self.mainloop.info_bar.hide_buttons(a,b,c,d,e,f,g,h,i)
                if self.mainloop.info.hidden == False and pos[0] < 124:
                    self.mainloop.info.title_only()
                    
                if (mlw + self.x_margin) < pos[0] < (mlw + self.icon_size + self.x_margin):
                    if self.y_margin+self.l.misio_pos[3] < pos[1] < self.game_h+self.l.misio_pos[3]:
                        self.active_pane = 1
                        row = (pos[1]-3-self.l.misio_pos[3]-self.scroll_r) // (self.icon_size + self.y_margin)
                        if row != self.mouseenter:
                            self.mouseenter = row
                            self.mouseenter_cat = -1
                            self.mainloop.info.title = self.games_current[row].title
                            self.mainloop.info.subtitle = self.games_current[row].subtitle
                            self.mainloop.redraw_needed[1] = True
                    else:
                        self.reset_titles()
                    if pos[1] > self.mainloop.size[1]-30:# and self.scroll_r >= 0:
                        self.scroll_direction = 1
                    elif 0 < pos[1] < self.l.misio_pos[3]+5:# and self.scroll_r < 0:
                        self.scroll_direction = -1
                    else:
                        self.scroll_direction = 0
                        
                else:
                    self.reset_titles()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mainloop.sb.update_me = True
                pos = event.pos
                
                if (mlw + self.x_margin) < pos[0] < (mlw + self.icon_size + self.x_margin):
                    if self.y_margin+self.l.misio_pos[3] < pos[1] < self.game_h+self.l.misio_pos[3]:
                        
                        row = (pos[1]-3-self.l.misio_pos[3]-self.scroll_r) // (self.icon_size + self.y_margin)
                        self.active_game_id = self.games_current[row].item_id
                        self.tab_r_scroll = (self.scroll_r // self.scroll_step)
                        self.tab_game_id = row
                        self.game_constructor = self.games_current[row].game_constructor
                        self.game_variant = self.games_current[row].variant
                        #self.mainloop.info.title_space = self.mainloop.info.width - 10
                        #switch active speaker and replace some strings temporarily
                        
                        if self.mainloop.config.settings["sounds"]:
                            s4.play()
                            
                        if self.mainloop.lang.lang[0:2] != "en":
                            #game_boards.game049.Board
                            n = str(self.game_constructor)[16:19]
                            if n in self.en_list:
                                self.mainloop.speaker.switch_spk(2)
                                self.lang.dp["Congratulations! Game Completed."] = "Congratulations! You have completed all tasks in this game."
                                self.lang.dp["Perfect! Level completed!"] = "Perfect! Level completed!"
                                self.lang.dp["Great job!"] = ["Great job!","Perfect!","Awesome!","Fantastic job!","Well done!"]
                            else:
                                self.mainloop.speaker.switch_spk(1)
                                self.lang.dp["Congratulations! Game Completed."] = self.lang.lang_file.dp["Congratulations! Game Completed."]
                                self.lang.dp["Perfect! Level completed!"] = self.lang.lang_file.dp["Perfect! Level completed!"]
                                self.lang.dp["Great job!"] = self.lang.lang_file.dp["Great job!"]
                        
                        self.mainloop.score = 0  
                        self.mainloop.redraw_needed = [True, True, True]
            elif event.type  == pygame.MOUSEBUTTONDOWN and event.button == 4:
                self.scroll_menu(direction = -1, pane = 1)
            elif event.type  == pygame.MOUSEBUTTONDOWN and event.button == 5:
                self.scroll_menu(direction = 1, pane = 1)
        except:
            pass
            
    def scroll_menu(self, direction = 0, pane = -1):
        self.mainloop.sb.update_me = True
        if pane == -1:
            direction = self.scroll_direction
            pane = self.active_pane
        menu_height = self.mainloop.size[1]-(self.y_margin+self.l.misio_pos[3])
        if direction != 0 and pane == 1:
            if self.game_h > menu_height:
                diff = self.game_h - menu_height
                
                #scroll the menu
                if (direction == 1 and -self.scroll_r < diff) or (direction == -1 and self.scroll_r < 0):
                    self.scroll_r = self.scroll_r - self.scroll_step * direction

                self.tab_r_scroll = (self.scroll_r // self.scroll_step)
                self.mainloop.redraw_needed[2] = True
                self.mainloop.redraw_needed[1] = True
        elif direction != 0 and pane == 0:
            if self.cat_h > menu_height:
                diff = self.cat_h - menu_height
                #scroll from here
                if (direction == 1 and -self.scroll_l < diff) or (direction == -1 and self.scroll_l < 0):
                    self.scroll_l = self.scroll_l - self.scroll_step * direction
                self.tab_l_scroll = (self.scroll_l // self.scroll_step)
                self.mainloop.redraw_needed[2] = True
                self.mainloop.redraw_needed[1] = True
        
    def reset_titles(self):
        self.mainloop.info.title = ""
        self.mainloop.info.subtitle = ""
        self.mainloop.redraw_needed[1] = True
        self.mainloop.redraw_needed[2] = True
        self.mouseenter = -1
        self.mouseenter_cat = -1
        
    def add_bookmark(self,title,img_src):
        new_bookmark = MenuBookmark(len(self.bookmarks),self.cat_icon_size,img_src)
        self.bookmarks.append(new_bookmark)

    def add_scroll_btn(self,img_src):
        new_scroll_btn = MenuScrollBtn(len(self.scroll_btns),[55,13],img_src)
        self.scroll_btns.append(new_scroll_btn)

    def add_scroll_btns(self):
        self.add_scroll_btn("arrow_l2.png")
        self.add_scroll_btn("arrow_r2.png")
            
    def update_scroll_pos(self):
        pass
        """
        pos = [[9+self.x_margin,self.mainloop.size[1]-13],[9+self.x_margin,self.mainloop.size[1]-13]]
        
        i=0        
        for each_item in self.scroll_btns:
            each_item.rect.topleft = pos[i]
            i+=1
        """
        
    def add_category(self,title,subtitle,img_src):
        new_category = MenuCategory(len(self.categories),title,subtitle,self.cat_icon_size,img_src)
        self.categories.append(new_category)
        self.categories_list.add(new_category)

    def add_categories(self):
        self.add_category(self.lang.d["Info Category"],"","ico_c_00.png")
        #self.add_category(self.lang.d["Working with large numbers"],"","ico_g_9999.png")
        self.add_category(self.lang.d["Discover Letters"],"","ico_c_01.png")
        if  self.mainloop.lang.lang[0:2] != "he":
            self.add_category(self.lang.d["Learn Words"],"","ico_c_02.png")
        if self.mainloop.lang.lang[0:2] != "en":
            self.add_category(self.lang.d["English"],"","ico_c_12.png")
        self.add_category(self.lang.d["Maths"],self.lang.d["Numbers & Basic Operations"],"ico_c_03a.png")
        self.add_category(self.lang.d["Maths"]+" 2",self.lang.d["Basic Operations - exercises"],"ico_c_03.png")
        self.add_category(self.lang.d["Maths"]+" 3",self.lang.d["Sorting and Comparing"],"ico_c_04.png")
        self.add_category(self.lang.d["Working with large numbers"],"","ico_c_11.png")
        self.add_category(self.lang.d["Geometry"],"","ico_c_05.png")
        self.add_category(self.lang.d["Time"],"","ico_c_10.png")
        self.add_category(self.lang.d["Art"],"","ico_c_06.png")
        self.add_category(self.lang.d["Memory"],"","ico_c_07.png")
        self.add_category(self.lang.d["Games & Mazes"],"","ico_c_08.png")
        self.add_category(self.lang.d["Multiplayer"],"","ico_c_09.png")
        self.cat_h = len(self.categories)*(self.cat_icon_size+self.y_margin)

    def add_game(self,dbgameid,cat_id,constructor,title,subtitle,img_src,variant=0):
        new_game = MenuItem(dbgameid,len(self.games),cat_id,title,subtitle,constructor,self.icon_size,img_src,variant)
        self.games.append(new_game)
        #if dbgameid not in self.saved_levels:
        #    self.saved_levels[dbgameid] = dict()
        self.saved_levels[dbgameid] = 1
        
        #self.saved_levels[constructor] = 1
        """
        if constructor not in self.saved_levels:
            self.saved_levels[constructor] = dict()
        self.saved_levels[constructor][str(variant)] = 1
        """

    def add_games(self):
        'creates all menu buttons'
        #last id = 118
        c_id = 0
        self.add_game(0,c_id,game000.Board,self.lang.d["About."],self.lang.d["Game info..."],"ico_g_0000.png")
        self.add_game(1,c_id,game001.Board,self.lang.d["Credits"],"","ico_g_0001.png")
        self.add_game(2,c_id,game002.Board,self.lang.d["Credits"],self.lang.d["Translators"],"ico_g_0001.png")
        self.add_game(3,c_id,game003.Board,self.lang.d["Translations"],"","ico_g_0003.png")
        
        #self.add_game(c_id,game067.Board,"Font Test","","ico_g_0000.png")
        
        #self.add_game(c_id,game056.Board,self.lang.d["Preferences"],"game056","ico_g_0000.png")
        #self.add_game(c_id,game058.Board,self.lang.d["TicTacToe"]+" 3",self.lang.d["multiline-tictactoe"],"ico_g_0808.png")
        #self.add_game(c_id,game060.Board,self.lang.d["Preferences"],"game060","ico_g_0000.png")

        c_id += 1
        if self.mainloop.lang.lang[0:2] == "en":
            self.add_game(4,c_id,game037.Board,self.lang.d["English Alphabet"],self.lang.d["Letter Flashcards"],"ico_g_0100.png")
        #if self.mainloop.lang.lang in ['en_gb','en_us','el','ru']:
        self.add_game(5,c_id,game017.Board,self.lang.d["Your Alphabet"],self.lang.d["Letter Flashcards"],"ico_g_0108.png")
        if self.mainloop.lang.lang[0:2] == "en":
            self.add_game(6,c_id,game068.Board,self.lang.d["Learn to Write"],self.lang.d["Trace Letters"],"ico_g_0109.png")
            self.add_game(7,c_id,game010.Board,self.lang.d["Learn to Write"],self.lang.d["Trace Letters"],"ico_g_0110.png")
        if self.mainloop.lang.lang == 'ru':
            self.add_game(8,c_id,game022.Board,self.lang.d["Learn to Write"],self.lang.d["local_kbrd"],"ico_g_0111.png")
        if self.mainloop.lang.lang == 'el':
            self.add_game(9,c_id,game067.Board,self.lang.d["Learn to Write"],self.lang.d["local_kbrd"],"ico_g_0112.png")
        
        #if self.mainloop.lang.lang not in self.lang.alphabet_26:
        if self.mainloop.lang.lang[0:2] == "en":
            self.add_game(10,c_id,game014.Board,self.lang.d["Complete the ABC"]+ " - " + self.lang.d["English"],self.lang.d["Complete abc"],"ico_g_0103.png")

        self.add_game(11,c_id,game049.Board,self.lang.d["Complete the ABC"],self.lang.d["in your language"],"ico_g_0104.png")
        self.add_game(12,c_id,game047.Board,self.lang.d["Sorting Letters"],self.lang.d["Lowercase Letters"],"ico_g_0105.png")
        if self.lang.has_uc:
            self.add_game(13,c_id,game048.Board,self.lang.d["Sorting Letters"]+" ",self.lang.d["Uppercase Letters"],"ico_g_0106.png")
        
        if self.mainloop.lang.lang in ["en_GB","en_US","pl","ru"] and self.mainloop.fs_size[1] > 440:
            self.add_game(14,c_id,game016.Board,self.lang.d["Keyboard Skills"],self.lang.d["Touch Typing"],"ico_g_0107.png")
        elif self.mainloop.fs_size[1] > 440: #and self.mainloop.lang.lang not in ["en_gb","en_us","pl","ru"]:
            if self.mainloop.lang.lang == 'el':
                self.add_game(15,c_id,game077.Board,self.lang.d["Keyboard Skills"] + " - Ελληνικά",self.lang.d["Touch Typing"],"ico_g_0107.png")

                
        #self.add_game(c_id,game006.Board,self.lang.d["Sorting Letters"],self.lang.d["Lowercase Letters"],"ico_g_0000.png")
        #self.add_game(c_id,game007.Board,self.lang.d["Sorting Letters"]+" ",self.lang.d["Uppercase Letters"],"ico_g_0000.png")
        
        if  self.mainloop.lang.lang[0:2] != "he":
            c_id += 1
            self.add_game(17,c_id,game013.Board,self.lang.d["Word Builder"],"","ico_g_0200.png")
            self.add_game(18,c_id,game023.Board,self.lang.d["Word Maze"],self.lang.d["Collect all"],"ico_g_0201.png")
            self.add_game(19,c_id,game025.Board,self.lang.d["Word Maze + 4"],self.lang.d["Collect all"],"ico_g_0202.png")
            if self.mainloop.lang.lang[0:2] == "en":
                self.add_game(107,c_id,game082.Board,self.lang.d["Word Builder - Animals"],self.lang.d["Complete the word"],"ico_g_0203.png",variant=0)
                self.add_game(108,c_id,game082.Board,self.lang.d["Word Builder - Sports"],self.lang.d["Complete the word"],"ico_g_0204.png",variant=1)
                self.add_game(109,c_id,game082.Board,self.lang.d["Word Builder - Body"],self.lang.d["Complete the word"],"ico_g_0205.png",variant=2)
                self.add_game(110,c_id,game082.Board,self.lang.d["Word Builder - People"],self.lang.d["Complete the word"],"ico_g_0206.png",variant=3)
                self.add_game(111,c_id,game082.Board,self.lang.d["Word Builder - Actions"],self.lang.d["Complete the word"],"ico_g_0209.png",variant=4)
                self.add_game(112,c_id,game082.Board,self.lang.d["Word Builder - Constructions"],self.lang.d["Complete the word"],"ico_g_0210.png",variant=5)
                self.add_game(113,c_id,game082.Board,self.lang.d["Word Builder - Nature"],self.lang.d["Complete the word"],"ico_g_0211.png",variant=6)
                self.add_game(114,c_id,game082.Board,self.lang.d["Word Builder - Jobs"],self.lang.d["Complete the word"],"ico_g_0212.png",variant=7)
                self.add_game(115,c_id,game082.Board,self.lang.d["Word Builder - Clothes and Accessories"],self.lang.d["Complete the word"],"ico_g_0208.png",variant=8)
                self.add_game(116,c_id,game082.Board,self.lang.d["Word Builder - Fruits and Vegetables"],self.lang.d["Complete the word"],"ico_g_0213.png",variant=9)
                self.add_game(117,c_id,game082.Board,self.lang.d["Word Builder - Transport"],self.lang.d["Complete the word"],"ico_g_0214.png",variant=10)
                self.add_game(118,c_id,game082.Board,self.lang.d["Word Builder - Food"],self.lang.d["Complete the word"],"ico_g_0207.png",variant=11)
                #self.add_game(106,c_id,game083.Board,"Title","sub-title","ico_g_9998.png")
            
        if self.mainloop.lang.lang[0:2] != "en":
            c_id += 1
            self.en_list = ["037","068","010","014","082"]
            self.add_game(4,c_id,game037.Board,self.lang.d["English Alphabet"],self.lang.d["Letter Flashcards"],"ico_g_1204.png")
            self.add_game(6,c_id,game068.Board,self.lang.d["Learn to Write"],self.lang.d["Trace Letters"],"ico_g_1200.png")
            self.add_game(7,c_id,game010.Board,self.lang.d["Learn to Write"],self.lang.d["Trace Letters"],"ico_g_1201.png")
            self.add_game(10,c_id,game014.Board,self.lang.d["Complete the ABC"]+" - "+self.lang.d["English"],self.lang.d["Complete abc"],"ico_g_1202.png")
            
            self.add_game(107,c_id,game082.Board,self.lang.d["Word Builder - Animals"],self.lang.d["Complete the word"],"ico_g_1205.png",variant=0)
            self.add_game(108,c_id,game082.Board,self.lang.d["Word Builder - Sports"],self.lang.d["Complete the word"],"ico_g_1206.png",variant=1)
            self.add_game(109,c_id,game082.Board,self.lang.d["Word Builder - Body"],self.lang.d["Complete the word"],"ico_g_1207.png",variant=2)
            self.add_game(110,c_id,game082.Board,self.lang.d["Word Builder - People"],self.lang.d["Complete the word"],"ico_g_1208.png",variant=3)
            self.add_game(111,c_id,game082.Board,self.lang.d["Word Builder - Actions"],self.lang.d["Complete the word"],"ico_g_1211.png",variant=4)
            self.add_game(112,c_id,game082.Board,self.lang.d["Word Builder - Constructions"],self.lang.d["Complete the word"],"ico_g_1212.png",variant=5)
            self.add_game(113,c_id,game082.Board,self.lang.d["Word Builder - Nature"],self.lang.d["Complete the word"],"ico_g_1213.png",variant=6)
            self.add_game(114,c_id,game082.Board,self.lang.d["Word Builder - Jobs"],self.lang.d["Complete the word"],"ico_g_1214.png",variant=7)
            self.add_game(115,c_id,game082.Board,self.lang.d["Word Builder - Clothes and Accessories"],self.lang.d["Complete the word"],"ico_g_1210.png",variant=8)
            self.add_game(116,c_id,game082.Board,self.lang.d["Word Builder - Fruits and Vegetables"],self.lang.d["Complete the word"],"ico_g_1215.png",variant=9)
            self.add_game(117,c_id,game082.Board,self.lang.d["Word Builder - Transport"],self.lang.d["Complete the word"],"ico_g_1216.png",variant=10)
            self.add_game(118,c_id,game082.Board,self.lang.d["Word Builder - Food"],self.lang.d["Complete the word"],"ico_g_1209.png",variant=11)
            #self.add_game(106,c_id,game083.Board,"Title","sub-title","ico_g_9998.png")
            
            if self.mainloop.lang.lang not in ["en_GB","en_US","pl","ru","el"] and self.mainloop.fs_size[1] > 440:
                self.add_game(16,c_id,game016.Board,self.lang.d["Keyboard Skills"] + " - " + self.lang.d["English"],self.lang.d["Touch Typing"],"ico_g_1203.png")
                self.en_list.append("016")
        else:
            self.en_list = []
        c_id += 1
        self.add_game(20,c_id,game038.Board,self.lang.d["Numbers"],self.lang.d["Number Flashcards"],"ico_g_0300.png")
        self.add_game(102,c_id,game079.Board,self.lang.d["Number Spelling"],"","ico_g_0325.png")
        self.add_game(21,c_id,game061.Board,self.lang.d["Number Spelling"],self.lang.d["Match numbers to their spelling"],"ico_g_0323.png",variant=0)
        self.add_game(22,c_id,game046.Board,self.lang.d["Learn to Count"],"","ico_g_0301.png",variant=0)
        self.add_game(23,c_id,game046.Board,self.lang.d["Learn to Count"],self.lang.d["Basic Addition"],"ico_g_0317.png",variant=1)
        self.add_game(24,c_id,game046.Board,self.lang.d["Learn to Count"],self.lang.d["Basic Subtraction"],"ico_g_0318.png",variant=2)
        
        
        self.add_game(25,c_id,game027.Board,self.lang.d["Shopping List"],"","ico_g_0302.png")
        self.add_game(26,c_id,game036.Board,self.lang.d["Plus or Minus"],"","ico_g_0303.png")
        
        self.add_game(103,c_id,game080.Board,self.lang.d["Addition Table"] +"  ",self.lang.d["answer_enter"],"ico_g_0326.png")
        
        self.add_game(27,c_id,game004.Board,self.lang.d["Multiplication Table"],self.lang.d["Find the product"],"ico_g_0306.png")
        self.add_game(28,c_id,game034.Board,self.lang.d["Multiplication Table"]+" ",self.lang.d["Find the multiplier"],"ico_g_0307.png")
        self.add_game(29,c_id,game035.Board,self.lang.d["Division"],"","ico_g_0308.png")
        
        self.add_game(30,c_id,game031.Board,self.lang.d["Multiplication Table"] +"  ",self.lang.d["answer_enter"],"ico_g_0324.png")

        c_id += 1
        self.add_game(31,c_id,game060.Board,self.lang.d["Maths Matching Game"],self.lang.d["Addition"],"ico_g_0319.png",variant=0)#2
        self.add_game(32,c_id,game060.Board,self.lang.d["Maths Matching Game"],self.lang.d["Subtraction"],"ico_g_0320.png",variant=1)#3
        self.add_game(33,c_id,game060.Board,self.lang.d["Maths Matching Game"],self.lang.d["Multiplication"],"ico_g_0321.png",variant=2)#4
        self.add_game(34,c_id,game060.Board,self.lang.d["Maths Matching Game"],self.lang.d["Division"],"ico_g_0322.png",variant=3)#5
        
        self.add_game(35,c_id,game039.Board,self.lang.d["Basic Operations"],self.lang.d["Addition"],"ico_g_0309.png",variant=0)
        self.add_game(36,c_id,game039.Board,self.lang.d["Basic Operations"],self.lang.d["Subtraction"],"ico_g_0310.png",variant=1)
        self.add_game(37,c_id,game039.Board,self.lang.d["Basic Operations"],self.lang.d["Multiplication"],"ico_g_0311.png",variant=2)
        self.add_game(38,c_id,game039.Board,self.lang.d["Basic Operations"],self.lang.d["Division"],"ico_g_0312.png",variant=3)

        self.add_game(39,c_id,game019.Board,self.lang.d["Basic Operations"]+" 2",self.lang.d["Addition"],"ico_g_0313.png",variant=0)
        self.add_game(40,c_id,game019.Board,self.lang.d["Basic Operations"]+" 2",self.lang.d["Subtraction"],"ico_g_0314.png",variant=1)
        self.add_game(41,c_id,game019.Board,self.lang.d["Basic Operations"]+" 2",self.lang.d["Multiplication"],"ico_g_0315.png",variant=2)
        self.add_game(42,c_id,game019.Board,self.lang.d["Basic Operations"]+" 2",self.lang.d["Division"],"ico_g_0316.png",variant=3)
        
        c_id += 1
        self.add_game(43,c_id,game005.Board,self.lang.d["Sorting Numbers"],"","ico_g_0400.png")
        self.add_game(44,c_id,game011.Board,self.lang.d["Even or Odd"],"","ico_g_0405.png")
        self.add_game(45,c_id,game032.Board,self.lang.d["Number Comparison"],"","ico_g_0401.png")
        self.add_game(46,c_id,game033.Board,self.lang.d["Addition & Subtraction"],self.lang.d["Comparison"],"ico_g_0402.png")
        self.add_game(47,c_id,game026.Board,self.lang.d["Fractions"],self.lang.d["Comparison"],"ico_g_0403.png")
        self.add_game(48,c_id,game020.Board,self.lang.d["Decimal Fractions"],self.lang.d["Comparison"],"ico_g_0404.png")        
        
        self.add_game(49,c_id,game056.Board,self.lang.d["Fraction Groups"],"","ico_g_0406.png",variant=0) #new game
        self.add_game(50,c_id,game056.Board,self.lang.d["Fraction Groups"]+" 2","","ico_g_0407.png",variant=1) #new game
        self.add_game(51,c_id,game056.Board,self.lang.d["Fraction Groups"]+" 3","","ico_g_0408.png",variant=2) #new game
        self.add_game(52,c_id,game056.Board,self.lang.d["Percentages"],"","ico_g_0409.png",variant=3) #new game
        self.add_game(53,c_id,game056.Board,self.lang.d["Ratios"],"","ico_g_0410.png",variant=4) #new game
        
        c_id += 1
        self.add_game(54,c_id,game073.Board,self.lang.d["Columnar addition"],self.lang.d["Demonstration"],"ico_g_1100.png")
        self.add_game(55,c_id,game069.Board,self.lang.d["Columnar addition"],self.lang.d["DIY"],"ico_g_1101.png")

        self.add_game(56,c_id,game074.Board,self.lang.d["Columnar subtraction"],self.lang.d["Demonstration"],"ico_g_1102.png")
        self.add_game(57,c_id,game070.Board,self.lang.d["Columnar subtraction"],self.lang.d["DIY"],"ico_g_1103.png")

        self.add_game(58,c_id,game075.Board,self.lang.d["Long multiplication"],self.lang.d["Demonstration"],"ico_g_1104.png")
        self.add_game(59,c_id,game071.Board,self.lang.d["Long multiplication"],self.lang.d["DIY"],"ico_g_1105.png")

        self.add_game(60,c_id,game076.Board,self.lang.d["Long division"],self.lang.d["Demonstration"],"ico_g_1106.png")
        self.add_game(61,c_id,game072.Board,self.lang.d["Long division"],self.lang.d["DIY"],"ico_g_1107.png")
        
        c_id += 1
        self.add_game(62,c_id,game009.Board,self.lang.d["Shapes"],self.lang.d["Shape Flashcards"],"ico_g_0500.png")
        self.add_game(63,c_id,game043.Board,self.lang.d["Solids"],self.lang.d["Solid Flashcards"],"ico_g_0501.png")
        self.add_game(64,c_id,game059.Board,self.lang.d["ShapeMaker"],self.lang.d["lets_see_what_you_draw"],"ico_g_0502.png")
        self.add_game(65,c_id,game024.Board,self.lang.d["ShapeMaker"],self.lang.d["test_yourself"],"ico_g_0503.png")
        
        c_id += 1
        if self.mainloop.lang.lang == 'ca':
            self.add_game(104,c_id,game081.Board,"Rellotge amb horari en català", self.lang.d["Play_w_clock"],"ico_g_1005.png")
        self.add_game(66,c_id,game066.Board,self.lang.d["Clock0"],self.lang.d["Play_w_clock"],"ico_g_1000.png",variant=0)
        self.add_game(67,c_id,game063.Board,self.lang.d["Clock1"] + " - " + self.lang.d["Read time"],"","ico_g_1001.png")
        self.add_game(68,c_id,game064.Board,self.lang.d["Clock2"] + " - " + self.lang.d["Set time"],"","ico_g_1002.png")
        self.add_game(69,c_id,game065.Board,self.lang.d["Clock2"]+ " - " + self.lang.d["Set time"],self.lang.d["txt_only"],"ico_g_1003.png",variant=0)
        
        self.add_game(70,c_id,game078.Board,self.lang.d["TimeMatching"],"","ico_g_1004.png")
        
        if self.mainloop.lang.lang == 'ru':
            self.add_game(105,c_id,game066.Board,self.lang.d["Clock0 - Russian official time"],self.lang.d["Russian official - subtitle"],"ico_g_1006.png",variant=1)
            self.add_game(106,c_id,game065.Board,self.lang.d["Clock2 - Russian official time"],self.lang.d["Russian official - txt_only"],"ico_g_1007.png",variant=1)
            
        c_id += 1
        self.add_game(71,c_id,game021.Board,self.lang.d["Paint"],"","ico_g_0600.png")
        self.add_game(72,c_id,game042.Board,self.lang.d["Colour Matching"],self.lang.d["label the colours"],"ico_g_0601.png")

        self.add_game(73,c_id,game062.Board,self.lang.d["Colour Matching"] + " 2","","ico_g_0602.png")
        self.add_game(74,c_id,game051.Board,self.lang.d["Paint Mixer"],self.lang.d["Mixing RYB"],"ico_g_0603.png")
        self.add_game(75,c_id,game052.Board,self.lang.d["Ink Mixer"],self.lang.d["Mixing CMY"],"ico_g_0605.png")
        self.add_game(76,c_id,game055.Board,self.lang.d["Find the colour of the circle"],self.lang.d["Adjust CMY"],"ico_g_0607.png")
        self.add_game(77,c_id,game053.Board,self.lang.d["Light Mixer"],self.lang.d["Mixing RGB"],"ico_g_0604.png")
        self.add_game(78,c_id,game054.Board,self.lang.d["Find the colour of the circle"],self.lang.d["Adjust RGB"],"ico_g_0606.png")
        
        c_id += 1
        self.add_game(79,c_id,game012.Board,self.lang.d["Follow the Arrows"],self.lang.d["remember the directions"],"ico_g_0700.png")
        self.add_game(80,c_id,game006.Board,self.lang.d["Photographic Memory"],self.lang.d["Training"],"ico_g_0701.png")
        self.add_game(81,c_id,game007.Board,self.lang.d["Photographic Memory"]+" ",self.lang.d["Automatic Levels"],"ico_g_0702.png")
        self.add_game(82,c_id,game018.Board,self.lang.d["Match Animals Memory"],self.lang.d["Find pairs"],"ico_g_0703.png",variant=0)
        self.add_game(83,c_id,game018.Board,self.lang.d["Match Fruits"],self.lang.d["Find pairs"],"ico_g_0704.png",variant=1)
        self.add_game(84,c_id,game018.Board,self.lang.d["Match Vegetables"],self.lang.d["Find pairs"],"ico_g_0705.png",variant=2)
        self.add_game(85,c_id,game018.Board,self.lang.d["Match Numbers"],self.lang.d["Find pairs"],"ico_g_0706.png",variant=3)
        
        c_id += 1
        self.add_game(86,c_id,game029.Board,self.lang.d["Mouse Maze"],self.lang.d["Let's have some cheese"],"ico_g_0800.png")
        self.add_game(87,c_id,game028.Board,self.lang.d["Sheep Maze"],self.lang.d["Find the rest"],"ico_g_0801.png")

        self.add_game(88,c_id,game060.Board,self.lang.d["Match Animals"],self.lang.d["Find all matching animals"],"ico_g_0811.png",variant=4)#0
        self.add_game(89,c_id,game060.Board,self.lang.d["Match Animals"]+" 2",self.lang.d["Match animals to their shadows"],"ico_g_0812.png",variant=5)#1
        self.add_game(90,c_id,game008.Board,self.lang.d["Match Animals"]+" 3",self.lang.d["help me find my shadow"],"ico_g_0813.png")

        self.add_game(91,c_id,game041.Board,self.lang.d["Connect"]+" ",self.lang.d["Balloons with threads"],"ico_g_0803.png")
        self.add_game(92,c_id,game040.Board,self.lang.d["Connect"],self.lang.d["Numbers"],"ico_g_0802.png")
        self.add_game(93,c_id,game050.Board,self.lang.d["Connect"],self.lang.d["Numbers"]+" 2","ico_g_0806.png")
        self.add_game(94,c_id,game015.Board,self.lang.d["Fifteen"],self.lang.d["With a Twist"],"ico_g_0804.png")
        self.add_game(95,c_id,game045.Board,self.lang.d["Fifteen"] + " 2",self.lang.d["With a Twist"],"ico_g_0807.png")

        self.add_game(96,c_id,game044.Board,self.lang.d["Sliced Images"],self.lang.d["Sliced Animals"],"ico_g_0808.png",variant=0)
        self.add_game(97,c_id,game044.Board,self.lang.d["Sliced Images"],self.lang.d["Sliced Fruits"],"ico_g_0809.png",variant=1)
        self.add_game(98,c_id,game044.Board,self.lang.d["Sliced Images"],self.lang.d["Sliced Numbers"],"ico_g_0810.png",variant=2)
        
        self.add_game(99,c_id,game030.Board,self.lang.d["Hit the Mole"],"","ico_g_0805.png")

        c_id +=1
        self.add_game(100,c_id,game057.Board,self.lang.d["TicTacToe2"],self.lang.d["multiline-tictactoe"],"ico_g_0900.png")
        self.add_game(101,c_id,game058.Board,self.lang.d["TicTacToe3"],self.lang.d["multiline-tictactoe"],"ico_g_0901.png")
        
        
    def draw_menu(self,menu,menu_l,menu_r,l):
        mw = l.menu_r_w
        #menu.fill((70,70,70))
        menu.fill((255,255,255))
        menu_l.fill(cl.menu_l)
        menu_r.fill(cl.menu_r)
        #pygame.draw.line(menu_l,cl.black,[l.menu_l_w-1,0],[l.menu_l_w-1,l.screen_h],1)
        #pygame.draw.line(menu_r,cl.black,[l.menu_r_w-1,0],[l.menu_r_w-1,l.screen_h],1)
        #pygame.draw.line(menu,(255,170,0),[l.menu_w-1,0],[l.menu_w-1,l.screen_h - l.info_bar_offset_h],1)

        #load games from new category if changed
        self.change_category(self.active_cat)

        x=self.x_margin
        y=self.y_margin+l.misio_pos[3]+self.scroll_l
        for each_item in self.categories:
            each_item.rect.topleft = [x, y]
            y += self.icon_size + self.y_margin
            each_item.update()
            
        x=self.x_margin
        y=self.y_margin+l.misio_pos[3]+self.scroll_r
        c=5
        for each_item in self.games_current:
            each_item.rect.topleft = [x, y]
            each_item.update()
            y += self.cat_icon_size + self.y_margin
            c += 10
        #if category with current game is shown show the tab, otherwise hide it (move it off screen) 
        if self.games[self.active_game_id] in self.games_in_current_cat:
            bmr_top = (self.tab_game_id+self.tab_r_scroll)*(self.icon_size+self.y_margin)+2+l.misio_pos[3]
        else:
            bmr_top = -100
        bml_top = (self.active_cat+self.tab_l_scroll)*(self.icon_size+self.y_margin)+2+l.misio_pos[3]
        self.bookmarks[0].rect.topleft = [5,bml_top-2]
        self.bookmarks[1].rect.topleft = [5,bmr_top-2]
        
        self.bookmarks[0].update()
        self.bookmarks[1].update()
        
       
        #Draw all spites
        self.categories_list.draw(menu_l)
        self.games_in_current_cat.draw(menu_r)
        #for each in self.scroll_btns:
        #    each.update()
                    
    def change_category(self, cat_id):
        if self.prev_cat != self.active_cat:
            self.change_cat(cat_id)

    def change_cat(self, cat_id):
        self.scroll_r = 0
        self.tab_r_scroll = 0
        self.games_in_current_cat.empty()
        self.games_current = []
        for each_item in self.games:
            if each_item.cat_id == cat_id:
                self.games_in_current_cat.add(each_item)
                self.games_current.append(each_item)
        self.games_in_current_cat.add(self.bookmarks[1])
        self.games_in_current_cat.move_to_back(self.bookmarks[1])
        self.prev_cat = self.active_cat
        #self.games_in_current_cat.add(self.scroll_btns[1])
        #self.games_in_current_cat.move_to_front(self.scroll_btns[1])
        self.game_h = len(self.games_current)*(self.icon_size+self.y_margin)#-self.y_margin
