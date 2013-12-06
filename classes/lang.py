# -*- coding: utf-8 -*-
from __future__ import with_statement
import os, sys
import pickle

    
# game003.py holds the GUI for language changing

class Language():
    def __init__(self, configo):
        self.config = configo
        #self.lang_settings = ["en_gb",1,0] #default settings
        self.alphabet_26 = ["en_gb","en_us","pt"]
        #self.loaded_settings = False
        #self.load_settings()
        """
        self.flag_files = ["flag_uk.png","flag_us.png","flag_pl.png","flag_gr.png","flag_es.png","flag_pt.png","flag_it.png","flag_fr.png","flag_de.png","flag_ru.png","flag_fi.png"]
        self.lang_titles = ["English","American English","Polski","Ελληνικά","Español","Português","Italiano","Français","Deutsch","Русский","Suomalainen"]
        self.all_lng = ["en_gb", "en_us", "pl", "gr", "es","pt","it","fr","de","ru","fi"]
        self.ok_lng = ["en_gb", "en_us", "pl", "gr", "es","pt","it"]
        """
        self.flag_files = ["flag_uk.png","flag_us.png","flag_es.png","flag_gr.png","flag_it.png", "flag_pl.png","flag_pt.png","flag_ru.png","flag_de.png","flag_fi.png","flag_fr.png"]
        self.lang_titles = ["English", "American English", "Español", "Ελληνικά", "Italiano", "Polski", "Português", "Русский", "Deutsch", "Suomalainen", "Français"]
        self.all_lng = ["en_gb", "en_us", "es", "gr","it", "pl" ,"pt","ru","de","fi","fr"]
        self.ok_lng = ["en_gb", "en_us", "es", "gr","it", "pl" ,"pt"]
        
        if self.config.settings[0] not in self.all_lng:
            self.config.reset_settings()
            
        self.lang = self.config.settings[0]
        self.get_lang_attr()
        
    def get_lang_attr(self):
        if self.lang == 'en_gb':
            import languages.en_gb
            import languages.word_lists.en_gb_di
            import languages.kbrd.en_gb
            import languages.kbrd.en_course
            #self.voice = ["-s 170","-a 100","-p 80","-ven+m1"]
            self.voice = ["-ven+m1"]
            #self.large_dict = languages.en_gb_long.my_dictionary
            self.di = languages.word_lists.en_gb_di.di
            self.lang_file = languages.en_gb
            self.kbrd = languages.kbrd.en_gb
            self.kbrd_course_mod = languages.kbrd.en_course
        elif self.lang == 'en_us':
            import languages.en_us
            import languages.word_lists.en_us_di
            import languages.kbrd.en_us
            import languages.kbrd.en_course
            #self.voice = ["-s 170","-a 100","-p 80","-ven-us+m1"]
            self.voice = ["-ven-us+m1"]
            self.di = languages.word_lists.en_us_di.di
            self.lang_file = languages.en_us
            self.kbrd = languages.kbrd.en_us
            self.kbrd_course_mod = languages.kbrd.en_course
        elif self.lang == 'pl':
            import languages.pl
            import languages.word_lists.pl_di
            import languages.kbrd.pl
            import languages.kbrd.pl_course
            #self.voice = ["-s 160","-a 100","-p 80","-vpl+m1"] #"-g 5",
            self.voice = ["-vpl+m1"]
            self.di = languages.word_lists.pl_di.di
            self.lang_file = languages.pl
            self.kbrd = languages.kbrd.pl
            self.kbrd_course_mod = languages.kbrd.pl_course
        elif self.lang == 'es':
            import languages.es
            import languages.word_lists.es_di
            #self.voice = ["-s 170","-a 100","-p 80","-ves+m1"]
            self.voice = ["-ves+m1"]
            self.di = languages.word_lists.es_di.di
            self.lang_file = languages.es
        elif self.lang == 'pt':
            import languages.pt
            import languages.word_lists.pt_di
            #self.voice = ["-s 170","-a 100","-p 80","-vpt-pt+m1"]
            self.voice = ["-vpt-pt+m1"]
            self.di = languages.word_lists.pt_di.di
            self.lang_file = languages.pt
        elif self.lang == 'fr':
            import languages.fr
            import languages.word_lists.fr_di
            #self.voice = ["-s 170","-a 100","-p 80","-vfr+m1"]
            self.voice = ["-vfr+m1"]
            self.di = languages.word_lists.fr_di.di
            self.lang_file = languages.fr
        elif self.lang == 'it':
            import languages.it
            import languages.word_lists.it_di
            #self.voice = ["-s 170","-a 100","-p 80","-vit+m1"]
            self.voice = ["-vit+m1"]
            self.di = languages.word_lists.it_di.di
            self.lang_file = languages.it
        elif self.lang == 'de':
            import languages.de
            import languages.word_lists.de_di
            #self.voice = ["-s 170","-a 100","-p 80","-vde+m1"]
            self.voice = ["-vde+m1"]
            self.di = languages.word_lists.de_di.di
            self.lang_file = languages.de
        elif self.lang == 'ru':
            import languages.ru
            import languages.word_lists.ru_di
            import languages.kbrd.ru
            import languages.kbrd.ru_course
            #self.voice = ["-s 130","-a 100","-p 80","-vru+m1"]
            self.voice = ["-vru+m1"]
            self.di = languages.word_lists.ru_di.di
            self.lang_file = languages.ru
            self.kbrd = languages.kbrd.ru
            self.kbrd_course_mod = languages.kbrd.ru_course
        elif self.lang == 'fi':
            import languages.fi
            import languages.word_lists.fi_di
            #self.voice = ["-s 170","-a 100","-p 80","-vfi+m1"]
            self.voice = ["-vfi+m1"]
            self.di = languages.word_lists.fi_di.di
            self.lang_file = languages.fi
        elif self.lang == 'gr':
            import languages.gr
            import languages.word_lists.gr_di
            import languages.kbrd.gr
            import languages.kbrd.gr_course
            #self.voice = ["-s 170","-a 100","-p 80","-vel+m1"]
            self.voice = ["-vel+m1"]
            self.di = languages.word_lists.gr_di.di
            self.lang_file = languages.gr
            self.kbrd = languages.kbrd.gr
            self.kbrd_course_mod = languages.kbrd.gr_course
        
        """
        if self.lang in ["en_gb","en_us","pl","ru"]:
            pass #self.kbrd_course = self.kbrd_course_mod.course
        else:
            import languages.kbrd.en_gb
            import languages.kbrd.en_course
            self.kbrd = languages.kbrd.ru
            self.kbrd_course_mod = languages.kbrd.ru_course
        """
        if self.lang not in ["en_gb","en_us","pl","ru","gr"]:
            import languages.kbrd.en_gb
            import languages.kbrd.en_course
            self.kbrd = languages.kbrd.en_gb
            self.kbrd_course_mod = languages.kbrd.en_course
            
        self.kbrd_course = self.kbrd_course_mod.course
            
        self.d = self.lang_file.d
        self.numbers = self.lang_file.numbers
        self.numbers2090 = self.lang_file.numbers2090
        self.n2txt = self.lang_file.n2txt
        
        self.solid_names = self.lang_file.solid_names
        self.shape_names = self.lang_file.shape_names
        self.fruit = self.lang_file.fruit
        self.fruits_1 = self.lang_file.fruits_1
        self.fruits_2 = self.lang_file.fruits_2
        self.plural_rules = self.lang_file.plural_rules
        self.letter_names = self.lang_file.letter_names
        
        
        self.alphabet_lc = self.lang_file.alphabet_lc
        self.alphabet_uc = self.lang_file.alphabet_uc
        self.accents_lc = self.lang_file.accents_lc
        self.accents_uc = self.lang_file.accents_uc
        
        
        #self.unicodify()
    """
    def load_settings(self):
        'loads saved language settings from pickled file'
        try:
            #with open(os.path.join('save',"lang_config.txt"),"rb") as lng_file:
            #file_name = os.path.abspath(os.path.expanduser("~/.config/pysiogame/lang_config.txt"))
            file_name = self.config.file_lang
            with open(file_name,"rb") as lng_file:
                self.lang_settings = pickle.load(lng_file)
            self.loaded_settings = True
        except:
            self.lang_settings = ["en_gb",1,0,0,""]
    """