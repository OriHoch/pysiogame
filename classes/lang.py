# -*- coding: utf-8 -*-
from __future__ import with_statement
import os, sys
import pickle

import gettext
import locale
from classes.extras import unival
from classes.extras import reverse
# game003.py holds the GUI for language switching

class Language():
    def __init__(self, configo):
        lib_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.locale_dir = unival(os.path.join(lib_dir, 'locale/'))
        if 'LC_MESSAGES' in vars(locale):
            # linux
            locale.setlocale(locale.LC_MESSAGES, '')
        else:
            # windows
            locale.setlocale(locale.LC_ALL, '')
        #locale.setlocale(locale.LC_MESSAGES, '') # use user's preferred locale
        
        self.config = configo
        self.alphabet_26 = ["en_GB","en_US","pt_PT"]
        self.def_imported = False
        self.trans = dict()
        self.lang_titles = self.config.lang_titles
        self.all_lng = self.config.all_lng
        self.ok_lng = self.config.ok_lng
        
    def load_language(self, lang_code = None):
        if lang_code == None:
            if self.config.settings["lang"] not in self.all_lng:
                self.config.reset_settings()
                
            self.lang = self.config.settings["lang"]
        else:
            if lang_code not in self.all_lng:
                self.lang = 'en_GB'
            else:
                self.lang = lang_code
        
        self.get_lang_attr()
        
    def _n(self, word, count):
        return self.trans[self.lang].ngettext(word, word, count)
        
    def get_lang_attr(self):
        filename = os.path.join(self.locale_dir, self.lang, "LC_MESSAGES", "pysiogame.mo")
        #filename = "locale/%s/LC_MESSAGES/pysiogame.mo" % self.lang
        try:
            #print("Opening message file %s for locale %s" % (filename, self.lang) )
            self.trans[self.lang] = gettext.GNUTranslations(open( filename, "rb" ) )
        except IOError:
            print("Locale not found. Using default messages")
            self.trans[self.lang]  = gettext.NullTranslations()

        self.trans[self.lang].install()
        
        import i18n.custom.default
        self.oi18n = i18n.custom.default.I18n()
        self.ltr_text = True
        self.ltr_numbers = True
        self.ltr_math = True
        self.has_uc = True
        self.has_cursive = True
        if self.lang == 'en_US':
            import i18n.custom.en_us
            import i18n.custom.word_lists.en_us_di
            import i18n.custom.kbrd.en_us
            import i18n.custom.kbrd.en_course
            #self.voice = ["-s 170","-a 100","-p 80","-ven-us+m1"]
            self.voice = ["-ven-us+m1"]
            self.di = i18n.custom.word_lists.en_us_di.di
            self.lang_file = i18n.custom.en_us
            self.kbrd = i18n.custom.kbrd.en_us
            self.kbrd_course_mod = i18n.custom.kbrd.en_course
        elif self.lang == 'pl':
            import i18n.custom.pl
            import i18n.custom.word_lists.pl_di
            import i18n.custom.kbrd.pl
            import i18n.custom.kbrd.pl_course
            #self.voice = ["-s 160","-a 100","-p 80","-vpl+m1"] #"-g 5",
            self.voice = ["-vpl+m1"]
            self.di = i18n.custom.word_lists.pl_di.di
            self.lang_file = i18n.custom.pl
            self.kbrd = i18n.custom.kbrd.pl
            self.kbrd_course_mod = i18n.custom.kbrd.pl_course
        elif self.lang == 'ca':
            import i18n.custom.ca
            import i18n.custom.word_lists.ca_di
            self.voice = ["-vca+m1"]
            self.di = i18n.custom.word_lists.ca_di.di
            self.lang_file = i18n.custom.ca
        elif self.lang == 'es_ES':
            import i18n.custom.es
            import i18n.custom.word_lists.es_di
            self.voice = ["-ves+m1"]
            self.di = i18n.custom.word_lists.es_di.di
            self.lang_file = i18n.custom.es
        elif self.lang == 'pt_PT':
            import i18n.custom.pt
            import i18n.custom.word_lists.pt_di
            self.voice = ["-vpt-pt+m1"]
            self.di = i18n.custom.word_lists.pt_di.di
            self.lang_file = i18n.custom.pt
        elif self.lang == 'fr':
            import i18n.custom.fr
            import i18n.custom.word_lists.fr_di
            self.voice = ["-vfr+m1"]
            self.di = i18n.custom.word_lists.fr_di.di
            self.lang_file = i18n.custom.fr
        elif self.lang == 'it':
            import i18n.custom.it
            import i18n.custom.word_lists.it_di
            self.voice = ["-vit+m1"]
            self.di = i18n.custom.word_lists.it_di.di
            self.lang_file = i18n.custom.it
        elif self.lang == 'de':
            import i18n.custom.de
            import i18n.custom.word_lists.de_di
            self.voice = ["-vde+m1"]
            self.di = i18n.custom.word_lists.de_di.di
            self.lang_file = i18n.custom.de
        elif self.lang == 'ru':
            import i18n.custom.ru
            import i18n.custom.word_lists.ru_di
            import i18n.custom.kbrd.ru
            import i18n.custom.kbrd.ru_course
            #self.voice = ["-s 130","-a 100","-p 80","-vru+m1"]
            #self.voice = ["-vru+m1"] s 150 -vru
            self.voice = ["-s 150","-vru"]
            self.di = i18n.custom.word_lists.ru_di.di
            self.lang_file = i18n.custom.ru
            self.kbrd = i18n.custom.kbrd.ru
            self.kbrd_course_mod = i18n.custom.kbrd.ru_course
            self.time2spk = self.lang_file.time2spk
            self.time2officialstr = self.lang_file.time2officialstr
            self.time2officialspk = self.lang_file.time2officialspk
        elif self.lang == 'fi':
            import i18n.custom.fi
            import i18n.custom.word_lists.fi_di
            self.voice = ["-vfi+m1"]
            self.di = i18n.custom.word_lists.fi_di.di
            self.lang_file = i18n.custom.fi
        elif self.lang == 'el': #Greek
            import i18n.custom.el
            import i18n.custom.word_lists.el_di
            import i18n.custom.kbrd.el
            import i18n.custom.kbrd.el_course
            self.voice = ["-vel+m1"]
            self.di = i18n.custom.word_lists.el_di.di
            self.lang_file = i18n.custom.el
            self.kbrd = i18n.custom.kbrd.el
            self.kbrd_course_mod = i18n.custom.kbrd.el_course
        elif self.lang == 'he': #Hebrew
            import i18n.custom.he
            import i18n.custom.word_lists.he_di
            self.voice = None #["-vel+m1"]
            self.di = i18n.custom.word_lists.he_di.di
            self.lang_file = i18n.custom.he
            self.ltr_text = False
            self.has_uc = False
            self.has_cursive = False
            alpha = i18n.custom.he.alpha
        elif self.lang == 'te_ST':
            import i18n.custom.te_st
            import i18n.custom.word_lists.te_st_di
            self.voice = ["-ven+m1"]
            self.di = i18n.custom.word_lists.te_st_di.di
            self.lang_file = i18n.custom.te_st
        else:# self.lang == 'en_GB':
            import i18n.custom.en_gb
            import i18n.custom.word_lists.en_gb_di
            import i18n.custom.kbrd.en_gb
            import i18n.custom.kbrd.en_course
            self.voice = ["-ven+m1"]
            self.di = i18n.custom.word_lists.en_gb_di.di
            self.lang_file = i18n.custom.en_gb
            self.kbrd = i18n.custom.kbrd.en_gb
            self.kbrd_course_mod = i18n.custom.kbrd.en_course
        
        if self.lang not in ["en_gb","en_us","pl","ru","el"]:
            import i18n.custom.kbrd.en_gb
            import i18n.custom.kbrd.en_course
            self.kbrd = i18n.custom.kbrd.en_gb
            self.kbrd_course_mod = i18n.custom.kbrd.en_course
        self.d = dict()
        self.b = dict()
        self.dp = dict()
        self.kbrd_course = self.kbrd_course_mod.course
        
        self.d.update(self.oi18n.d)
        self.d.update(self.lang_file.d)
        self.b.update(self.oi18n.b)
        self.numbers = self.lang_file.numbers
        self.numbers2090 = self.lang_file.numbers2090
        self.n2txt = self.lang_file.n2txt
        self.time2str = self.lang_file.time2str
        
        self.solid_names = self.oi18n.solid_names
        self.shape_names = self.oi18n.shape_names
        self.letter_names = self.lang_file.letter_names
        
        if not self.ltr_text:
            for each_d in [self.d, self.b]:
                for key in each_d.keys():
                    if isinstance(each_d[key], list):
                        for index in range(len(each_d[key])):
                            if sys.version_info < (3, 0):
                                if isinstance(each_d[key][index], basestring):
                                    each_d[key][index] = reverse(each_d[key][index], alpha)
                            else:
                                if isinstance(each_d[key][index], str):
                                    each_d[key][index] = reverse(each_d[key][index], alpha)
                        
                    else:
                        each_d[key] = reverse(each_d[key], alpha)
        
            for each in [self.solid_names, self.shape_names]:
                for index in range(len(each)):
                    if sys.version_info < (3, 0):
                        if isinstance(each[index], basestring):
                            each[index] = reverse(each[index], alpha)
                    else:
                        if isinstance(each[index], str):
                            each[index] = reverse(each[index], alpha)
        
        
        self.dp.update(self.d)
        if self.lang == 'ru':
            self.dp.update(self.lang_file.dp)
            #self.dp["Great job!"] = self.lang_file.dp["Great job!"][:]
            
        self.alphabet_lc = self.lang_file.alphabet_lc
        self.alphabet_uc = self.lang_file.alphabet_uc
        self.accents_lc = self.lang_file.accents_lc
        self.accents_uc = self.lang_file.accents_uc
        