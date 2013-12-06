class Layout:
    def __init__(self,mainloop, screen_w, screen_h,x_count=26,y_count=11,game_type="Board"):
        self.screen_w = screen_w
        self.screen_h = screen_h   
        self.mainloop = mainloop
        self.game_type = game_type
        self.update_layout(x_count,y_count)

    def update_layout(self,x_count=0,y_count=0):
        self.x_count = x_count
        self.y_count = y_count

        self.menu_w = 124+5 #+5 - extra space to make the gap for tabs to look ok
        self.menu_a_w = self.menu_w
        #50+10+50+10+1
        self.grid_line_w = 1
        self.info_bar_h = 76
        self.info_bar_offset_h_init = 76
        self.menu_w_offset = 0
        self.avail_game_w = self.screen_w - self.menu_w  
        self.avail_game_h = self.screen_h - self.info_bar_h
        if self.game_type == "Board":
            #find the right size (scale) for a single square and calculate panels' sizes
            scale_x = (self.screen_w - self.menu_w - self.grid_line_w) // x_count
            scale_y = (self.screen_h - self.info_bar_h - self.grid_line_w) // y_count
    
            if scale_x < scale_y:
                self.scale = scale_x
            else:
                self.scale = scale_y
                
            self.menu_w_offset = (self.screen_w - self.menu_w) - self.scale*x_count - self.grid_line_w#(screen_w - menu_w) % x_count
        
            self.menu_w += self.menu_w_offset
            self.width=self.scale #width of a single square
            self.height=self.scale
            self.game_h = y_count*self.height+self.grid_line_w
            
        elif self.game_type == "Puzzle":
            self.game_h = self.screen_h - self.info_bar_h
            
        self.game_w = self.screen_w - self.menu_w
        self.info_bar_offset_h = self.info_bar_offset_h_init+ (self.screen_h - self.info_bar_offset_h_init) - self.game_h
        self.menu_pos = (0,0, self.menu_w, self.screen_h)

        self.menu_l_w = 62
        self.menu_r_w = 62 #self.menu_w - self.menu_l_w
        self.menu_l_pos = (0,0, self.menu_l_w, self.screen_h)
        self.menu_r_pos = (self.menu_l_w,0, self.menu_r_w, self.screen_h)
        #self.game_pos = (self.menu_w,0, self.game_w, self.game_h) #changed
        self.game_pos = (self.menu_w,0, self.game_w, self.game_h) #changed
        self.misio_pos = (0,0, 123, 123)
        self.info_bar_offset_pos = (self.menu_w - self.menu_w_offset, self.game_h, self.game_w + self.menu_w_offset, self.info_bar_offset_h)
        self.info_bar_pos = (1, self.info_bar_offset_h - self.info_bar_h, self.game_w-1+self.menu_w_offset, self.info_bar_h)
        self.info_top = self.game_h + self.info_bar_pos[1]
        
    def draw_layout(self):
        pass
        
    def update_layout_fs(self,screen_w, screen_h,x_count,y_count):
        #update layout after switching from fullscreen to windowed view
        self.game_type = self.mainloop.game_board.game_type
        self.__init__(self.mainloop, screen_w, screen_h,x_count,y_count,self.game_type)
        self.mainloop.m.update_scroll_pos()