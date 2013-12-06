# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

d = dict()

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
numbers2090 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

d['abc_flashcards_word_sequence'] = ['Arbre','Bateau', 'Canard','Dormir', 'Éléphant', 'Fleurs', 'Girafe', 'Hibou', 'Iglou', 'Jonquille','Koala','Lion', 'Maison', 'Nuitée','Océan','Pomme', 'Quille', 'Raisin', 'Soleil', 'Tomate', 'Univers', 'Violon', 'Wagon', 'Xylophone', 'Yoga', 'Zèbre']
d['abc_flashcards_frame_sequence'] = [31,1,3, 49,4,36,30,14,8, 69,72,11,7, 54,52,42, 64,6,18,33, 55,21, 58,23,32,25]

#alphabet - fr - "aàâæbcçdeéèêëfghiîïjklmnoôœpqrstuùûüvwxyÿz"
alphabet_lc = ['a', 'à', 'â', 'æ', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'œ', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'ÿ', 'z']
alphabet_uc = ['A', 'À', 'Â', 'Æ', 'B', 'C', 'Ç', 'D', 'E', 'É', 'È', 'Ê', 'Ë', 'F', 'G', 'H', 'I', 'Î', 'Ï', 'J', 'K', 'L', 'M', 'N', 'O', 'Ô', 'Œ', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ù', 'Û', 'Ü', 'V', 'W', 'X', 'Y', 'Ÿ', 'Z']
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
                return [tens, ones]
            else:
                return tens + " " + ones
    
    elif n == 0: return "zero"
    elif n == 100: return "one hundred"
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
     