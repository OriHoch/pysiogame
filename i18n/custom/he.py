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
alphabet_lc = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ך', 'ל', 'מ', 'ם', 'נ', 'ן', 'ס', 'ע', 'פ', 'ף', 'צ', 'ץ', 'ק', 'ר', 'ש', 'ת']
alphabet_uc = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ך', 'ל', 'מ', 'ם', 'נ', 'ן', 'ס', 'ע', 'פ', 'ף', 'צ', 'ץ', 'ק', 'ר', 'ש', 'ת']

#correction of eSpeak pronounciation of single letters if needed
#the following is an example how I'd replace pronunciation of single letters in abc games. 
#Please correct the following letter names - I got them wrong
letter_names = ['alef', 'beth', 'gimel', 'daleth', 'he', 'vav', 'zayin', 'heth', 'teth', 'yodh', 'kaph', 'lamed', 'mem', 'nun', 'samekh', 'ayin', 'pe', 'tsadi', 'qoph', 'resh', 'shin', 'sin', 'tav'] 

alpha = "אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ׳״"

def r(s):
    return reverse(s,alpha)
    
numbers = ['אחד', 'שתיים', 'שלוש', 'ארבע', 'חמש', 'שש', 'שבע', 'שמונה', 'תשע', 'עשר', 'אחד עשרה', 'שתים עשרה', 'שלוש-עשרה', 'ארבע-עשרה', 'חמש-עשרה', 'שש-עשרה', 'שבע-עשרה', 'שמונה-עשרה', 'תשע-עשרה', 'עשרים', 'עשרים ואחת', 'עשרים ושתים', 'עשרים ושלוש', 'עשרים וארבע', 'עשרים וחמש', 'עשרים ושש', 'עשרים ושבע', 'עשרים ושמונה', 'עשרים ותשע']
numbers2090 = ['עשרים','שלושים','ארבעים','חמישים','שישים','שבעים','שמונים','תשעים']


#The following 2 lines are not to be translated but replaced with a sequence of words starting in each of the letters of your alphabet in order, best if these words have a corresponding picture in images/flashcard_images.jpg. The second line has the number of the image that the word describes. 
#The images are numbered from left to bottom such that the top left is numbered 0, the last image is 73, if none of the available things have names that start with any of the letters we can add new pictures.
#d['abc_flashcards_word_sequence'] = ['אבטיח', 'בננה', 'גיטרה', 'Dolphin', 'Elephant', 'Fortepiano', 'Guitar', 'Hedgehog', 'Igloo', 'Jar', 'Koala', 'Lion', 'Monitor', 'Notebook', 'Ocean', 'Parrot', 'Queen', 'Rabbit', 'Street', 'Tomato', 'Umbrella', 'Violin', 'Watermelon', 'Xylophone', 'Yarn', 'Zebra']
d['abc_flashcards_word_sequence'] = [r("אבטיח"), r("בננה"), r("גיטרה"), r("דולפין"), r("היפופוטם"), r("ורד"), r("זברה"), r("חלזון"), r("טלפון"), r("ינשוף"), r("כינור"), r("מערוך"), r("לחם"), r("מסך"), r("מים"), r("נעליים"), r("שעון"), r("סירה"), r("עין"), r("פרח"), r("חוף"), r("צליל"), r("מיץ"), r("קוף"), r("רכבת"), r("שעון"), r("תפוח")]
d['abc_flashcards_frame_sequence'] = [26, 71, 28, 59, 47, 78, 25, 61, 79, 14, 21, 80, 35, 40, 81, 60, 51, 1, 75, 69, 82, 83, 84, 37, 63, 51, 42]


#letter_names = []

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
    elif n == 100: return r("מאה")
    else: return ""

#phonetic transcription - number to spoken number 
#TODO - implement the use of the following function
#numbers in left to right order in phonetic transcription
numbersp = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
numbers2090p = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def n2spk(n, twoliner = False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbersp[n-1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090p[(n//10)-2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbersp[m-1]
            if twoliner:
                return [tens, ones]
            else:
                return tens + " " + ones
    
    elif n == 0: return "one"
    elif n == 100: return "one hundred"
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
        elif m == 30: return r(u"חצי אחרי ") + n2txt(h)
        elif m == 45: return r(u"רבע ל ") + n2txt(h)
        elif m == 59: return r(u"דקה ל ") + n2txt(h)
        elif m < 30: return n2txt(m) + r(u" אחרי ") +n2txt(h)
        elif m > 30: return n2txt(60-m) + r(u" ל ") +n2txt(h)
        return ""
    else:
        if m == 0: return "%s" % n2txt(h)
        elif m == 1: return r(" דקה אחרי") + n2txt(h)
        elif m == 15: return r(" רבע אחרי") + n2txt(h)
        elif m == 30: return r("חצי אחרי ") + n2txt(h)
        elif m == 45: return r("רבע ל ") + n2txt(h)
        elif m == 59: return r("דקה ל ") + n2txt(h)
        elif m < 30: return n2txt(m) + r(" אחרי ") +n2txt(h)
        elif m > 30: return n2txt(60-m) + r(" ל ") +n2txt(h)
        return ""
        
def time2spk(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    'but this time in Latin letters for espeak so it can to read it phonetically'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if sys.version_info < (3, 0):
        if m == 0: return u"%s" % n2spk(h)
        elif m == 1: return u" דקה אחרי" + n2spk(h)
        elif m == 15: return u" רבע אחרי" + n2spk(h)
        elif m == 30: return u"חצי אחרי " + n2spk(h)
        elif m == 45: return u"רבע ל " + n2spk(h)
        elif m == 59: return u"דקה ל " + n2spk(h)
        elif m < 30: return n2spk(m) + u" אחרי " +n2spk(h)
        elif m > 30: return n2spk(60-m) + u" ל " +n2spk(h)
        return ""
    else:
        if m == 0: return "%s" % n2spk(h)
        elif m == 1: return " דקה אחרי" + n2spk(h)
        elif m == 15: return " רבע אחרי" + n2spk(h)
        elif m == 30: return "חצי אחרי " + n2spk(h)
        elif m == 45: return "רבע ל " + n2spk(h)
        elif m == 59: return "דקה ל " + n2spk(h)
        elif m < 30: return n2spk(m) + " אחרי " +n2spk(h)
        elif m > 30: return n2spk(60-m) + " ל " +n2spk(h)
        return ""

#dictionary used to override the text that's being passed to tts engine
dp = dict()

dp["Hebrew"] = "Hebrew"
dp['shape_names'] = ["Equilateral Triangle", "Isosceles Triangle", "Obtuse Triangle", "Right Triangle", "Acute Triangle", "Square", "Rectangle", "Right Trapezium", "Isosceles Trapezium", "Rhombus", "Parallelogram", "Pentagon", "Hexagon", "Circle", "Ellipse"]
dp['solid_names'] = ["Cube", "Square Prism", "Triangular Prism", "Square Pyramid", "Triangular Pyramid", "Sphere", "Cylinder", "Cone", "Torus"]
dp['abc_flashcards_word_sequence'] = [r("אבטיח"), r("בננה"), r("גיטרה"), r("דולפין"), r("היפופוטם"), r("ורד"), r("זברה"), r("חלזון"), r("טלפון"), r("ינשוף"), r("כינור"), r("מערוך"), r("לחם"), r("מסך"), r("מים"), r("נעליים"), r("שעון"), r("סירה"), r("עין"), r("פרח"), r("חוף"), r("צליל"), r("מיץ"), r("קוף"), r("רכבת"), r("שעון"), r("תפוח")]

#game start
dp["Hello"] = "Hello"
dp["Welcome back."] = "Welcome back in the game."
dp["fruit"] = ["green apple", "red apple", "strawberry", "pear", "orange", "onion", "tomato", "lemon", "cherry", "pepper", "carrot", "banana", "watermelon"]    

dp["Drag the slider"] = "Drag the slider up or down so that the right sign is in the red square."
dp["Check the shopping list"] = "Check the shopping list and drag all needed items into the basket."
dp["Drag lt2"] = "Drag one of the lesser, greater or equal to the red square."
dp["Re-arrange right"] = "Re-arrange the above numbers so they are in the right order"
dp["Complete abc"] = "Complete the abc using the letters above."
dp["Write a word:"] = "Write a word:"
dp["Find and separate"] = "Find and separate the Even Numbers form the Odd Numbers in the above series."
dp["Re-arrange alphabetical"] = "Re-arrange the above letters so they are in the alphabetical order."
dp["Re-arrange ascending"] = "Re-arrange the above numbers so they are in the ascending order."

dp["Perfect! Task solved!"] = "Perfect! Task solved!"
dp["work harder"] = "You need to work a little bit harder next time."

dp["Game Over!"] = "Game Over!"
dp["Congratulations! Game Completed."] = "Congratulations! You have completed all tasks in this game."
dp["Great job!"] = ["Great job!","Perfect!","Awesome!","Fantastic job!","Well done!"]
dp["Perfect! Level completed!"] = "Perfect! Level completed!"
dp["Perfect!"] = "Perfect" #Perfect!

dp["area:"] = "area:"
dp["perimeter:"] = "perimeter:"
dp["circumference:"] = "circumference"
dp["surface area:"] = "surface area:"
dp["volume:"] = "volume:"
dp["divided by"] = "divided by"
dp["multiplied by"] = "times"
dp["equals"] = "equals"
dp["Even"] = "Even"
dp["Odd"] = "Odd"

dp["white"]="white"
dp["black"]="black"
dp["grey"]="grey"
dp["red"]="red"
dp["orange"]="orange"
dp["yellow"]="yellow"
dp["olive"]="olive"
dp["green"]="green"
dp["sea green"]="sea green"
dp["teal"]="teal"
dp["blue"]="blue"
dp["navy"]="navy"
dp["purple"]="purple"
dp["violet"]="violet"
dp["magenta"]="magenta"
dp["indigo"]="indigo"
dp["pink"]="pink"
dp["maroon"] = "maroon"
dp["brown"] = "brown"
dp["aqua"] = "aqua"
dp["lime"] = "lime"

dp["more red"] = "more red"
dp["more green"] = "more green"
dp["more blue"] = "more blue"
dp["more cyan"] = "more cyan"
dp["more magenta"] = "more magenta"
dp["more yellow"] = "more yellow"

dp["less red"] = "less red"
dp["less green"] = "less green"
dp["less blue"] = "less blue"
dp["less cyan"] = "less cyan"
dp["less magenta"] = "less magenta"
dp["less yellow"] = "less yellow"

dp["red is ok"] = "red is ok"
dp["green is ok"] = "green is ok"
dp["blue is ok"] = "blue is ok"
dp["cyan is ok"] = "cyan is ok"
dp["magenta is ok"] = "magenta is ok"
dp["yellow is ok"] = "yellow is ok"

dp["Fract instr0"] = "Match fraction charts on the right to the ones on the left"
dp["Fract instr1"] = "Match fraction charts and fractions on the right to the fraction charts on the left"
dp["Fract instr2"] = "Match fraction charts to the fractions on the left"
dp["Fract instr3"] = "Match fraction charts, fractions and decimal fractions on the right to their percentage representations"
dp["Fract instr4"] = "Match charts to the ratios on the left. Ratios are expressed as ratio of coloured pieces to white pieces"
