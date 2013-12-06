# -*- coding: utf-8 -*-

#Translated by Kamila Roszak-Imiolek and Ireneusz Imiolek

#Część zdań skrócona, lub zmieniona ze wzgędów estetycznych bądź też braku miejsca na długie zdania.
#jeśli myślisz że coś mogłoby być lepiej - skontaktuj się ze mną - zmienimy...

d=dict()

shape_names = ["Trójkąt równoboczny", "Trójkąt równoramienny", "Trójkąt rozwartokątny", "Trójkąt prostokątny", "Trójkąt ostrokątny", "Kwadrat", "Prostokąt", "Trapez prostokątny", "Trapez równoramienny", "Romb", "Równoległobok "," Pięciokąt "," Sześciokąt "," Koło "," Elipsa "]
solid_names = ["Sześcian", "Prostopadłościan", "Graniastosłup prawidłowy trójkątny", "Ostrosłup prawidłowy czworokątny", "Ostrosłup prawidłowy trójkątny", "Kula", "Cylinder", "Stożek", "Torus"]
numbers = ['jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć', 'jedenaście', 'dwanaście' , 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście', 'dwadzieścia', 'dwadzieścia jeden', 'dwadzieścia dwa', 'dwadzieścia trzy', 'dwadzieścia cztery', 'dwadzieścia pięć', 'dwadzieścia sześć', 'dwadzieścia siedem', 'dwadzieścia osiem', 'dwadzieścia dziewięć']
numbers2090 = ['dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt']

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
    return ""
           
d['abc_flashcards_word_sequence'] = ['Arbuz', 'Pociąg','Buty', 'Cymbałki','Ćma', 'Dom', 'Ekran', 'Ciężarówka','Fortepian', 'Gitara', 'Hamak','Iglo', 'Jabłko', 'Kwiatki', 'Lew', 'Łódka', 'Mrówka', 'Noc','Koń', 'Okno','Królik', 'Pomidor', 'Ryba', 'Sowa', 'Ślimak','Tygrys','Ulica', 'Winogron','Mysz', 'Zebra', 'Źrebak','Żyrafa']
d['abc_flashcards_frame_sequence'] = [26, 63, 60, 23, 44, 7, 40, 50, 34, 28, 56, 8, 42, 36, 11,  1, 0, 54, 45, 22, 17, 33, 5, 14, 61, 65,53, 6, 12, 25, 62,30]

#used in telling time activity
d["minute_numbers_1to29"] = ['jeden','dwie']
d["minute_numbers_1to29"].extend(numbers[2:])

#hours case 0: full hour, ie. one o'clock, two o'clock, etc.
d["hours_a"] = ["pierwsza","druga","trzecia","czwarta","piąta","szósta","siódma","ósma","dziewiąta","dziesiąta","jedenasta","dwunasta"]

#hours case 1: ie. ten past one, 22 past three, etc. 
d["hours_b"] = ["pierwszej","drugiej","trzeciej","czwartej","piątej","szóstej","siódmej","ósmej","dziewiątej","dziesiątej","jedenastej","dwunastej"]

#hours case 2: ie. ten to one, 22 to three, etc.
d["hours_c"] = d["hours_a"][:]

d["time_string_one_to"] = "za minute %s"
d["time_string_one_past"] = "minuta po %s"
d["time_string_to_mh"] = "za %s %s" #ie. za pięć dziesiąta
d["time_string_past_mh"] = "%s po %s" #ie. pięć po drugiej
d["time_string_to_hm"] = "" #ie. 3:55 = four o'clock in five
d["time_string_past_hm"] = "" #ie. 4:05 = four and five minutes
#if you never use the "to the hour" form leave the above fields blank and only fill one of the following two
d["time_string_1_59_past_mh"] = "" 
d["time_string_1_59_past_hm"] = ""
d["time_string_3q_past"] = "" #if you don't use quarter to but rather past use this one to either say it's 3 quarters past or 45 past - and leave the "quarter to" field blanck

d["time_string_half_to"] = "wpół do %s" #ie. wpół do dziewiątej
d["time_string_half_past"] = "" #ie. wpół do dziewiątej
d["time_string_q_to"] = "za kwadrans %s"
d["time_string_q_past"] = "kwadrans po %s"
d["time_string_full"] = "%s godzina"

fruit = ["zielone jabłko", "czerwone jabłko", "truskawka", "gruszka", "pomarańcza", "cebula", "pomidor", "cytryna", "wiśnia", "papryka", "marchewka", "banan","arbuz"]

#2,3,4
fruits_1 = ["zielone jabłka", "czerwone jabłka", "truskawki", "gruszki", "pomarańcze", "cebule", "pomidory", "cytryny", "wiśnie", "papryki", "marchewki", "banany","arbuzy"]
#5,6,7
fruits_2 = ["zielonych jabłek", "czerwonych jabłek", "truskawek", "gruszek", "pomarańczy", "cebul", "pomidorów", "cytryn", "wiśni", "papryk", "marchewek", "bananów","arbuzów"]
#[[for this number of fruits (in range of 2-7) use names from fruits_1],[and for those from fruits_2]]
plural_rules = [[2,3,4],[5,6,7]]

#alphabet - pl
alphabet_lc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet_uc = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']
#correction of eSpeak pronounciation of single letters if needed
letter_names = ['a', 'ą', 'be', 'ce', 'će', 'de', 'e', 'ę', 'ef', 'gje', 'ha', 'i', 'jot', 'ka', 'el', 'eł', 'em', 'en', 'eń', 'o', 'u kreskowane', 'pe', 'er', 'es', 'eś', 'te', 'u', 'wu', 'igrek', 'zet', 'ziet', 'żet' ] 

accents_lc = ['-','q','v','x']
accents_uc = ['Q','V','X']


#game start
d["Hello"] ="Cześć"
d["Welcome back."] ="Fajnie, że już jesteś spowrotem. A teraz w co zagramy?"

#menu categories
d["Info Category"] = "Ustawienia"
d["Keyboard & Mouse"] = "Klawiatura i Mysz"
d["Discover Letters"] = "Poznaj alfabet"
d["Learn Words"] = "Poznaj nowe słowa"
d["Maths"] ="Matematyka"
d["Numbers & Basic Operations"] ="Liczby i podstawowe działania"
d["Basic Operations - exercises"] = "Podstawowe działania"
d["Sorting and Comparing"] ="Sortowanie i porównywanie liczb"
d["Geometry"] ="Geometria i rozpoznawanie kształtów"
d["Art"] ="Twórcze"
d["Memory"] ="Trening pamięci"
d["Games & Mazes"] ="Łamigłówki"
d["Multiplayer"] = "Gry Multiplayer"

#settings
d["Preferences"] = "Ustawienia"
d["Language"] = "Język"
d["Reader"] = "Lektor (eSpeak)"
d["Read Instructions"] = "Czytaj Instrukcje przy starcie gier"

#games
d["About."] ="Info."
d["Game info..."] ="Informacje o grze..."
d["Credits"] = "Copyright & Credits"
d["Hit the Mole"] ="Złap Krecika"
d["Letters"] ="Litery"
d["Letter Flashcards"] ="Poznaj litery"
d["Learn to Write"] ="Nauka kaligrafii"
d["Trace Letters"] ="Przepisz litery i cyfry"
d["Complete the ABC"] ="Uzupełnij alfabet"
d["English"] = "angielski"
d["in your language"] = "polski"
d["Sorting Letters"] ="Sortowanie liter"
d["Lowercase Letters"] ="Małe litery"
d["Uppercase Letters"] ="Wielkie litery"
d["Word Builder"] ="Ułóż słowo"
d["Word Maze"] ="Labirynt nowych słówek"
d["Collect all"] ="Zbierz wszystkie litery"
d["Word Maze + 4"] ="Labirynt słów + 4"
d["Numbers"] ="Liczby"
d["Number Flashcards"] ="Poznaj cyfry"
d["Learn to Count"] ="Naucz się liczyć"
d["Basic Addition"] = "Dodawanie"
d["Basic Subtraction"] = "Odejmowanie"
d["Shopping List"] ="Na zakupach"
d["Plus or Minus"] ="Plus czy minus?"
d["Basic Operations"] ="Podstawowe zadania"
d["Multiplication Table"] ="Tabliczka mnożenia"
d["Find the product"] ="Znajdź iloczyn"
d["Find the multiplier"] ="Znajdź mnożnik"
d["Division"] ="Dzielenie"
d["Sorting Numbers"] ="Sortowanie liczb"
d["Number Comparison"] ="Porównanie liczb"
d["Addition & Subtraction"] ="Dodawanie i odejmowanie"
d["Comparison"] ="Porównanie"
d["Fractions"] ="Ułamki"
d["Decimal Fractions"] ="Ułamki dziesiętne"
d["Even or Odd"] ="Parzyste i nieparzyste"
d["Shapes"] ="Kształty"
d["Shape Flashcards"] ="Poznaj kształty"
d["Solids"] ="Bryły"
d["Solid Flashcards"] ="Geometria przestrzenna"
d["Shape Matching"] ="Przeciągnij zwierzaki do ich cieni"
d["help me find my shadow"] ="Przeciągnij zwierzaki do ich cieni"
d["Paint"] ="Artystycznie"
d["Colour Matching"] ="Kolory"
d["label the colours"] ="Przyporządkuj nazwy do kolorów"
d["Follow the Arrows"] ="Podążaj za strzałkami"
d["remember the directions"] ="zapamiętaj drogę"
d["Photographic Memory"] ="Ćwiczenie pamięci"
d["Training"] ="fotograficznej"
d["Photographic Memory"] ="Ćwiczenie pamięci"
d["Automatic Levels"] ="automatyczne poziomy"
d["Mouse Maze"] ="Mysi Labirynt"
d["Let's have some cheese"] ="Mam ochotę na serek"
d["Sheep Maze"] ="Owieczka w labiryncie"
d["Find the rest"] ="Znajdź moją rodzinkę"
d["Connect"] ="Połącz"
d["Balloons with threads"] ="balony z nitkami"
d["Fifteen"] ="Piętnaście"
d["With a Twist"] ="mniej więcej"

#game instructions
d["Drag the slider"] ="Przeciągnij suwak tak by właściwy znak był w czerwonym kwadracie."
d["Take your sheep"] ="Doprowadź owce do reszty stada."
d["Check the shopping list"] ="Sprawdź listę zakupów i przeciągnij potrzebne owoce do koszyka."
d["Drag lt"] =["Przeciągnij jeden z <, > lub = (mniejsze, większe lub równe)", "do czerwonego kwadratu w środku."]
d["Drag lt2"] ="Przeciągnij większy, mniejszy lub równy do czerwonego kwadratu."
d["Re-arrange right"] ="Ułóż powyższe liczby we właściwej kolejności"
d["Complete abc"] ="Uzupełnij alfabet."
d["Write a word:"] ="Ułóż słowo:"
d["Find and separate"] ="Znajdź i oddziel liczby parzyste od nieparzystych."
d["Re-arrange alphabetical"] ="Ułóż powyższe litery w kolejności alfabetycznej."
d["Re-arrange ascending"] ="Ułóż powyższe liczby w porządku rosnącym."

#game dialogs
d["Please try again."] ="Spróbuj ponownie."
d["Sorry! It is wrong."] ="Niestety! Coś jeszcze nie jest dobrze."
d["Perfect! Task solved!"] ="Świetnie! Zadanie rozwiązane!"
d["work harder"] ="Musisz popracować trochę ciężej następnym razem."

#level_controller
d["Game Over!"] = "Koniec Gry!"
d["Congratulations! Game Completed."] = "Gratulacje! Wszystkie zadania wykonane."
d["Great job!"] = ["Świetnie!","Idealnie!","Wspaniale!","Super!"]

d["Perfect! Level completed!"] = "Rewelacja! Poziom ukończony!"

#game specific labels:
d["area:"] ="powierzchnia:"
d["perimeter:"] ="obwód:"
d["surface area:"] ="powierzchnia:"
d["volume:"] ="objętość:"
d["Perfect!"] ="Super!"
d["divided by"] ="podzielone przez"
d["multiplied by"] ="razy"
d["equals"] ="równa się"
d["Shopping List"] ="Lista zakupów"
d["Even"] ="Parzyste"
d["Odd"] ="Nieparzyste"
d["white"]="biały"
d["black"]="czarny"
d["grey"]="szary"
d["red"]="czerwony"
d["orange"]="pomarańczowy"
d["yellow"]="żółty"
d["olive"]="oliwkowy"
d["green"]="zielony"
d["sea green"]="morska zieleń"
d["teal"]="morski"
d["blue"]="niebieski"
d["navy"]="granatowy"
d["purple"]="purpurowy"
d["violet"]="fioletowy"
d["magenta"]="fuksja"
d["indigo"]="indygo"
d["pink"]="różowy"
d["maroon"] = "bordowy"
d["brown"] = "brązowy"
d["aqua"] = "aqua"
d["lime"] = "limetkowy"

#new
d["Keyboard Skills"] = "Tęczowa Klawiatura"
d["Touch Typing"] = "Nauka szybkiego pisania na klawiaturze"
d["Translators"] = "Tłumaczenia"
d["English Alphabet"] = "Angielski alfabet"
d["Your Alphabet"] = "Polski alfabet"

#new in 0.3.0
d["Paint Mixer"] = "Mieszamy Kolory - Farba"
d["Mixing RYB"] = "Czerwony, żółty, niebieski, czarny i biały"
d["Light Mixer"] = "Mieszamy Kolory - Światło"
d["Mixing RGB"] = "Uzyskaj inne kolory z czerwonego, zielonego i niebieskiego"
d["Ink Mixer"] = "Mieszamy Kolory - Farba, Tusz"
d["Mixing CMY"] = "Uzyskaj inne kolory z kolorów: cyjan, magenta i żółty"

d["Find the colour of the circle"] = "Znajdź Kolor Koła"
d["Adjust CMY"] = "Dopasuj ilość koloru cyjan, magenta i żółtego"
d["Adjust RGB"] = "Dopasuj intensywność czerowego, zielonego i niebieskiego światła"

#the following is used by colour matching games in spoken hints
#ie. "more red, less green, blue is ok"
d["more color"] = "więcej"
d["less color"] = "mniej"
d["color is ok"] = "jest o-kej" #o-kej bo "ok" jest czyt. jako około, a w okej akcent pada na "e" i nie brzmi to dobrze :)
#in some languages to keep the colours gramaticaly correct 
#the ie. red will be a different word in "more red" and "red is ok"
#ie. in Polish "więcej czerwonego" and "czerwony jest ok"
#and in the following 2 element lists first element is used with more, less,
#and the second with the "is ok" - in most languages those will be the same, but not in Polish or Russian
d["of red"] = ["czerwonego","czerwony"]
d["of green"] = ["zielonego","zielony"]
d["of blue"] = ["niebieskiego","niebieski"]
d["of cyan"] = ["koloru cyjan","cyjan"]
d["of magenta"] = ["koloru magenta","magenta"]
d["of yellow"] = ["żółtego","żółty"]

#new in 0.3.1
d["brush size"] = "rozmiar pędzla"

#new in 0.3.2
d["TicTacToe2"] = "Kółko i krzyżyk 2"
d["TicTacToe3"] = "Kółko i krzyżyk 3"
d["multiline-tictactoe"] = "Ułóż jak najwięcej potrójnych linii by wygrać"

d["Player"] = "Gracz"
d["Won"] = "Wygrał"
d["Game Draw"] = "Remis"
d["UserName"] = "Imię"

d["Match Animals"] = "Dopasuj zwierzaki"
d["Match Fruits"] = "Dopasuj owoce"
d["Match Vegetables"] = "Dopasuj warzywa"
d["Match Numbers"] = "Dopasuj numerki"
d["Find pairs"] = "Znajdź pary takich samych obrazków"

d["Match Animals Memory"] = "Zapamiętaj położenie zwierzaków"
d["Match Fruits"] = "Zapamiętaj położenie owoców"
d["Match Vegetables"] = "Zapamiętaj położenie warzyw"
d["Match Numbers"] = "Zapamiętaj położenie numerków"
d["Find pairs"] = "Znajdź pary takich samych obrazków"

d["Sliced Images"] = "Przesówanka"
d["Sliced Animals"] = "Zwierzaki"
d["Sliced Fruits"] = "Owoce"
d["Sliced Numbers"] = "Numerki"

d["Fraction Groups"] = "Ułamki"
d["Percentages"] = "Procenty"
d["Ratios"] = "Stosunki"
d["Fract instr0"] = ["Dopasuj graficzne reprezentacje ułamków po prawej", "do tych po lewej"] #Match fraction charts on the right to the ones on the left"
d["Fract instr1"] = ["Dopasuj ułamki zwykłe i ich graficzne reprezentacje po prawej", "to tych po lewej"]# Match fraction charts and fractions on the right","to the fraction charts on the left"]
d["Fract instr2"] = ["Dopasuj graficzne reprezentacje ułamków po prawej", "do ułamków zwykłych po lewej"]#"Match fraction charts to the fractions on the left"
d["Fract instr3"] = ["Dopasuj graficzne reprezentacje ułamków, ułamki zwykłe i dziesiętne", " do procentów po lewej"]#["Match fraction charts, fractions and decimal fractions on the right","to their percentage representations"]
d["Fract instr4"] = ["Dopasuj graficzne reprezentacje stosunku kolorowych części do białych","do ich liczbowego zapisu po lewej"]#["Match charts to the ratios on the left","Ratios are expressed as ratio of coloured pieces to white pieces"]

d["Maths Matching Game"] = "Matematyczna dopasowanka"
d["Addition"] = "Dodawanie"
d["Subtraction"] = "Odejmowanie"
d["Multiplication"] = "Mnożenie"
d["Division"] = "Dzielenie"

#d["Check for newer version..."] = ["","Check for newer version, report bugs, discuss, translate or review this project at:"]
d["Check for newer version..."] = ["","Sprawdź najnowszą wersję, zgłaszaj błędy i pomysły, przetłumacz lub oceń ten projekt na:"]
d["Match numbers to their spelling"] = "Dopasuj liczby do ich słownego zapisu"
d["Number Spelling"] = "Zapis słowny liczb"

d["Match Animals"] = "Zwierzakowa dopasowanka"
d["Find all matching animals"] = "Znajdź takie same zwierzaki"
d["Match animals to their shadows"] = "Dopasuj zwierzaki do ich cieni"

d["ShapeMaker"] = "Shape Maker"

d["draw_instr1"] = "Figura do narysowania: %s"
d["draw_instr2"] = "Figura do narysowania: %s" #if the following size_instr turn out to be too long the beginning can be moved here, ie. d["draw_instr2"] = "Shape to draw: %s, such that" 

d["size_instr_0"] = "o długości podstaw równej %d i %d, i wysokości równej %d" #for trapeziums
d["size_instr_1"] = "o długości ścian równej %d" #square
d["size_instr_2"] = "o długości ścian równej %d i %d" #rectangle
d["size_instr_3"] = "o długości jednej z podstaw równej %d i wysokości równej %d" #for parallelogram
d["size_instr_4"] = "o długości podstawy równej %d i wysokości równej %d" #for triangles incl. isosceles triangles
d["size_instr_5"] = "o długości przyprostokątnych równej %d i %d" #for right triangles
d["size_instr_6"] = "o długości obu przyprostokątnych równej %d" #for right isosceles triangles
d["size_instr_7"] = "o długości przeciwprostokątnej równej %d" #for right isosceles triangles
d["size_instr_8"] = "o długości jednej ze ścian równej %d i wysokości spadającej na nią równej %d" #for obtuse triangles
d["size_instr_9"] = "o promieniu o długości %d" #for circles

d["square"] = shape_names[5]
d["rectangle"] = shape_names[6]
d["right_trapezium"] = shape_names[7] 
d["iso_trapezium"] = shape_names[8] 
d["rhombus"] = shape_names[9] 
d["parallelogram"] = shape_names[10] 
d["quadrilateral"] = "Czworokąt"
d["trapezium"] = "Trapez"
d["u_trapezium"] = "Trapez"
d["triangle"] = "Trójkąt"
d["squished_quadi"] = "Nieco przymiażdżony czworokąt"

d["equi_tria"] = shape_names[0]
d["iso_tria"] = shape_names[1]
d["obtuse_tria"] = shape_names[2]
d["right_tria"] = shape_names[3]
d["acute_tria"] = shape_names[4]
d["right_iso_tria"] = "Trójkąt prostokątny równoramienny"
d["obtuse_iso_tria"] = "Trójkąt rozwartokątny równoramienny"
d["acute_iso_tria"] = "Trójkąt ostrokątny równoramienny"
d["squished_tria"] = "Nieco przymieżdżony trójkąt"
d["circle"] = shape_names[13]
d["triangle_not_really"] = "Trójkąt? Niezupełnie..."

d["test_yourself"] = "Sprawdź się"
d["Clock1"] = "Zegar"
d["Read time"] = "odczytaj czas"
d["Clock2"] = "Zegar"
d["Set time"] = "ustaw właściwy czas na zegarze"
d["Set_clock"] = "Ustaw zegar na godzinę:"
d["Set_clock_instr"] = ["","Przeciągnij wskazówki","by ustawić czas"]
d["What time"] = "Która godzina?"
d["close_confirm"] = "Przyciśnij jeszcze raz by wyjść z gry"
d["answer_enter"] = "Wpisz odpowiedź i wciśnij enter"

d["enable_untranslated"] = "Do Tłumaczy - włącz tę opcje by wyświetlić dodatkowe języki (do testowania):"
d["Fullscreen:"] = "Pełny ekran:"
d["Time"] = "Czas"
d["Play_w_clock"] = "Pokręć wskazówkami i sprawdź co się stanie."


d["lets_see_what_you_draw"] = "Zobaczmy jakie kształty umiesz narysować"
d["txt_only"] = "Tym razem tylko zapis słowny."
d["Clock0"] = "Jak działa zegar?"

d["Columnar addition"] = "Dodawanie pisemne"
d["Columnar subtraction"] = "Odejmowanie pisemne"
d["Long multiplication"] = "Mnożenie pisemne"
d["Long division"] = "Dzielenie pisemne"
d["borrow 10"] = "pożyczamy 10"
d["carry"] = "przenosimy"
d["demo start"] = "Zacznij >>"
d["demo next eg"] = "Następny przykład >>"
d["demo next step"] = "Następny krok >>"
d["demo write"] = "wpisujemy " #used to show which digit of the result should be entered in a box, ie. "enter 5"

d["Demonstration"] = "Samouczek"
d["DIY"] = "Zrób to sam"
d["Ratio"] = "Ratio"
d["Working with large numbers"] = "Działania na dużych liczbach"
d["demo rewrite"] = "przepisujemy "
d["remainder"] = "remainder"
d["demo_result"] = "wynik"
d["TimeMatching"] = "Zegarkowa dopasowanka"