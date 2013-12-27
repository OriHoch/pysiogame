# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

d = dict()
#word lists

numbers = ['yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän', 'kymmenen', 'yksitoista', 'kaksitoista', 'kolmetoista', 'neljätoista', 'viisitoista', 'kuusitoista', 'seitsemäntoista', 'kahdeksantoista', 'yhdeksäntoista', 'kaksikymmentä', 'kaksikymmentäyksi', 'kaksikymmentäkaksi', 'kaksikymmentäkolme', 'kaksikymmentäneljä', 'kaksikymmentäviisi', 'kaksikymmentäkuusi', 'kaksikymmentäseitsemän', 'kaksikymmentäkahdeksan', 'kaksikymmentäyhdeksän']
numbers2090 = ['kaksikymmentä','kolmekymmentä','neljäkymmentä','viiskymmentä','kuusikymmentä','seitsemänkymmentä','kahdeksankymmentä','yhdeksänkymmentä']


#The following 2 lines are not to be translated but replaced with a sequence of words starting in each of the letters of your alphabet in order, best if these words have a corresponding picture in images/flashcard_images.jpg. The second line has the number of the image that the word describes.          
#The images are numbered from left to bottom such that the top left is numbered 0, the last image is 73, if none of the available things have names that start with any of the letters we can add new pictures.
d['abc_flashcards_word_sequence'] = [ 'Avain','Banaani', 'Cheddar', 'Delfiini', 'Elefantti', 'Flyygeli', 'Gnuu','Hiiri', 'Ikkuna', 'Jooga', 'Kirahvi','Leipä', 'Muurahainen', 'Näyttö', 'Omena', 'Papukaija', 'Q', 'Riippumatto', 'Seepra', 'Talo', 'Uuni', 'Vene', 'Watti', 'Xylofoni', 'Yö', 'Z', 'Å', 'Ämpäri', 'Öinen']
d['abc_flashcards_frame_sequence'] = [10, 71,57, 59,4,34, 70,12,22,32,30,35,0,40,42,15, 43,56,25,7, 67,1, 18, 23,54, 43,43,73,54]

#alphabet en
alphabet_lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
alphabet_uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

#letters that may exist in words but are not part of the officail alphabet
accents_lc = ['š','ž','-']
accents_uc = ['Š','Ž']

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
                return [tens+"-", ones]
            else:
                return tens + ones
    
    elif n == 0: return "nolla"
    elif n == 100: return "sata"
    return ""
    
def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if m == 0: return "tasan %s" % n2txt(h)
    elif m == 1: return "minuutin yli %s" % n2txt(h)
    elif m == 15: return "vartin yli %s" % n2txt(h)
    elif m == 30: return "puoli %s" % n2txt(h+1)
    elif m == 45: return "varttia vaille %s" % n2txt(h)
    elif m == 59: return "minuutin vaille %s" % n2txt(h)
    elif m < 30: return "%s yli %s" % (n2txt(m), n2txt(h))
    elif m > 30: return "%s vaille %s" % (n2txt(60-m), n2txt(h))
    return ""
     
