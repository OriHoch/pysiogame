import os
import pygame.mixer
sounds = pygame.mixer
sounds.init()

class SoundFX:
    def __init__(self, mainloop):
        self.mainloop = mainloop

        #sounds

        #reload game
        #self.s1 = sounds.Sound(os.path.join('res', 'sounds', '140506__blackstalian__click-sfx4b.ogg'))
        self.s1 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select06_rev.ogg'))

        #showing dialog
        #self.s2 = sounds.Sound(os.path.join('res', 'sounds', '162465__kastenfrosch__lostitem.ogg'))
        self.s2 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_whistle02_rstartx.ogg'))

        #category selected
        #self.s3 = sounds.Sound(os.path.join('res', 'sounds', '140508__blackstalian__click-sfx2.ogg'))
        self.s3 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select02.ogg'))

        #game selected
        #self.s4 = sounds.Sound(os.path.join('res', 'sounds', '140509__blackstalian__click-sfx1.ogg'))
        self.s4 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select01.ogg'))

        #category group open
        #self.s5 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_slide3.ogg'))
        self.s5 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select03_rev.ogg'))

        #close group close
        #self.s6 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_slide3_rev.ogg'))
        self.s6 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select03.ogg'))

        #increase level
        #self.s7 = sounds.Sound(os.path.join('res', 'sounds', '140511__blackstalian__click-sfx7.ogg'))
        self.s7 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select04.ogg'))


        #decrease level
        #self.s9 = sounds.Sound(os.path.join('res', 'sounds', '140511__blackstalian__click-sfx7.ogg'))
        self.s9 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_select05.ogg'))

        #game failed
        self.s8 = sounds.Sound(os.path.join('res', 'sounds', '146731__fins__game-fail.ogg'))

        #object motion
        #self.s10 = sounds.Sound(os.path.join('res', 'sounds', '104874__robinhood76__02020-cartoon-slide_1.ogg'))
        self.s10 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_slide05.ogg'))

        #object unable to move
        #self.s11 = sounds.Sound(os.path.join('res', 'sounds', '104874__robinhood76__02020-cartoon-slide_2.ogg'))
        self.s11 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_noise01.ogg'))

        #hit the mole - deactivated
        self.s12 = sounds.Sound(os.path.join('res', 'sounds', '188043__antumdeluge__mouse.ogg'))

        #level completed
        self.s13 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_whistle03.ogg'))

        #game completed
        self.s14 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_whistle04.ogg'))


        #keyboard press
        self.s15 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_press01.ogg'))

        #keyboard wrong btn
        self.s16 = sounds.Sound(os.path.join('res', 'sounds', 'sfx_press02_rev.ogg'))

    def play(self, sound_id):
        if self.mainloop.config.settings["sounds"]:
            eval("self.s%i.play()" % sound_id)
