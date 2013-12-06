# -*- coding: utf-8 -*-

# traduzido para português da europa por Américo Monteiro (a_monteiro@gmx.com)

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

d = dict()

numbers = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte', 'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco', 'vinte e seis', 'vinte e sete', 'vinte e oito', 'vinte e nove']
numbers2090 = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
 
d['abc_flashcards_word_sequence'] = ['Abeto', 'Barco', 'Casa', 'Dormir','Elefante', 'Formiga', 'Girafa', 'Hipopótamo','Iglu', 'Janela','Koala', 'Leão', 'Maçã', 'Narciso-amarelo', 'Ouriço', 'Peixe', 'Queijo', 'Rainha', 'Sol', 'Tomate', 'Uvas', 'Violino', 'Windsurf', 'Xilofone', 'Y', 'Zebra']
d['abc_flashcards_frame_sequence'] = [31,1,7, 49,4,0,30, 47,8,22, 72,11,42, 69,29,5, 57,16,18,33,6,21, 66,23, 43,25]

#alphabet - pt - "abcdefghijlmnopqrstuvxz"
alphabet_lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['á','â','ã','à','ç','é','ê','í','ó','ô','õ','ú','-']
accents_uc = ['Á','Â','Ã','À','Ç','É','Ê','Í','Ó','Ô','Õ','Ú']

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
                return [tens + " e ", ones]
            else:
                return tens + " e " + ones
    
    elif n == 0: return "zero"
    elif n == 100: return "cem"
    return ""

horas = ['uma hora', 'duas horas', 'três horas', 'quatro horas', 'cinco horas', 'seis horas', 'sete horas', 'oito horas', 'nove horas', 'dez horas', 'onze horas', 'doze horas']

def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if m == 0: return "%s em ponto" % horas[h-1]
    elif m == 1: return "%s e um minuto" % horas[h-1]
    elif m == 15: return "%s e um quarto" % horas[h-1]
    elif m == 30: return "%s e meia" % horas[h-1]
    elif m == 45: return "um quarto para %s" % horas[h-1]
    elif m == 59: return "um minuto para %s" % horas[h-1]
    elif m < 30: return "%s e %s minutos" % (horas[h-1], n2txt(m))
    elif m > 30: return "%s minutos para %s" % (n2txt(60-m), horas[h-1])
    return ""