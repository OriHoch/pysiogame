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

#Example in German:
# - d["Welcome back."] = "Welcome back in the game."
# + d["Welcome back."] = "Willkommen zurück im Spiel."

d=dict()

#word lists
shape_names = ["Triangolo equilatero", "Triangolo isoscele", "Triangolo ottuso", "Triangolo rettangolo", "Triangolo acuto", "Quadrato", "Rettangolo", "Trapezio rettangolo", "Trapezio isoscele", "Rombo", "Parallelogramma", "Pentagono", "Esagono", "Cerchio", "Ellisse"]

solid_names = ["Cubo", "Prisma a base quadrata", "Prisma a base triangolare", "Piramide", "Piramide a base triangolare", "Sfera", "Cilindro", "Cono", "Toro"]
numbers = ['uno', 'due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici' ,'tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti','ventuno', 'ventidue', 'ventitré', 'ventiquattro', 'venticinque', 'ventisei', 'ventisette', 'ventotto', 'ventinove' ]
#'ventuno', 'ventidue', 'ventitre', 'ventiquattro', 'venticinque', 'ventisei', 'ventisette', 'ventotto', 'ventinove'

numbers2090 = ['venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']

def n2txt(n, twoliner = False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n-1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n//10)-2]
        if m > 0:
            ones = numbers[m-1]
        else:
            ones = ""
        if m in [1,8]:
            return tens[0:-1] + ones
        elif m == 3:
            return tens + "tré"
        else:
            if twoliner:
                return [tens +"-", ones]
            else:
                return tens + ones
    else:
        return ""

d['abc_flashcards_word_sequence'] = ['Anguria', 'Barca', 'Casa', 'Dormire', 'Elefante', 'Fiori', 'Giraffa', 'Hockey','Iglù', 'Koala','Leone', 'Mela', 'Narciso','Ombrello', 'Pomodoro', 'Quaderno', 'Riccio','Sole', 'Teiera', 'Uva', 'Violino', 'Xilofono', 'Yoga', 'Zebra']
d['abc_flashcards_frame_sequence'] = [26,1,7, 49,4,36,30, 68,8, 72,11,42, 69,20,33, 13,29,18,19,6,21,23,32,25]

#used in telling time activity
#the number lists below are for languages with a bit more complex forms, ie. different suffixes depending on context - if your language is like that check Polish translation to see how to use them

d["minute_numbers_1to29"] = numbers[:]
#last digit when joining numbers of minutes

#hours case 0: full hour, ie. one o'clock, two o'clock, etc.
d["hours_a"] = ["l'una",'le due','le tre','le quattro','le cinque','le sei','le sette','le otto','le nove','le dieci','le undici','le dodici']#numbers[0:12]

#hours case 1: ie. ten past one, 22 past three, etc.
d["hours_b"] = d["hours_a"][:]

#hours case 2: ie. ten to one, 22 to three, etc.
d["hours_c"] = d["hours_a"][:]

d["time_string_one_to"] = "" #if you never use the "to the hour" form leave this blank
d["time_string_one_past"] = "%s e un minuto"

#pick either mh or hm version, or leave these 4 blank if you don't use to the hour form: mh means that number of minutes will appear first in the sentence followed by the number of hours, the hm is the opposite.
d["time_string_to_mh"] = "" #not applicable in Italian
d["time_string_past_mh"] = "" #not applicable in Italian
d["time_string_to_hm"] = "" #ie. 3:55 = four o'clock in five
d["time_string_past_hm"] = "" #ie. 4:05 = four and five minutes

#if you never use the "to the hour" form leave the above fields blank and only fill one of the following two
d["time_string_1_59_past_mh"] = "" 
d["time_string_1_59_past_hm"] = "%s e %s"
d["time_string_3q_past"] = "%s e quarantacinque" #if you don't use quarter to but rather past use this one to either say it's 3 quarters past or 45 past
d["time_string_q_to"] = ""
d["time_string_q_past"] = "%s e quindici"#un quarto

d["time_string_half_to"] = "" #not applicable in Italian
d["time_string_half_past"] = "%s e trenta"#mezzo
d["time_string_full"] = "%s in punto"

#google translated fruits - are they ok?  {was quite ok!}
fruit = ["mela verde", "mela rossa", "fragola", "pera", "arancia","cipolla", "pomodoro", "limone", "ciliegia", "pepeone", "carota","banana ","anguria"]
fruits_1 = ["mele verdi", "mele rosse", "fragole", "pere", "arance","cipolle", "pomodori", "limoni", "ciliegie", "peperoni", "carote","banane ","angurie"]
fruits_2 = []
#[[for this number of fruits (in range of 2-7) use names from fruits_1],[and for those from fruits_2]]
plural_rules = [[2,3,4,5,6,7],[]] #used for some languages where there are more than one form for plurals depending on number

#alphabet - it
alphabet_lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
alphabet_uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['à','è','é','ì','í','î','ò','ó','ù','ú','-']
accents_uc = ['À','È','É','Ì','Í','Î','Ò','Ó','Ù','Ú']

#game start
d["Hello"] = "Ciao"
d["Welcome back."] = "Bentornato nel gioco."


#settings
d["Preferences"] = "Preferenze"
d["Language"] = "Lingua"

d["Reader"] = "eSpeak"
#d["Reader"] = "Italiano"
d["Read Instructions"] = "Leggere le istruzioni all'inizio del gioco"

#menu categories
d["Info Category"] = "Informazioni e impostazioni"
d["Keyboard & Mouse"] = "Tastiera e mouse"
d["Discover Letters"] = "Scoprire le lettere"
d["Learn Words"] = "Imparare nuove parole"
d["Maths"] = "Matematica"
d["Numbers & Basic Operations"] = "Numeri e principali operazioni"
d["Basic Operations - exercises"] = "Principali operazioni - Esercizi"
d["Sorting and Comparing"] = "Ordinamento e confronto"
d["Geometry"] = "Geometria e riconoscimento della forma"
d["Art"] = "Arte e colori"
d["Memory"] = "Memoria"
d["Games & Mazes"] = "Giochi e labirinti"
d["Multiplayer"] = "Giochi per più giocatori"

#games
d["About."] = "Caratteristiche."
d["Game info..."] = "Informazioni sul gioco..."
d["Credits"] = "Diritti e riconoscimenti"
d["Hit the Mole"] = "Colpisci la talpa"
d["Letters"] = "Lettere"
d["Letter Flashcards"] = "Impara le lettere con le schede"
d["Learn to Write"] = "Impara a scrivere"
d["Trace Letters"] = "Riconosci lettere e numeri"
d["Complete the ABC"] = "Completa l'alfabeto"
d["English"] = "Inglese"
d["in your language"] = "Italiano"

d["Sorting Letters"] = "Riordina le lettere" #(could be also "Metti le lettere in ordine alfabetico")
d["Lowercase Letters"] = "Lettere minuscole"
d["Uppercase Letters"] = "Lettere maiuscole"
d["Word Builder"] = "Il costruttore di parole"
d["Word Maze"] = "Labirinto di parole"
d["Collect all"] = "Raggruppa le lettere nel giusto ordine"
d["Word Maze + 4"] = "Labirinto di parole +4"
d["Numbers"] = "Numeri"
d["Number Flashcards"] = "Impara i numeri con le schede"
d["Learn to Count"] = "Impara a contare"
d["Basic Addition"] = "Addizione di base"
d["Basic Subtraction"] = "Sottrazione di base"
d["Shopping List"] = "Lista della spesa"
d["Plus or Minus"] = "Più o meno"
d["Basic Operations"] = "Operazioni di base"
d["Multiplication Table"] = "Tabella di moltiplicazione"
d["Find the product"] = "Trova il prodotto"
d["Find the multiplier"] = "Trova il moltiplicatore"
d["Division"] = "Divisione"
d["Sorting Numbers"] = "Ordinare i numeri"
d["Number Comparison"] = "Confronto di numeri"
d["Addition & Subtraction"] = "Addizione e sottrazione"
d["Comparison"] = "Confronto" #(also "Comparazione")
d["Fractions"] = "Frazioni"
d["Decimal Fractions"] = "Frazioni decimali"
d["Even or Odd"] = "Pari o dispari"
d["Shapes"] = "Forme"
d["Shape Flashcards"] = "Impara le forme con le schede"
d["Solids"] = "Solidi"
d["Solid Flashcards"] = "Geometria solida con le schede"
d["Shape Matching"] = "Forme che corrispondono"
d["help me find my shadow"] = "aiutami a trovare la mia ombra"
d["Paint"] = "Colora"
d["Colour Matching"] = "Colori che corrispondono"
d["label the colours"] = "etichetta i colori"
d["Follow the Arrows"] = "Segui le frecce"
d["remember the directions"] = "ricorda le direzioni"
d["Photographic Memory"] = "Memoria fotografica"
d["Training"] = "Allenamento"
d["Photographic Memory"] = "Memoria fotografica"
d["Automatic Levels"] = "Livelli automatici"
d["Mouse Maze"] = "Labirinto con il mouse"
d["Let's have some cheese"] = "Diamo un po 'di formaggio"
d["Sheep Maze"] = "Labirinto con le pecore"
d["Find the rest"] = "Trova il resto della mandria"
d["Connect"] = "Connettiti"
d["Balloons with threads"] = "Palloncini col filo"
d["Fifteen"] = "Quindici"
d["With a Twist"] = "Con una torsione"


#game instructions
d["Drag the slider"] = ["Trascina il dispositivo di scorrimento verso l'alto o verso il basso in modo", "che il segno giusto si trovi nel quadrato rosso"]
d["Take your sheep"] = "Unisci la tua pecora al resto del gregge"
d["Check the shopping list"] = "Controlla la lista della spesa e metti nel cesto tutti gli oggetti che servono."
d["Drag lt"] = "Trascina uno tra <, > o = (minore, maggiore o uguale) dentro il riquadro rosso."
d["Drag lt2"] = "Trascina uno dei minore, maggiore o uguale dentro il riquadro rosso."
d["Re-arrange right"] = "Riporta i numeri sovrastanti nell'ordine giusto"
d["Complete abc"] = "Completa l'alfabeto usando le lettere sovrastanti"
d["Write a word:"] = "Scrivi una parola:"
d["Find and separate"] = "Trova e separa i numeri pari da quelli dispari nelle serie sovrastanti."
d["Re-arrange alphabetical"] = "Riposiziona le lettere sovrastanti in ordine alfabetico."
d["Re-arrange ascending"] = "Riposiziona i numeri sovrastanti in ordine ascendente."


#game dialogs
d["Please try again."] = "Ritenta."
d["Sorry! It is wrong."] = "Mi spiace! E' sbagliato."
d["Perfect! Task solved!"] = "Perfetto! Compito eseguito!"
d["work harder"] = "La prossima volta impegnati di più."


#level_controller
d["Game Over!"] = "Fine del gioco!"
d["Congratulations! Game Completed."] = "Congratulazioni! Hai completato tutte le prove di questo gioco."
d["Great job!"] = ["Grandioso!","Perfetto!","Imponente!","Super!","Ben fatto!"]
d["Perfect! Level completed!"] = "Perfetto! Livello completato!"


#game specific labels:
d["area:"] = "area:"
d["perimeter:"] = "perimetro:"
d["surface area:"] = "area di superficie:"
d["volume:"] = "volume:"
d["Perfect!"] = "Perfetto!"
d["divided by"] = "diviso da"
d["multiplied by"] = "volte"
d["equals"] = "uguale"
d["Shopping List"] = "Lista della spesa"
d["Even"] = "Pari"
d["Odd"] = "Dispari"
d["white"]="bianco"
d["black"]="nero"
d["grey"]="grigio"
d["red"]="rosso"
d["orange"]="arancione"
d["yellow"]="giallo"
d["olive"]="oliva"
d["green"]="verde"
d["sea green"]="verde mare"
d["teal"]="verde blu"
d["blue"]="blu"
d["navy"]="blu scuro"
d["purple"]="porpora"
d["violet"]="violetto"
d["magenta"]="magenta"
d["indigo"]="indaco"
d["pink"]="rosa"
d["maroon"] = "marroncino"
d["brown"] = "marrone"
d["aqua"] = "verde blu"
d["lime"] = "giallo verde"


#new
d["Keyboard Skills"] = "Tastiera arcobaleno"
d["Touch Typing"] = "Insegnante a scrivere con il tocco"
d["Translators"] = "Traduttori"
d["English Alphabet"] = "Alfabeto inglese"
d["Your Alphabet"] = "Alfabeto italiano"


#new in 0.3.0
d["Paint Mixer"] = "Miscelare i colori per dipingere"
d["Mixing RYB"] = "Miscelare pittura rossa, gialla, blu, nera e bianca"
d["Light Mixer"] = "Miscelare un colore aggiuntivo - Leggero"
d["Mixing RGB"] = "Miscelare rosso, verde e blu chiaro per ottenere altri colori"
d["Ink Mixer"] = "Miscela sottrattiva di colori - Pitture, tinte, inchiostri"
d["Mixing CMY"] = "Miscelare pitture ciano, magenta e gialla per ottenere altri colori"
d["Find the colour of the circle"] = "Scopri il colore del cerchio"
d["Adjust CMY"] = "Correggi il dosaggio della pittura ciano, magenta e gialla"
d["Adjust RGB"] = "Correggi l'intensità del rosso, verde e blu chiaro"

#the following is used by colour matching games in spoken hints
#ie. "more red, less green, blue is ok"
d["more color"] = "di più"
d["less color"] = "di meno"
d["color is ok"] = "va bene"

#in some languages to keep the colours gramaticaly correct
#the ie. red will be a different word in "more red" and "red is ok"
#ie. in Polish "więcej czerwonego" and "czerwony jest ok"
#and in the following 2 element lists first element is used with more, less,
#and the second with the "is ok" - in most languages those will be the same, but not in Polish or Russian
d["of red"] = ["rosso", "rosso"]
d["of green"] = ["verde", "verde"]
d["of blue"] = ["blu", "blu"]
d["of cyan"] = ["ciano", "ciano"]
d["of magenta"] = ["magenta", "magenta"]
d["of yellow"] = ["giallo", "giallo"]


#new in 0.3.1
#d["brush size"] = "dimensioni del pennello"
d["brush size"] = "dimensioni"

#new in 0.3.2
d["TicTacToe2"] = "Tic Tac Toe 2"
d["TicTacToe3"] = "Tic Tac Toe 3"
d["multiline-tictactoe"] = "Ottieni più linee di 3 che sia possibile per vincere"
d["Player"] = "Giocatore"
d["Won"] = "Vinto"
d["Game Draw"] = "Disegno"
d["UserName"] = "Nome dell'utente"
d["Match Animals Memory"] = "Fai corrispondere gli animali"
d["Match Fruits"] = "Fai corrispondere i frutti"
d["Match Vegetables"] = "Fai corrispondere le verdure"
d["Match Numbers"] = "Fai corrispondere i numeri"
d["Find pairs"] = "Scopri le immagini uguali"
d["Sliced Images"] = "Immagini affettate"
d["Sliced Animals"] = "Animali"
d["Sliced Fruits"] = "Frutti"
d["Sliced Numbers"] = "Numeri"
d["Fraction Groups"] = "Gruppi di frazioni"
d["Percentages"] = "Percentuali"
d["Ratios"] = "Rapporti"
d["Fract instr0"] = "Confronta le carte delle frazioni sulla destra con quelle sulla sinistra"
d["Fract instr1"] = ["Confronta le carte e le frazioni sulla destra","con le carte delle frazioni sulla sinistra"]
d["Fract instr2"] = "Confronta le carte delle frazioni con le frazioni sulla sinistra"

d["Fract instr3"] = ["Confronta le carte delle frazioni, le frazioni e le frazioni decimali sulla destra","con le loro rappresentazioni in percentuale"]
d["Fract instr4"] = ["Confronta le carte con i rapporti sulla sinistra","I rapporti sono espressi come rapporto di pezzi colorati con pezzi bianchi"]
d["Maths Matching Game"] = "Gioco di confronto matematico"
d["Addition"] = "Addizione"
d["Subtraction"] = "Sottrazione"
d["Multiplication"] = "Moltiplicazione"
d["Division"] = "Divisione"
d["Check for newer version..."] = ["Controlla la presenza di versioni più nuove, riferisci sui bug, discuti, traduci","o revisiona questo progetto su:"]
d["Match numbers to their spelling"] = "Confronta i numeri con la loro pronuncia"
d["Number Spelling"] = "Pronuncia dei numeri"
d["Match Animals"] = "Confronta gli animali"
d["Find all matching animals"] = "Trova gli animali corrispondenti"
d["Match animals to their shadows"] = "Confronta gli animali con le loro ombre"
d["ShapeMaker"] = "Creatore di forme"
d["draw_instr1"] = "Forma da disegnare: %s "

d["draw_instr2"] = "Forma da disegnare: %s"
d["size_instr_0"] = "così che le lunghezze delle loro basi siano uguali a %d e %d e l'altezza a %d"
d["size_instr_1"] = "così che le lunghezze dei loro lati siano uguali a %d"
d["size_instr_2"] = "così che le lunghezze dei loro lati siano uguali a %d e %d"
d["size_instr_3"] = "così che le lunghezze delle loro 2 basi parallele siano uguali a %d e l'altezza a %d"
d["size_instr_4"] = "così che la lunghezza della sua base sia uguale a %d e l'altezza a %d"
d["size_instr_5"] = "così che le lunghezze dei suoi catati siano uguali a %d e %d"
d["size_instr_6"] = "così che le lunghezze di entrambi i suoi cateti siano uguali a %d"
d["size_instr_7"] = "così che la lunghezza della sua ipotenusa sia uguale a %d"
d["size_instr_8"] = "così che la lunghezza di uno dei suoi lati sia uguale a %d e l'altezza a %d"
d["size_instr_9"] = "così che la lunghezza del suo raggio sia uguale a %d"


d["square"] = shape_names[5]
d["rectangle"] = shape_names[6]
d["right_trapezium"] = shape_names[7]
d["iso_trapezium"] = shape_names[8]
d["rhombus"] = shape_names[9]
d["parallelogram"] = shape_names[10]
d["quadrilateral"] = "quadrilatero"
d["trapezium"] = "Trapezio"
d["u_trapezium"] = "Trapezio"
d["triangle"] = "Triangolo"

d["squished_quadi"] = "Ouch... quadrilatero schiacciato"

d["equi_tria"] = shape_names[0]
d["iso_tria"] = shape_names[1]
d["obtuse_tria"] = shape_names[2]
d["right_tria"] = shape_names[3]
d["acute_tria"] = shape_names[4]
d["right_iso_tria"] = "Triangolo isoscele rettangolo"
d["obtuse_iso_tria"] = "Triangolo isoscele ottuso"
d["acute_iso_tria"] = "Triangolo isoscele acuto"
d["squished_tria"] = "Ouch... triangolo schiacciato"
d["circle"] = shape_names[13]
d["triangle_not_really"] = "Triangolo? Beh, no davvero..."
d["test_yourself"] = "Provaci tu stesso"
d["Clock1"] = "Orologio"
d["Read time"] = "impare a leggere l'ora"
d["Clock2"] = "Orologio"
d["Set time"] = "impara a regolare l'orologio"
d["Set_clock"] = "Imposta l'ora a:"
d["Set_clock_instr"] = ["","Trascina le lancette dell'orologio","per regolare l'orario"]
d["What time"] = "Che ora è?"
d["close_confirm"] = "Clicca ancora per uscire"
d["answer_enter"] = "Scrivi la tua risposta e premi invio"

d["enable_untranslated"] = "FAO: Traduttori - abilitate questo per mostrare le lingue non ancora tradotte (per prova):"
d["Fullscreen:"] = "A pieno schermo"

d["Time"] = "Ora"
d["Play_w_clock"] = "Gira le lancette dell'orologio e guarda cosa succede."
d["lets_see_what_you_draw"] = "Vediamo quali forme puoi disegnare"
d["txt_only"] = "Orario soltanto nella versione testuale"
d["Clock0"] = "Come funziona l'orologio?"
d["Columnar addition"] = "Addizione in colonna"
d["Columnar subtraction"] = "Sottrazione in colonna"
d["Long multiplication"] = "Moltiplicazione lunga"
d["Long division"] = "Divisione lunga"
d["borrow 10"] = "prendere in prestito 10"
d["carry"] = "riporto"
d["demo start"] = "Partenza >>"
d["demo next eg"] = "Prossimo esempio >>"
d["demo next step"] = "Prossimo passo >>"
d["demo write"] = "scrivi"
d["Demonstration"] = "Dimostrazione"
d["DIY"] = "Fallo da te"
d["Ratio"] = "Rapporto"
d["Working with large numbers"] = "Lavorare con numeri grandi"
d["demo rewrite"] = "riscrivere "
d["remainder"] = "resto"
d["demo_result"] = "risultato"

d["TimeMatching"] = "Orologi che corrispondono"