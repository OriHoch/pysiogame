# -*- coding: utf-8 -*-

import pygame
import os, sys
import classes.extras
import pygame.mixer

sounds = pygame.mixer
sounds.init()

sound_9 = '140506__blackstalian__click-sfx4b.ogg'
sound_8 = '162465__kastenfrosch__lostitem.ogg'
s4 = sounds.Sound(os.path.join('res', 'sounds', sound_9))
s5 = sounds.Sound(os.path.join('res', 'sounds', sound_8))

class BaseButton(pygame.sprite.Sprite):
    def __init__(self,panel,pos_x, pos_y, width, height, img_src_1="", img_src_2="", img_src_3="", rev=False):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.pos = [pos_x, pos_y]
        self.color = (255, 255, 255) #(70,70,70)#70
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.rect.width = width
        self.img_src_1 = img_src_1
        self.img_src_2 = img_src_2  
        self.img_src_3 = img_src_3  
        self.update_fonts()
        self.hasimg = False
        
        if self.btntype == "imgbtn":
            self.load_images(rev)
        elif self.btntype in ["levels", "titles"]:
            self.update_levels()

    def update_fonts(self):
        if self.btn_id in [2,6]:
            self.font  = self.panel.fonts[0]
            self.font2 = self.panel.fonts[1]
            self.font3 = self.panel.fonts[2]
            self.font4 = self.panel.fonts[3]
                
class Button(BaseButton):
    def __init__(self, panel, pos_x, pos_y, width, height, btntype="imgbtn", img_src_1="", img_src_2="", img_src_3="", rev=False):
        self.btn_id = len(panel.btns)
        self.panel = panel
        self.btntype = btntype
        BaseButton.__init__(self,panel,pos_x, pos_y, width, height, img_src_1, img_src_2, img_src_3, rev)
        
    def load_images(self, rev):
        self.img_pos = (0,0)
        try:
            self.img_1 = pygame.image.load(os.path.join('res', 'images', self.img_src_1)).convert()
            self.img_2 = pygame.image.load(os.path.join('res', 'images', self.img_src_2)).convert()
            if self.img_src_3 != "":
                self.img_3 = pygame.image.load(os.path.join('res', 'images', self.img_src_3)).convert()
            if rev:
                self.img_1 = pygame.transform.flip(self.img_1, 1, 0)
                self.img_2 = pygame.transform.flip(self.img_2, 1, 0)
            self.img = self.img_2
            self.hasimg = True
        except:
            pass

        self.update()
        
    def update_levels(self):
        #unsuccessful attempt to center the text
        if 1 < self.panel.level.games_per_lvl != 99:
            text2 = self.font2.render("%s/%s" % (self.panel.level.game_step, self.panel.level.games_per_lvl), 1, self.panel.font_color)
            textpos2 = text2.get_rect(centerx=self.image.get_width()//2)
            self.image.blit(text2, (textpos2[0],40))
            lvl_lift = -9
        else:
            lvl_lift = 3
            
        if self.panel.level.lvl_count > 1:
            if self.panel.level.completed > 0:
                font_color = self.panel.font_color2
            else:
                font_color = self.panel.font_color3
            text = self.font.render("%s" % (self.panel.level.lvl), 1, font_color)
            textpos1 = text.get_rect(centerx=self.image.get_width()//2)
            self.image.blit(text, (textpos1[0],lvl_lift))
            
    def update_title(self):
        #book 3
        text = self.font3.render("%s" % (self.panel.title), 1, self.panel.font_color)
        text2 = self.font4.render("%s" % (self.panel.subtitle), 1, self.panel.font_color1)
        #print text.rect.w
        tw1 = self.font3.size(self.panel.title)[0]
        tw2 = self.font4.size(self.panel.subtitle)[0]
        if self.panel.mainloop.lang.ltr_text:
            ttx = 0
            stx = 0
        else:
            ttx = self.panel.title_space - tw1 - 10
            stx = self.panel.title_space - tw2 - 10
            
        if self.panel.title_space == 0 or tw1 < self.panel.title_space:
            self.image.blit(text, (ttx,2))
            if tw2 < self.panel.title_space:
                self.image.blit(text2, (stx,39))
            
    def update(self):
        self.image.fill(self.color)
        if self.btntype == "imgbtn":
            self.image.blit(self.img, self.img_pos)
        elif self.btntype == "levels":
            self.update_levels()
        elif self.btntype == "titles":
        	self.update_title()

class InfoBar():
    def __init__(self,mainloop):
        self.btns = []
        
        #orange
        self.font_color = (255,75,0,0) #0,0,0,0)
        self.font_color1 = (60,60,60,0)
        
        self.font_color2 = (130,0,115,0)
        self.font_color3 = (255,130,240,0)
        
        
        self.font_color2 = (255,75,0,0) #0,0,0,0)
        self.font_color3 = (90,90,90,0)
        
        self.hidden = False
        self.close_dialog = False
        self.mainloop = mainloop
        self.margin_top = 13
        self.lang = self.mainloop.lang
        self.arrow_down = False
        self.title_space = 0
        self.title = ""
        self.subtitle = ""
        self.btn_list = pygame.sprite.LayeredUpdates()
        self.reset_buttons()
        self.update_fonts()
        
    def update_fonts(self):
        self.fonts = []
        points = int(round((60 * 72 /96),0))
        sizes = [points, points//2, int(points/1.9), int(points/2.6)]    
            
        for i in range(4):
            self.fonts.append(pygame.font.Font(os.path.join('res', 'fonts', 'FreeSansBold', 'FreeSansBold.ttf'), sizes[i]))
        
        for each in self.btns:
            each.update_fonts()
        self.reset_titles()

    def new_game(self,game_board,screen):
        self.game_board = game_board
        self.level = self.game_board.level
        self.screen = screen
        self.l = self.game_board.layout
        self.height = self.l.info_bar_h
        self.height_o = self.l.info_bar_offset_h
        self.width = self.l.info_bar_pos[2]#self.game_board.layout.screen_w - self.m_offset
        if len(self.btns) == 0:
            self.add_btns()
        self.layout_update()
        self.game_board.dialog.layout_update()

    def hover(self,pos,l):
        for btn in self.btns:
            if btn.rect.topleft[0] < (pos[0] - l.menu_w + 1) < (btn.rect.topleft[0] + btn.width) and btn.rect.topleft[1] < (pos[1] - l.info_bar_pos[1]) < (btn.rect.topleft[1] + btn.height):
                if btn.hasimg:
                    self.mainloop.redraw_needed[1] = True                
                    return btn
        return False

    def handle(self,event,layout,mainloop):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Change the x/y screen coordinates to grid coordinates
            pos = event.pos
            btn = self.hover(pos,layout)
            #if left button pressed:
            if event.button == 1:
                if btn != False:
                    if btn.btn_id == 0:
                        btn.img = btn.img_2
                        self.game_board.check_result()
                        
                    elif btn.btn_id == 1:
                        self.level.leveldown()
                        if self.level.lvl == 1:
                            btn.img = btn.img_2
    
                    elif btn.btn_id == 3:
                        self.level.levelup()
                        if self.level.lvl == self.level.lvl_count:
                            btn.img = btn.img_2
                    
                    elif btn.btn_id == 4: #clicked on close button
                        if self.close_dialog == True:
                            mainloop.done = True
                            mainloop.done4good = True
                        else:
                            self.sure_to_close()
    
                    elif btn.btn_id == 5:
                        self.level.load_level()
                        if self.mainloop.config.settings["sounds"]:
                            s4.play()
                        
                    elif btn.btn_id == 7:
                        self.level.chapter_down()
                        if self.level.lvl == 1:
                            btn.img = btn.img_2
                            
                    elif btn.btn_id == 8:
                        self.level.chapter_up()
                        if self.level.lvl == self.level.lvl_count:
                            btn.img = btn.img_2
                            
                    elif btn.btn_id == 9:
                        self.arrow_down = True
                        self.mainloop.game_board.direction[0] = -1
                    elif btn.btn_id == 10:
                        self.arrow_down = True
                        self.mainloop.game_board.direction[0] = 1
                    elif btn.btn_id == 11:
                        self.arrow_down = True
                        self.mainloop.game_board.direction[1] = -1
                    elif btn.btn_id == 12:
                        self.arrow_down = True
                        self.mainloop.game_board.direction[1] = 1
                    if self.arrow_down:
                        self.mainloop.game_board.check_direction_kdown()

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.arrow_down:
                self.arrow_down = False
                self.mainloop.game_board.direction = [0,0]
                self.mainloop.game_board.check_direction_kup()
            
        elif event.type == pygame.MOUSEMOTION:
            if self.mainloop.info.title != self.mainloop.m.games[self.mainloop.m.active_game_id].title:
                self.reset_titles()
            if self.hidden == True:
                if self.close_dialog == False:
                    self.buttons_restore()
            pos = event.pos
            btn = self.hover(pos,layout)
            if btn != False:
                if btn.hasimg:
                    if not (((btn.btn_id == 1 or btn.btn_id == 7) and self.level.lvl == 1) or ((btn.btn_id == 3 or btn.btn_id == 8) and self.level.lvl == self.level.lvl_count)):# or (btn.btn_id == 0)):# and self.game_board.changed_since_check == False)):                 
                        self.resetbtns()                        
                        btn.img = btn.img_1
            else:
                self.resetbtns()
                self.close_dialog = False
                
    def reset_titles(self):
        if self.close_dialog == False:
            #book 1
            self.title = self.mainloop.m.games[self.mainloop.m.active_game_id].title
            self.subtitle = self.mainloop.m.games[self.mainloop.m.active_game_id].subtitle                        
            self.mainloop.redraw_needed[1] = True
            self.mainloop.m.mouseenter = -1
            self.mainloop.m.mouseenter_cat = -1
       
    def resetbtns(self):
        for btn in self.btns:
            if btn.hasimg:
                btn.img = btn.img_2
        
    def add_btn(self, panel, pos_x, pos_y, btn_size_x, btn_size_y, btntype="imgbtn", img_src_1="", img_src_2="", img_src_3="", rev=False):
        new_button = Button(panel, pos_x, pos_y, btn_size_x, btn_size_y, btntype, img_src_1, img_src_2,img_src_3, rev)
        self.btns.append(new_button)
        self.btn_list.add(new_button)

    def add_btns(self):
        self.add_btn(self,122,5+self.margin_top,84,66,"imgbtn","info_ok1.png", "info_ok2.png", "info_ok3.png")
        self.add_btn(self,self.width-318,5+self.margin_top,64,66,"imgbtn","info_arrow1.png", "info_arrow2.png")
        self.add_btn(self,self.width-253,5+self.margin_top,74,66,"levels")#level number label
        self.add_btn(self,self.width-178,5+self.margin_top,64,66,"imgbtn","info_arrow1.png","info_arrow2.png","",True)
        self.add_btn(self,self.width-71,5+self.margin_top,66,66,"imgbtn","info_close1.png","info_close2.png")
        self.add_btn(self,222,5+self.margin_top,63,66,"imgbtn","info_refresh1.png","info_refresh2.png")
        title_width = self.width #-303 - (168+5+20)-5
        self.add_btn(self,300,5+self.margin_top,title_width,66,"titles")
        
        self.add_btn(self,self.width-351,5+self.margin_top,33,66,"imgbtn","info_lvls1.png","info_lvls2.png")
        self.add_btn(self,self.width-113,5+self.margin_top,33,66,"imgbtn","info_lvls1.png","info_lvls2.png","",True)
        self.add_btn(self,5,2+self.margin_top,34,72,"imgbtn","info_k_lr1.png","info_k_lr2.png")
        self.add_btn(self,78,2+self.margin_top,34,72,"imgbtn","info_k_lr1.png","info_k_lr2.png","",True)
        self.add_btn(self,41,2+self.margin_top,35,35,"imgbtn","info_k_up1.png","info_k_up2.png")
        self.add_btn(self,41,2+35+2+self.margin_top,35,35,"imgbtn","info_k_down1.png","info_k_down2.png")
        
        #add a layer of solid colour behind right-aligned buttons
        self.add_btn(self,self.width-323,5+self.margin_top,323,66,"btn_bg")

        self.btn_list.move_to_back(self.btns[13]) 
        self.btn_list.move_to_back(self.btns[6]) 


    def layout_update(self):
        self.btns[1].rect.left = self.width-318
        self.btns[2].rect.left = self.width-253
        self.btns[3].rect.left = self.width-178
        self.btns[4].rect.left = self.width-71
        self.btns[7].rect.left = self.width-351
        self.btns[8].rect.left = self.width-113
        self.btns[13].rect.left = self.width-318
        
        self.reset_alignment()
        self.check_btn_tops()
        
    def title_only(self):
        self.hide_buttons(0,0,0,0,0,0,1,0,0)
        self.mainloop.redraw_needed[1] = True
        self.hidden = True
        self.btn_list.move_to_front(self.btns[6])
        self.layout_update()
        self.title_space = self.width - 10
        
    def sure_to_close(self):
        self.hide_buttons(0,0,0,0,1,0,1,0,0)
        self.mainloop.redraw_needed[1] = True
        self.hidden = True
        self.close_dialog = True
        self.title = classes.extras.unival(self.lang.d["close_confirm"])
        self.subtitle = ""
        if self.mainloop.config.settings["sounds"]:
            s5.play()
        self.layout_update()
        
    def buttons_restore(self):
        a = self.mainloop.game_board.vis_buttons
        self.hide_buttonsa(a)
        self.mainloop.redraw_needed[1] = True
        self.hidden = False
        self.btn_list.move_to_back(self.btns[6]) 
        self.layout_update()
        
    def align_to_left(self):
        if self.visible_btns[8] == 0:
            if self.visible_btns[0] == 0 and self.visible_btns[5] == 1:
                self.btns[5].rect.left = 5
                self.btns[6].rect.left = 78
            elif self.visible_btns[0] == 0 and self.visible_btns[5] == 0:
                self.btns[6].rect.left = 5
            elif self.visible_btns[0] == 1 and self.visible_btns[5] == 0:
                self.btns[0].rect.left = 5
                self.btns[6].rect.left = 105
        else:
            if self.visible_btns[0] == 0 and self.visible_btns[5] == 1:
                self.btns[5].rect.left = 142 #5+117+20
                self.btns[6].rect.left = 215 #78+117+20
            elif self.visible_btns[0] == 0 and self.visible_btns[5] == 0:
                self.btns[6].rect.left = 142 #5+117+20
            elif self.visible_btns[0] == 1 and self.visible_btns[5] == 0:
                self.btns[0].rect.left = 142 #5+117+20
                self.btns[6].rect.left = 242 #105+117+20
        
    def reset_alignment(self):
        if self.visible_btns[7] == 0:
            pass #self.btns[1].rect.left = self.width-303
            #self.btns[2].rect.left = self.width-233
            #self.btns[3].rect.left = self.width-153 
            
        if self.visible_btns[8] == 0:
            self.btns[0].rect.left = 5
            self.btns[5].rect.left = 105
            self.btns[6].rect.left = 183
        else:
            self.btns[0].rect.left = 122
            self.btns[5].rect.left = 222
            self.btns[6].rect.left = 300

    def align_to_right(self):
        if self.visible_btns[7] == 1:
            self.btns[1].rect.left = self.width-318
            self.btns[2].rect.left = self.width-253
            self.btns[3].rect.left = self.width-178
        else:
            self.btns[1].rect.left = self.width-288
            self.btns[2].rect.left = self.width-223
            self.btns[3].rect.left = self.width-148
        
    def hide_buttons(self,a,b,c,d,e,f,g,h,i):
        self.visible_btns = [a,b,c,d,e,f,g,h,i]
        
    def hide_buttonsa(self, a):
        self.visible_btns = a
        
    def reset_buttons(self):
        self.visible_btns = [1,1,1,1,1,1,1,0,0]
        
    def check_btn_tops(self):
        #                      0  1          2     3            4     5      6       7             8
        #self.visible_btns = [ok,left_arrow,levels,right_arrow,close,refresh,titles, fast forward, keyboard]
        #self.visible_btns = [1,1,1,1,1,1,1,0,0]
        #if sum(self.visible_btns) < 7:
        vb = self.visible_btns
        for i in range(9):
            if vb[i]==0:
                if i < 7:
                    self.btns[i].rect.top = -200
                elif i==7:
                    self.btns[7].rect.top = -200
                    self.btns[8].rect.top = -200
                else:
                    self.btns[9].rect.top = -200
                    self.btns[10].rect.top = -200
                    self.btns[11].rect.top = -200
                    self.btns[12].rect.top = -200
            else:
                if i < 7:
                    self.btns[i].rect.top = 5 + self.margin_top
                elif i==7:
                    self.btns[7].rect.top = 5 + self.margin_top
                    self.btns[8].rect.top = 5 + self.margin_top
                else:
                    self.btns[9].rect.top = 2 + self.margin_top
                    self.btns[10].rect.top = 2 + self.margin_top
                    self.btns[11].rect.top = 2 + self.margin_top
                    self.btns[12].rect.top = 39 + self.margin_top
                    
        if vb[0] == 0 or vb[5] == 0 or vb[8] == 0:
            self.align_to_left()
        if vb[7] == 0:
            self.align_to_right()
        
        #adjusting the position of the background strip behind the right-aligned buttons
        if vb[1:4] == [0,0,0] and vb[7] == 0:
            self.btns[13].rect.left = self.width-71 -5
        elif vb[7] == 1:
            self.btns[13].rect.left = self.width-351 -5
        elif vb[1] == 1 and vb[7] == 0:
            self.btns[13].rect.left = self.width-288-5
        elif vb[1] == 0 and vb[2] == 1:
            self.btns[13].rect.left = self.width-223-5
        else:
            self.btns[13].rect.left = self.width - 5
        #title space
        self.rescale_title_space()
        
    def rescale_title_space(self):        
        if self.hidden == False or self.close_dialog:
            self.title_space = self.btns[13].rect.left - self.btns[6].rect.left
        elif self.hidden == True and self.close_dialog == False:
            self.title_space = self.width - 10
            
    def draw(self,screen):
        #draw info bar
        screen.fill((255,255,255))
        #colors = ((250,250,250),(233,233,233),(192,192,192),(141,141,141),(137,137,137))#,(255,255,255),(240,223,238),(133,0,116),(148,31,133))
        #colors = ((250,250,250),(233,233,233),(233,233,233),(192,192,192),(192,192,192),(141,141,141),(141,141,141),(137,137,137),(137,137,137))#,(255,255,255),(240,223,238),(133,0,116),(148,31,133))
        colors = ((250,250,250),(242,242,242),(236,236,236),(228,228,228),(218,218,218),(206,206,206),(193,193,193),(180,180,180),(166,166,166),(152,152,152),(140,140,140),(177,177,177))        
        hs = 0
        for each in colors:
            pygame.draw.line(screen,each,[0,hs],[self.game_board.layout.screen_w - self.game_board.layout.menu_w,hs],1)
            hs += 1
        for each_item in self.btns:
            each_item.update()

        self.btn_list.draw(screen)
        
