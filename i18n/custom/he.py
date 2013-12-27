# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

import sys
from classes.extras import reverse

d = dict()

#alphabet he
alphabet_lc = ['א', 'ב', 'ג', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['א', 'ב', 'ג', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
alpha = "אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ׳״"

def r(s):
    return reverse(s,alpha)
    
numbers = ['אחד', 'שתיים', 'שלוש', 'ארבע', 'חמש', 'שש', 'שבע', 'שמונה', 'תשע', 'עשר', 'אחד עשרה', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
numbers2090 = ['עשרים','שלושים','ארבעים','fifty','sixty','seventy','eighty','ninety']


#The following 2 lines are not to be translated but replaced with a sequence of words starting in each of the letters of your alphabet in order, best if these words have a corresponding picture in images/flashcard_images.jpg. The second line has the number of the image that the word describes. 
#The images are numbered from left to bottom such that the top left is numbered 0, the last image is 73, if none of the available things have names that start with any of the letters we can add new pictures.
#d['abc_flashcards_word_sequence'] = ['אבטיח', 'בננה', 'גיטרה', 'Dolphin', 'Elephant', 'Fortepiano', 'Guitar', 'Hedgehog', 'Igloo', 'Jar', 'Koala', 'Lion', 'Monitor', 'Notebook', 'Ocean', 'Parrot', 'Queen', 'Rabbit', 'Street', 'Tomato', 'Umbrella', 'Violin', 'Watermelon', 'Xylophone', 'Yarn', 'Zebra']
d['abc_flashcards_word_sequence'] = [r("אבטיח"), r("בננה"), r("גיטרה"), 'Dolphin', 'Elephant', 'Fortepiano', 'Guitar', 'Hedgehog', 'Igloo', 'Jar', 'Koala', 'Lion', 'Monitor', 'Notebook', 'Ocean', 'Parrot', 'Queen', 'Rabbit', 'Street', 'Tomato', 'Umbrella', 'Violin', 'Watermelon', 'Xylophone', 'Yarn', 'Zebra']
d['abc_flashcards_frame_sequence'] = [26, 71, 28, 59, 4, 34, 28, 29, 8, 9, 72, 11, 40, 13, 52, 15, 16, 17, 53, 33, 20, 21, 26, 23, 24, 25]  


letter_names = []

accents_lc = ['-']
accents_uc = []

def n2txt(n, twoliner = False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return r(numbers[n-1])
    elif 30 <= n < 100:
        m = n % 10
        tens = r(numbers2090[(n//10)-2])
        if m == 0:
            return r(tens)
        elif m > 0:
            ones = r(numbers[m-1])
            if twoliner:
                return [tens, ones]
            else:
                return ones + " " + tens
    
    elif n == 0: return r("אפס")
    elif n == 100: return r("one hundred")
    else: return ""

     
def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if sys.version_info < (3, 0):
        if m == 0: return u"%s" % n2txt(h)
        elif m == 1: return r(u" דקה אחרי") + n2txt(h)
        elif m == 15: return r(u" רבע אחרי") + n2txt(h)
        elif m == 30: return r(u"half past ") + n2txt(h)
        elif m == 45: return r(u"quater to ") + n2txt(h)
        elif m == 59: return r(u"one minute to ") + n2txt(h)
        elif m < 30: return n2txt(m) + r(u" past ") +n2txt(h)
        elif m > 30: return n2txt(60-m) + r(u" to ") +n2txt(h)
        return ""
    else:
        if m == 0: return "%s" % n2txt(h)
        elif m == 1: return "דקה אחרי %s" % n2txt(h)
        elif m == 15: return "רבע אחרי %s" % n2txt(h)
        elif m == 30: return "half past %s" % n2txt(h)
        elif m == 45: return "quater to %s" % n2txt(h)
        elif m == 59: return "one minute to %s" % n2txt(h)
        elif m < 30: return "%s past %s" % (n2txt(m), n2txt(h))
        elif m > 30: return "%s to %s" % (n2txt(60-m), n2txt(h))
        return ""
        
"""
def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
        
    if m == 0: r = u"%s" % n2txt(h)
    elif m == 1: r = u"דקה אחרי " % n2txt(h)
    elif m == 15: r = u"רבע אחרי %s" % n2txt(h)
    elif m == 30: r = u"half past %s" % n2txt(h)
    elif m == 45: r = u"quater to %s" % n2txt(h)
    elif m == 59: r = u"one minute to %s" % n2txt(h)
    elif m < 30: r =  u"%s past %s" % (n2txt(m), n2txt(h))
    elif m > 30: r = u"%s to %s" % (n2txt(60-m), n2txt(h))
    else: r = ""
    
    if sys.version_info < (3, 0):
        if not isinstance(r, unicode):
            #r = unicode(r, "utf-8")
            r = r.decode("utf-8")
    return r
"""    
