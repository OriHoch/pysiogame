# -*- coding: utf-8 -*-

import classes.level_controller as lc
import classes.game_driver as gd
import classes.extras as ex
import classes.board

import math
import pygame
import random
import sys

class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,11,9)
        
        
    def create_game_objects(self, level = 1):
        #create non-movable objects
        self.board.draw_grid = False
        s = random.randrange(30, 80)
        v = random.randrange(200, 255)
        h = random.randrange(0, 225)
        self.letter_color = ex.hsv_to_rgb(h,s,v)
        font_color = ex.hsv_to_rgb(h,s,75)
        outline_color =  ex.hsv_to_rgb(h,s+50,v-50)
        frame_color = [255,255,255]
        card_color = ex.hsv_to_rgb(h+10,s-25,v)
        
        if self.lang.lang == 'fr':
            lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        else:
            uc = self.lang.alphabet_uc    
            lc = self.lang.alphabet_lc
        self.abc_len = len(lc)
        h = int(math.ceil(self.abc_len/3.0))

        #data = [17,10]
        data = [16,h]
        #stretch width to fit the screen size
        x_count = self.get_x_count(data[1],even=True)
        if x_count < 16:
            data[0] = 16
        else:
            data[0] = x_count
            
        self.data = data
        
        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)
        #self.prev_item = None
        self.base26 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']        
        self.font_size = 17
        #if self.lang.lang in ['en_gb', 'en_us']:
        self.word_list = self.lang.d['abc_flashcards_word_sequence']# = ['Apple', 'Butterfly', 'Cat', 'Dolphin', 'Elephant', 'Fortepiano', 'Guitar', 'Hedgehog', 'Igloo', 'Jar', 'Koala', 'Lion', 'Monitor', 'Notebook', 'Ocean', 'Parrot', 'Queen', 'Rabbit', 'Street', 'Tomato', 'Umbrella', 'Violin', 'Watermelon', 'Xylophone', 'Yarn', 'Zebra']            
        frame_flow = self.lang.d['abc_flashcards_frame_sequence']# = [42, 27, 2, 59, 4, 34, 28, 29, 8, 9, 72, 11, 40, 13, 52, 15, 16, 17, 53, 33, 20, 21, 26, 23, 24, 25]            
        """
        elif self.lang.lang == 'pl':
            self.word_list = ['Arbuz', 'Pociąg','Buty', 'Cymbałki','Ćma', 'Dom', 'Ekran', 'Ciężarówka','Fortepian', 'Gitara', 'Hamak','Iglo', 'Jabłko', 'Kwiatki', 'Lew', 'Łódka', 'Mrówka', 'Noc','Koń', 'Okno','Królik', 'Pomidor', 'Ryba', 'Sowa', 'Ślimak','Tygrys','Ulica', 'Winogron','Mysz', 'Zebra', 'Źrebak','Żyrafa']
            frame_flow = [26, 63, 60, 23, 44, 7, 40, 50, 34, 28, 56, 8, 42, 36, 11,  1, 0, 54, 45, 22, 17, 33, 5, 14, 61, 65,53, 6, 12, 25, 62,30]            
        elif self.lang.lang == 'ru':
            self.word_list = ['Арбуз', 'Бабочка', 'Виноград', 'Гитара','Дом','Еж', 'Ёлка', 'Жираф', 'Зебра',  'Иглу', 'Йога', 'Кошка','Лодка', 'Муравей', 'Нить', 'Окно', 'Попугай', 'Рыба', 'Сова', 'Томат','Утка','Фортепиано', 'Хлеб', 'Цветы', 'Чайник', 'Шимпанзе', 'Щука', 'Съёмка', 'Мышь', 'Нить', 'Экран', 'Юбка', 'Яблоко']
            frame_flow = [26, 27, 6, 28, 7, 29, 31, 30, 25, 8, 32, 43, 1, 0, 24, 22,  15, 5, 14, 33, 3, 34, 35, 36, 19, 37, 38, 39, 12, 24, 40, 41, 42]            
        elif self.lang.lang == "es":
            self.word_list = ['Abeto', 'Búho', 'Casa', 'Dormir','Elefante', 'Fortepiano', 'Gato','Hormiga', 'Iglú', 'Jirafa', 'Koala', 'Loro', 'Manzana', 'Narciso','Ñu','Océano','Pescado', 'Queso','Ratón', 'Sol', 'Tomate', 'Uvas', 'Violín','Wagon', 'Xilófono', 'Yoga','Zapatos']
            frame_flow = [31, 14, 7, 49,4,34, 2,0, 8, 30, 72,15, 42, 69, 70,52,5, 57,12,18, 33,6, 22, 58,23,32,60]       

        elif self.lang.lang == "pt":
            self.word_list = ['Abeto', 'Barco', 'Casa', 'Dormir','Elefante', 'Formiga', 'Girafa', 'Hipopótamo','Iglu', 'Janela','Koala', 'Leão', 'Maçã', 'Narciso-amarelo', 'Ouriço', 'Peixe', 'Queijo', 'Rainha', 'Sol', 'Tomate', 'Uvas', 'Violino', 'Windsurf', 'Xilofone', 'Y', 'Zebra']
            frame_flow = [31,1,7, 49,4,0,30, 47,8,22, 72,11,42, 69,29,5, 57,16,18,33,6,21, 66,23, 43,25]
        elif self.lang.lang == "fr":
            self.word_list = ['Arbre','Bateau', 'Canard','Dormir', 'Éléphant', 'Fleurs', 'Girafe', 'Hibou', 'Iglou', 'Jonquille','Koala','Lion', 'Maison', 'Nuitée','Océan','Pomme', 'Quille', 'Raisin', 'Soleil', 'Tomate', 'Univers', 'Violon', 'Wagon', 'Xylophone', 'Yoga', 'Zèbre']
            frame_flow = [31,1,3, 49,4,36,30,14,8, 69,72,11,7, 54,52,42, 64,6,18,33, 55,21, 58,23,32,25]
        elif self.lang.lang == "it":
            self.word_list = ['Anguria', 'Barca', 'Casa', 'Dormire', 'Elefante', 'Fiori', 'Giraffa', 'Hockey','Iglù', 'Koala','Leone', 'Mela', 'Narciso','Ombrello', 'Pomodoro', 'Quaderno', 'Riccio','Sole', 'Teiera', 'Uva', 'Violino', 'Xilofono', 'Yoga', 'Zebra']
            frame_flow = [26,1,7, 49,4,36,30, 68,8, 72,11,42, 69,20,33, 13,29,18,19,6,21,23,32,25]
        elif self.lang.lang == "de":
            self.word_list = ['Apfel', 'Hängematte', 'Blumen', 'C', 'Ducken', 'Eule', 'Fisch',  'Giraffe', 'Haus','Iglu', 'Joghurt', 'Kaninchen', 'Löwe', 'Maus', 'Notizbuch', 'Ozean', 'Königin', 'Papagei', 'Q', 'Regenschirm','Sonne', 'Straße', 'Tomate', 'Umgehen', 'Schlüssel','Violine', 'Wassermelone', 'Xylophon', 'Yoga', 'Zebra']
            frame_flow = [42, 56,36, 43,3,14,5,30,7,8, 73,17,11,12,13, 52,16,15, 43,20,18, 53,33,41,10,21,26,23,32,25]
        elif self.lang.lang == "fi":
            self.word_list = [ 'Aurinko','Banaani', 'C', 'Delfiini', 'Elefantti', 'Fortepiano', 'Gnuu','Hiiri', 'Ikkuna', 'Jooga', 'Kirahvi','Leipä', 'Muurahainen', 'Näppäin', 'Omena', 'Papukaija', 'Q', 'Riippumatto', 'Seepra', 'Talo', 'Uuni', 'Vene','Xylofoni', 'Yö', 'Z', 'Å', 'Näyttö', 'Pöllö']
            frame_flow = [18, 71,43, 59,4,34, 70,12,22,32,30,35,0,10,42,15, 43,56,25,7, 67,1, 23,54, 43,43,40,14]
        elif self.lang.lang == "gr":
            self.word_list = ['Άλογο', 'Βάρκα', 'Γάτα', 'Δέντρο', 'Ελέφαντας', 'Ζέβρα', 'Ήλιος', 'Θάμνος', 'Ιπποπόταμος', 'Καμηλοπάρδαλη', 'Λουλούδια', 'Μήλο', 'Ντομάτα', 'Ξυλόφωνο', 'Ομπρέλα', 'Πάπια', 'Ρούχα', 'Σπίτι', 'Τσαγιέρα', 'Ύπνος', 'Φορτηγό', 'Χιμπατζής', 'Ψάρι', 'Ώρα']
            frame_flow = [45,1,2,31,4,25,18,46,47,30,36,42,33,23,20,3,48,7,19,49,50,37,5,51]
            self.font_size = 16
        """
        if self.lang.lang == "gr":
            self.font_size = 16

        x = 0
        x2 = 0 #(data[0] - (33 - data[0]-data[0]))//2
        y = 0
        
        for i in range(self.abc_len):
            self.board.add_unit(x,y,2,1,classes.board.Letter,uc[i]+lc[i],self.letter_color,"",3)
            self.board.ships[i].readable = False
            self.board.ships[i].set_outline(outline_color,1)
            y += 1
            if y >= data[1]:
                if i > 2*data[1]-2:
                    x = 4
                    y = 0 #data[1]-1
                else:
                    x = 2
                    y = 0 #data[1]-2

        x=(data[0]-4+3+3)//2
        y=1
        
        #Card
        self.board.add_unit(x-2,y+1,2,1,classes.board.Label,uc[0],card_color,"",0)
        self.board.add_unit(x+4,y+1,2,1,classes.board.Label,lc[0],card_color,"",0)
        self.board.add_unit(x-2,y+2,2,2,classes.board.Label,uc[0],card_color,"",self.font_size)
        self.board.add_unit(x+4,y+2,2,2,classes.board.Label,lc[0],card_color,"",self.font_size)

        #frame size 288 x 216        
        self.board.add_unit(x,y+1,4,3,classes.board.MultiImgSprite,self.word_list[0],card_color,"flashcard_images.jpg",row_data=[10,8])
        self.board.add_unit(x-2,y,8,1,classes.board.Letter,self.word_list[0],card_color,"",2)
        self.board.add_unit(x-2,y+4,8,2,classes.board.Letter,self.word_list[0],card_color,"",self.font_size)
        
        self.board.add_door(x-2,y,8,6,classes.board.Door,"",card_color,"")
        self.board.units[4].door_outline = True
        self.board.all_sprites_list.move_to_front(self.board.units[4])
        self.slide = self.board.ships[self.abc_len]

        self.slide.build_frame_flow(self.abc_len,frame_flow)
        self.slide.correction = True
        self.slide.correction_factor = 2.5
        self.slide.perm_outline = True
        self.slide.set_frame(0)
        for each in self.board.ships:
            each.immobilize()
            each.font_color = font_color
        for each in self.board.units:
            each.font_color = font_color
        
        self.active_item = self.board.ships[0]
        self.active_item.color = (255,255,255)
        self.prev_item = self.active_item
            
    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active_item = self.board.ships[self.board.active_ship]
            if self.active_item.unit_id < self.abc_len:
                if self.prev_item != None:
                    self.prev_item.color = self.letter_color
                    self.prev_item.update_me = True
                self.active_item.color = (255,255,255)
                self.create_card(self.active_item)
                self.prev_item = self.active_item
                self.mainloop.redraw_needed[0] = True

    def create_card(self, active):

        val = ex.unival(active.value)
        
        if sys.version_info < (3, 0):
            self.say(val[0].encode("utf-8"))
        else:
            self.say(val[0])
        self.board.units[0].value = val[0]
        self.board.units[1].value = val[1]
        
        self.board.units[2].value = val[0]
        self.board.units[3].value = val[1]
        display_word = True

        self.board.ships[self.abc_len+2].value = self.word_list[active.unit_id]


        self.board.ships[self.abc_len].value = self.word_list[active.unit_id]
        self.board.ships[self.abc_len+1].value = self.word_list[active.unit_id]
        self.mainloop.redraw_needed[0] = True
        self.slide.set_frame(active.unit_id)
        self.board.active_ship = -1
        
        self.slide.update_me = True
        for i in [0,1,2,3]:
            self.board.units[i].update_me = True
        for i in [self.abc_len, self.abc_len+1, self.abc_len+2]:
            self.board.ships[i].update_me = True
        
    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass