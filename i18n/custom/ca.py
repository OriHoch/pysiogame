# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game,
#I will be grateful if you could share it with the community -
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible).
#The color names in other languages than English are already in smaller font.


d = dict()

numbers = ['u', 'dos', 'tres', 'quatre', 'cinc', 'sis', 'set', 'vuit', 'nou', 'deu', 'onze', 'dotze', 'tretze', 'catorze', 'quinze', 'setze', 'disset', 'divuit', 'dinou', 'vint', 'vint-i-u', 'vint-i-dos', 'vint-i-tres', 'vint-i-quatre', 'vint-i-cinc', 'vint-i-sis', 'vint-i-set', 'vint-i-vuit', 'vint-i-nou']
numbers2090 = ['vint', 'trenta', 'quaranta', 'cinquanta', 'seixanta', 'setanta', 'vuitanta', 'noranta']

#The following 2 lines are not to be translated but replaced with a sequence of words starting in each of the letters of your alphabet in order, best if these words have a corresponding picture in images/flashcard_images.jpg. The second line has the number of the image that the word describes.
#The images are numbered from left to bottom such that the top left is numbered 0, the last image is 73, if none of the available things have names that start with any of the letters we can add new pictures.
# XXX: j*, kiwi, ull missing - j* - little red wagon used for Joguina, other images added
d['abc_flashcards_word_sequence'] = ['Ànec', 'Barca', 'Coala', 'Calçat', 'Dofí', 'Elefant', 'Formiga', 'Gat', 'Hipopotam', 'Iglú', 'Joguina', 'Kiwi', 'Lleó', 'Mússol', 'Nit', 'Oceà', 'Poma', 'Quadern', 'Ratolí', 'Síndria', 'Tomàquet', 'Ull', 'Violí', 'Windsurf', 'Xilofon', 'Yoga', 'Zebra']
d['abc_flashcards_frame_sequence'] = [3, 1, 72, 60, 59, 4, 0, 2, 47, 8, 58, 74, 11, 14, 54, 52, 42, 13, 12, 26, 33, 75, 21, 66, 23, 32, 25]

#alphabet ca
alphabet_lc = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['à', 'é', 'è', 'í', 'ò', 'ó', 'ú','-']
accents_uc = ['À', 'É', 'È', 'Í', 'Ò', 'Ó', 'Ú']

def n2txt(n, twoliner = False):
    "takes a number from 0 - 100 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n-1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n//10)-2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbers[m-1]
            if twoliner:
                return [tens + "-", ones]
            else:
                return tens + "-" + ones
    
    elif n == 0: return "zero"
    elif n == 100: return "cent"
    return ""
    
hores = ['unes', 'dues', 'tres', 'quatre', 'cinc', 'sis', 'set', 'vuit', 'nou', 'deu', 'onze', 'dotze']

def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 7:
        if h == 12:
            h = 1
        else:
            h += 1
            
    if m == 0: return "les %s en punt" % hores[h-1]
    elif m == 1: return "les %s i un minut" % hores[h-1]
    elif 0 < m < 8: return "les %s i %s" % (hores[h-1], n2txt(m))

    elif 0 < m < 8: return "les %s i %s" % (hores[h-1], n2txt(m))
    elif 7 < m < 15: return "un quart menys %s de %s" % (n2txt(15 - m), hores[h-1])
    elif m == 15: return "un quart de %s" % hores[h-1]
    
    elif 15 < m < 23: return "un quart i %s de %s" % (n2txt(m - 15), hores[h-1])
    elif 22 < m < 30: return "dos quarts menys %s de %s" % (n2txt(30 - m), hores[h-1])
    elif m == 30: return "dos quarts de %s" % hores[h-1]
    
    elif 30 < m < 38: return "dos quarts i %s de %s" % (n2txt(m - 30), hores[h-1])
    elif 37 < m < 45: return "tres quarts menys %s de %s" % (n2txt(45 - m), hores[h-1])
    elif m == 45: return "tres quarts de %s" % hores[h-1]
    
    elif 45 < m < 53: return "tres quarts i %s de %s" % (n2txt(m - 45), hores[h-1])
    elif 52 < m < 59: return "les %s menys %s" % (hores[h-1], n2txt(60 - m))
    elif m == 59: return "les %s menys un minut" % hores[h-1]