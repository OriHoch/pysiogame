# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

#when translating the "d" dictionary please translate the values
#and leave keys as they are (the keys are sometimes shortened to save on space)

d = dict()

numbers = ['eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf' , 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn', 'zwanzig', 'eins und zwanzig', 'zweieins und zwanzig', 'dreieins und zwanzig', 'viereins und zwanzig', 'fünfeins und zwanzig', 'sechseins und zwanzig', 'siebeneins und zwanzig', 'achteins und zwanzig', 'neuneins und zwanzig']
numbers2090 = ['zwanzig','dreißig','vierzig','fünfzig','sechzig','siebzig','achtzig','neunzig']

 
d['abc_flashcards_word_sequence'] = ['Apfel', 'Hängematte', 'Blumen', 'C', 'Ducken', 'Eule', 'Fisch',  'Giraffe', 'Haus','Iglu', 'Joghurt', 'Kaninchen', 'Löwe', 'Maus', 'Notizbuch', 'Ozean', 'Königin', 'Papagei', 'Q', 'Regenschirm','Sonne', 'Straße', 'Tomate', 'Umgehen', 'Schlüssel','Violine', 'Wassermelone', 'Xylophon', 'Yoga', 'Zebra']
d['abc_flashcards_frame_sequence'] = [42, 56,36, 43,3,14,5,30,7,8, 73,17,11,12,13, 52,16,15, 43,20,18, 53,33,41,10,21,26,23,32,25]

#alphabet - de
alphabet_lc = ['a', 'ä', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ß', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'Ä', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'ß', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []
accents_lc = ['-']
accents_uc = []

def n2txt(n, twoliner = False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
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
                return [ones + " und ", tens]
            else:
                return ones + " und " + tens
    
    elif n == 0: return "null"
    elif n == 100: return "einhundert"
    return ""
    
    
def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if m == 0: return "%s o'clock" % n2txt(h)
    elif m == 1: return "one minute past %s" % n2txt(h)
    elif m == 15: return "quater past %s" % n2txt(h)
    elif m == 30: return "half past %s" % n2txt(h)
    elif m == 45: return "quater to %s" % n2txt(h)
    elif m == 59: return "one minute to %s" % n2txt(h)
    elif m < 30: return "%s past %s" % (n2txt(m), n2txt(h))
    elif m > 30: return "%s to %s" % (n2txt(60-m), n2txt(h))
    return ""
     
           