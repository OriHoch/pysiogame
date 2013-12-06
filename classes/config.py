# -*- coding: utf-8 -*-

import pickle
import os, sys

class Config():
    'holds some basic configuration data - screen size among others'
    def __init__(self):
        self.version = "1.30.811"
        #Screen Settings
        #set this to False if you want to manually set the screen size, but if you have manually resized the window the latest size will be used instead
        #self.screen_size_autodetect = True
        #self.screen_size_autodetect = False
        self.size_changed = False
        #enter the size of your screen manually if not using auto-detection
        #this will be overridden if self.screen_size_autodetect is set to True and if used earlier - the saved size will be used

        self.fs_width = 1024
        self.fs_height = 768
        
        #size_limits - don't let window resizing get out of hand [min_w, min_h, max_w, max_h]
        self.size_limits = [670,480,2000,2000] #[670,480,2000,2000] #670 - minimum to fit all buttons, 2000 - with over 2000 pixels each way pygame is not redrawing very well
        #self.fs_width = 1440
        #self.fs_height = 900
        
        #set total size of OS panels and window decorations on both sides - used in windowed version. Not so much important now with resizing enabled.
        #this will not be auto-detected
        self.os_panels_w = 2  #sum of widths of non-hiding vertical Panels (if any) and window border (1px on each side). 
        self.os_panels_h = 52 #sum of heights of non-hiding horizontal panels (ie. menu bar(s) + application bar + window bar + border, etc.).

        
        #the game will 'remember' at what level each game has been left and it will save this data for next session if the save_levels is left at True
        #to reset the game - remove the level_data.txt file check below for the location of these files - it will be recreated next time you close the game
        #if the pickle has been saved with python3 then python2 will not be able to open it and will reset all levels to 1
        #the data is automatically saved to file every time you switch game and on exit. 
        self.save_levels = True

        #the following 2 settings will be overridden by configuration file
        #to change any of these do this in the in-game preferences, except fullscreen if there's no config file the value below will be used.
        self.fullscreen = False
        #self.read_inst = False #no longer used
        self.google_trans_languages = False
        
        #Window title
        self.window_caption = "pySioGame - Educational Activity Pack for Kids"
        
        """
        #file names paths to level and language files
        $XDG_DATA_HOME defines the base directory relative to which user
        specific data files should be stored. If $XDG_DATA_HOME is either not
        set or empty, a default equal to $HOME/.local/share should be used.
        $XDG_CONFIG_HOME defines the base directory relative to which user
        specific configuration files should be stored. If $XDG_CONFIG_HOME is
        either not set or empty, a default equal to $HOME/.config should be
        used.
        """
        p = sys.platform
        if p == "linux" or p == "linux2":
            try:
                xdg_data_home = os.environ.get('XDG_DATA_HOME')
            except:
                xdg_data_home = None
                
            if xdg_data_home == None or xdg_data_home == "":
                home = os.environ.get('HOME')
                directory = os.path.join(home,'.local','share', 'pysiogame')
            else:
                directory = os.path.join(xdg_data_home, 'pysiogame')
                
            self.file_level = os.path.join(directory, 'level_data.txt')
            self.file_settings = os.path.join(directory, 'settings.txt')
            
        else: #if p == "darwin" or p == "win32" or p == "cygwin":
            self.file_level = os.path.abspath(os.path.expanduser("~/.config/pysiogame/level_data.txt"))
            self.file_settings = os.path.abspath(os.path.expanduser("~/.config/pysiogame/settings.txt"))
            directory = os.path.dirname(self.file_level)
            
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except:
            print("Error - can't create directory. The game data won't be saved.")
            
        #default settings
        self.loaded_settings = False
        #[language, talkative, untranslated languages, full screen, user_name, screen_w, screen_h]
        self.default_settings = ["en_gb",1,0,0,"", 0, 0]
        self.settings = []
        self.load_settings()
        if len(self.settings) != 7:
            self.settings = self.default_settings
            
    def reset_settings(self):
        self.settings = self.default_settings
        
    def load_settings(self):
        'loads saved settings from pickled file - language and screen size dimensions and mode'
        try:
            with open(self.file_settings,"rb") as s_file:
                self.settings = pickle.load(s_file)
            self.loaded_settings = True
        except:
            self.settings = self.default_settings
            
    def save_settings(self):
        'save settings to file'
        try:
            with open(self.file_settings, "wb") as s_file:
                pickle.dump(self.settings, s_file)
        except:
            print('Could not save settings')