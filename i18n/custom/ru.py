# -*- coding: utf-8 -*-

#Translated by Anton Kayukov (Антон Каюков), Alexey Loginov (Алексей Логинов)

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

d=dict() # messages for display
dp = dict() # messages with pronunciation exceptions - this dictionary will override entries in a copy of d

d["local_kbrd"] = "Русскими буквами"
d["Clock0 - Russian official time"] = "Научитесь читать официальное русское время" #Learn to read Russian official time
d["Russian official - subtitle"] = ""

d["Clock2 - Russian official time"] = "Официальное русское время" #Russian official time
d["Russian official - txt_only"] = "Протестируйте сами себя" #test yourself

numbers = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать", "двадцать один", "двадцать два", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять"]
numbers2090 = ['двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']

d['abc_flashcards_word_sequence'] = ['Автобус', 'Банка', 'Виноград','Гитара','Дом','Ель', 'Ёж', 'Жеребец', 'Зебра',  'Иглу', 'Йога','Кошка','Лев', 'Муравей', 'Ночь', 'Обувь', 'Попугай', 'Рыба', 'Слон','Томат','Утка','Филин', 'Хлеб', 'Цветок', 'Чайник', 'Шлюпка', 'Щука','Съёмка', 'Мышь', 'Нить', 'Электричка', 'Юбка', 'Яхта']
d['abc_flashcards_frame_sequence'] = [77, 9, 6, 28, 7, 31, 29, 45, 25,8, 32, 2, 11, 0, 54, 60,  15, 5, 4, 33, 3, 14, 35, 69, 19, 1, 38, 39,12, 24, 63, 41, 66]

#alphabet ru: - 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' & 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_lc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet_uc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
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
    elif n == 0: return "ноль"
    elif n == 100: return "сто"
    return ""

#TIME FOR DISPLAY
mt1 = ["одна","две","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать","двадцать","двадцать одна","двадцать две","двадцать три","двадцать четыре","двадцать пять","двадцать шесть","двадцать семь","двадцать восемь","двадцать девять", "тридцать", "тридцать одна","тридцать две","тридцать три","тридцать четыре","тридцать пять","тридцать шесть","тридцать семь","тридцать восемь","тридцать девять"]
mt2 = ["одной","двух","трёх","четырёх","пяти","шести","семи","восьми","девяти","десяти","одиннадцати","двенадцати","тринадцати","четырнадцати","пятнадцати","шестнадцати","семнадцати","восемнадцати","девятнадцати","двадцати","двадцати одной","двадцати двух", "двадцати трёх", "двадцати четырёх", "двадцати пяти","двадцати шести", "двадцати семи", "двадцати восьми", "двадцати девяти"]

ht1 = ["час","два","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать"]
ht2 = ["первого", "второго", "третьего", "четвёртого", "пятого", "шестого", "седьмого", "восьмого", "девятого", "десятого", "одиннадцатого", "двенадцатого"]

def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 0:
        if h == 12: h = 1
        else: h += 1
        
    if m == 0:
        if h == 1: return "один час"
        elif h < 5: return "%s часа" % ht1[h-1]
        else: return "%s часов" % ht1[h-1]
    elif m == 15: return "четверть %s" % ht2[h-1]
    elif m == 20: return "%s минут %s" % (mt1[m-1], ht2[h-1])
    elif m in [1,21]: return "%s минута %s" % (mt1[m-1], ht2[h-1])
    elif m in [2,3,4,22,23,24]: return "%s минуты %s" % (mt1[m-1], ht2[h-1])
    elif m < 30: return "%s минут %s" % (mt1[m-1], ht2[h-1])
    elif m == 30: return "половина %s" % ht2[h-1]
    elif m == 39: return "без двадцати одной минуты %s" % ht1[h-1]
    elif m == 40: return "без %s минут %s" % (mt2[60-m-1], ht1[h-1])
    elif m == 45: return "без четверти %s" % ht1[h-1]
    elif m == 59: return "без одной минуты %s" % ht1[h-1]
    elif m > 30: return "без %s минут %s" % (mt2[60-m-1], ht1[h-1])
    return ""
    
def time2officialstr(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'

    #get the right "suffix" for hour
    if h == 1: sf = "час"
    elif h < 5: sf = "часа"
    else: sf = "часов"
    
    if m == 0: return "%s %s" % (ht1[h-1], sf)
    elif m == 1: return "%s %s одна минута" % (ht1[h-1], sf)
    elif m in [21,31,41,51]: return "%s %s %s одна минута" % (ht1[h-1], sf, n2txt(m-1))
    elif m == 2: return "%s %s две минуты" % (ht1[h-1], sf)
    elif m in [22,32,42,52]: return "%s %s %s две минуты" % (ht1[h-1], sf, n2txt(m-2))
    elif m in [3,4,23,24,33,34,43,44,53,54]: return "%s %s %s минуты" % (ht1[h-1], sf, n2txt(m))
    else: return "%s %s %s минут" % (ht1[h-1], sf, n2txt(m))
    return ""
    
#TIME FOR SPEAKER
spkmt1 = ["одна","две","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","20 одна","20 две","23","24","25","26","27","28","29","30", "30 одна","30 две","33","34","35","36","37","38","39"]
spkmt2 = ["одной","двух","трёх","четырёх","пяти","шести","семи","вось-ми","девя-ти","десяти","1-надца-ти","две-надца-ти","три-надца-ти","четыр-надца-ти","пят-надца-ти","шест-надца-ти","сем-надца-ти","восем-надца-ти","девят-надца-ти","двадца-ти","двадца-ти одной","двадца-ти двух", "двадца-ти трёх", "двадца-ти четырёх", "двадца-ти пяти","двадца-ти шести", "двадца-ти семи", "двадца-ти вось-ми", "двадца-ти девя-ти"]

spkht1 = ["час","2","3","4","5","6","7","8","9","10","11","12"]
spkht2 = ["пер-во-во", "второго", "треть-его", "четвёртого", "пя-то-во", "шестого", "седьмого", "восьмого", "девятого", "десятого", "1-надца-того", "две-надца-того"]

def time2spk(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string but in exception format for espeak Russian language'
    if m > 0:
        if h == 12: h = 1
        else: h += 1
        
    if m == 0:
        if h == 1: return "1 час"
        elif h < 5: return "%s ча-са" % spkht1[h-1]
        else: return "%s ча-сов" % spkht1[h-1]
    elif m == 15: return "чет-верть %s" % spkht2[h-1]
    elif m == 20: return "%s минут %s" % (spkmt1[m-1], spkht2[h-1])
    elif m in [1,21]: return "%s минута %s" % (spkmt1[m-1], spkht2[h-1])
    elif m in [2,3,4,22,23,24]: return "%s минуты %s" % (spkmt1[m-1], spkht2[h-1])
    elif m < 30: return "%s минут %s" % (spkmt1[m-1], spkht2[h-1])
    elif m == 30: return "половина %s" % spkht2[h-1]
    elif m == 39: return "без двад-ца-ти одной минуты %s" % spkht1[h-1]
    elif m == 40: return "без %s минут %s" % (spkmt2[60-m-1], spkht1[h-1])
    elif m == 45: return "без четвер-ти %s" % spkht1[h-1]
    elif m == 59: return "без од-ной минуты %s" % spkht1[h-1]
    elif m > 30: return "без %s минут %s" % (spkmt2[60-m-1], spkht1[h-1])
    return ""
    
def time2officialspk(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'

    #get the right "suffix" for hour
    if h == 1: sf = "час"
    elif h < 5: sf = "ча-са"
    else: sf = "ча-сов"
    
    if m == 0: return "%s %s" % (spkht1[h-1], sf)
    elif m == 1: return "%s %s одна минута" % (spkht1[h-1], sf)
    elif m in [21,31,41,51]: return "%s %s %d-одна минута" % (spkht1[h-1], sf, m-1)
    elif m == 2: return "%s %s две минуты" % (spkht1[h-1], sf)
    elif m in [22,32,42,52]: return "%s %s %d-две минуты" % (spkht1[h-1], sf, m-2)
    elif m in [3,4,23,24,33,34,43,44,53,54]: return "%s %s %d минуты" % (spkht1[h-1], sf, m)
    else: return "%s %s %d минут" % (spkht1[h-1], sf, m)
    return ""


dp["Welcome back."] = "Доб-ро по-жа-ловать в иг-ру."

dp['abc_flashcards_word_sequence'] = ['Автобус', 'Банка', 'Виноград','Гитара','Дом','Ель', 'Ёж', 'Жеребец', 'Зебра',  'Иглу', 'Йога','Кошка','Лев', 'Муравей', 'Ночь', 'Обувь', 'Попугай', 'Рыба', 'Слон','Томат','Утка','Филин', 'Хлеб', 'Цветок', 'Чайник', 'Шлюпка', 'Щука','Съёмка', 'Мышь', 'Нить', 'Электричка', 'Юбка', 'Яхта']
dp["shape_names"] = ["Равносторонний треугольник", "Равнобедренный треугольник", "Тупоугольный треугольник", "Прямоугольный треугольник", "Остроугольный треугольник", "Квадрат", "Прямоугольник", "Правильная трапеция", "Равнобедренная трапеция", "Ромб", "Пара-лле-ло-грамм", "Пятиугольник", "Шестиугольник", "Круг", "Эллипс"]
dp["solid_names"] = ["Куб", "Квадратная призма", "Треугольная призма", "Квадратная пирамида", "Треугольная пирамида", "Сфера", "Цилиндр", "Конус", "Тор"]

dp["fruit"] = ["зе-лё-ное яб-ло-ко", "крас-ное яб-ло-ко", "клубника", "груша", "апель-син", "луковица", "томат", "ли-мон", "вишня", "пе--рец", "мор-ковь", "ба-нан","ар-буз"]

#game instructions				
dp["Drag the slider"] = "Перетащите ползунок вверх или вниз так, чтобы правильный знак оказался в красном квадрате." #Drag the slider up or down so that the right sign is in the red square.
#dp["Take your sheep"] = "Приве-ди-те овцу к ос-таль-но-му стаду." #Take your sheep to the rest of the herd.

dp["Check the shopping list"] = "Проверьте список покупок и перетащите все необходи-мые предметы в корзину." #Check the shopping list and drag all needed items into the basket.
dp["Drag lt2"] = "Перетащите 1 из меньше, больше или ра-вно в красный квадрат." #Drag one of the greater, lesser or equal to the red square.
dp["Re-arrange right"] = "Переставьте цифры, чтобы они были в правильном порядке" #Re-arrange the above numbers so they are in the right order
dp["Complete abc"] = "Заполните алфавит с помощью букв." #Complete the abc using the letters above.
dp["Write a word:"] = "Напишите слово:" #Write a word:
dp["Find and separate"] = "Найдите и отделите чётные числа от нечётных чисел в указанной последовательна-сти." #Find and separate the Even Numbers form the Odd Numbers in the above series.
dp["Re-arrange alphabetical"] = "Переставьте буквы, чтобы они были в алфавитном порядке." #Re-arrange the above letters so they are in the alphabetical order.
dp["Re-arrange ascending"] = "Переставьте цифры, чтобы они были в порядке возрастания." #Re-arrange the above numbers so they are in the ascending order.

#dp["Please try again."] = "Пожалуйста, попробуйте ещё раз."#no longer used
#dp["Sorry! It is wrong."] = "Извините! Это неправильно." #no longer uses
dp["Perfect! Task solved!"] = "Великолепно! Задача решена!"
dp["work harder"] = "В следующий раз постарайтесь ра-бо-тать лучше."

#level_controller
dp["Game Over!"] = "Игра проиграна!"
dp["Congratulations! Game Completed."] = "Поздравляем! Вы выполнили все задачи в этой игре."
dp["Great job!"] = ["Отличная работа", "Велико-лепно", "Потрясающе","Фантастическая работа", "Мо-ло-дец"] #["Great job!","Perfect!","Awesome!","Fantastic job!","Well done!"]
dp["Perfect! Level completed!"] = "Великолепно! Уровень завершён!"

dp["Perfect!"] = "Велико-лепно" #Perfect!

#game specific labels:				
dp["area:"] = "пло-щадь:" #area:
dp["circumference:"] = "окру--жность::" #circumference:
dp["perimeter:"] ="периметр:"
dp["surface area:"] = "пло-щадь поверхности:" #surface area:
dp["volume:"] = "объём" #volume:
dp["divided by"] = "делённое на" #divided by
dp["multiplied by"] = "умножен-ное на"
dp["equals"] = "ра-вно" #equals
#dp["Shopping List"] = "Список поку-пок" #Shopping List
dp["Even"] = "Чётные" #Even 
dp["Odd"] = "Нечётные" #Odd

dp["white"] = "Белый" #"white"
dp["black"] = "Чёрный" #"black"
dp["grey"] = "Серый" #"grey"
dp["red"] = "Красный" #"red"
dp["orange"] = "Оран-же-вый" #"orange"
dp["yellow"] = "Жёлтый" #"yellow"
dp["olive"] = "Оли-вковый" #"olive"
dp["green"] = "Зелёный" #"green"
dp["sea green"] = "Мор-ской вол-ны" #"sea green"
dp["teal"] = "Сине-зелёный" #"teal"
dp["blue"] = "Синий" #"blue"
dp["navy"] = "Тёмно-синий" #"navy"
dp["purple"] = "Фиолетовый" #"purple"
#dp["violet"] = "Лиловый" #"violet"
dp["magenta"] = "Пурпурный" #"magenta"
dp["indigo"] = "Индиго" #"indigo"
dp["pink"] = "Ро-зо-вый" #"pink"
dp["maroon"] = "Бордовый" #maroon
dp["brown"] = "Коричневый" #brown
dp["aqua"] = "Го-лу-бой" #aqua
dp["lime"] = "Лайм" #lime

dp["more red"] = "ещё красного"
dp["more green"] = "ещё зелёного"
dp["more blue"] = "ещё синего"
dp["more cyan"] = "ещё го-лу-бого"
dp["more magenta"] = "ещё пурпурного"
dp["more yellow"] = "ещё жёлтого"

dp["less red"] = "поменьше красного"
dp["less green"] = "поменьше зелёного"
dp["less blue"] = "поменьше синего"
dp["less cyan"] = "поменьше го-лу-бого"
dp["less magenta"] = "поменьше пурпурного"
dp["less yellow"] = "поменьше жёлтого"

dp["red is ok"] = "красного нормально"
dp["green is ok"] = "зелёного нормально"
dp["blue is ok"] = "синего нормально"
dp["cyan is ok"] = "го-лу-бого нормально"
dp["magenta is ok"] = "пурпурного нормально"
dp["yellow is ok"] = "жёлтого нормально"

#new in 0.3.1
#dp["brush size"] = "раз-мер кисти" #brush size

#new in 0.3.2
#dp["TicTacToe2"] = "Крестики-нолики 2" #Tic Tac Toe 2
#dp["TicTacToe3"] = "Крестики-нолики 3" #Tic Tac Toe 3
#dp["multiline-tictactoe"] = "Чтобы победить, сделайте тройные линии, насколько это будет возможно" #Get as many lines of 3 as possible to win

dp["Fract instr0"] = "Устано-вите соответствие дро-бей справа и дро-бей слева" #Match fraction charts on the right to the ones on the left
dp["Fract instr1"] = "Устано-вите соответствие дро-бей справа дро-бям слева" #[Match fraction charts and fractions on the right","to the fraction charts on the left"]
dp["Fract instr2"] = "Устано-вите соответствие дро-бей справа дро-бям слева" #Match fraction charts to the fractions on the left
dp["Fract instr3"] = "Устано-вите соответствие дро-бей и десятичных дро-бей слева их процентному представлению справа" #["Match fraction charts, fractions and decimal fractions on the right","to their percentage representations"]
dp["Fract instr4"] = "Устано-вите соответствие отношений слева отношениям справа. Отношения показаны как отношения цвет-ных час-тей к белым час-тям" #["Match charts to the ratios on the left","Ratios are expressed as ratio of coloured pieces to white pieces"]

#dp["Check for newer version..."] = "Проверьте новую версию, сообщите о переводах, ошибках, идеях на сайте проэкта:" #["","Check for newer version, report bugs, discuss, translate or review this project at:"]
"""
dp["draw_instr1"] = "Нари-совать фигуру: %s"
dp["draw_instr2"] = "Нари-совать фигуру: %s" #if the following size_instr turn out to be too long the beginning can be moved here, ie. dp["draw_instr2"] = "Shape to draw: %s, such that" 

dp["size_instr_0"] = "так, чтобы длины оснований были ра-вны %d и %d, а высо-та %d" #for trapeziums
dp["size_instr_1"] = "так, чтобы длины сторон были ра-вны %d" #square
dp["size_instr_2"] = "так, чтобы длины сторон были ра-вны %d и %d" #rectangle
dp["size_instr_3"] = "так, чтобы длины двух параллельных оснований были ра-вны %d, а высо-та %d" #for parallelogram
dp["size_instr_4"] = "так, чтобы длина основания была ра-вна %d, а высота %d" #for triangles incl. isosceles triangles
dp["size_instr_5"] = "так, чтобы длины кате-тов были ра-вны %d и %d" #for right triangles
dp["size_instr_6"] = "так, чтобы длины обоих кате-тов были ра-вны %d" #for right isosceles triangles
dp["size_instr_7"] = "так, чтобы длина гипоте-нузы была ра-вна %d" #for right isosceles triangles
dp["size_instr_8"] = "так, чтобы длина одной из сторон была ра-вна %d, а высо-та %d" #for obtuse triangles
dp["size_instr_9"] = "так, чтобы длина ра-диуса была ра-вна %d" #for circles


dp["square"] = "Квадрат"
dp["rectangle"] = "Прямоугольник"
dp["right_trapezium"] = "Правильная трапеция"
dp["iso_trapezium"] = "Равнобедренная трапеция"
dp["rhombus"] = "Ромб"
dp["parallelogram"] = "Пара-лле-ло-грамм"
dp["quadrilateral"] = "Четырёхугольник"
dp["trapezium"] = "Трапеция"
dp["triangle"] = "Треугольник"

#req
dp["equi_tria"] = "Равносторонний треугольник"
dp["iso_tria"] = "Равнобедренный треугольник"
dp["obtuse_tria"] = "Тупоугольный треугольник"
dp["right_tria"] = "Прямоугольный треугольник"
dp["acute_tria"] = "Остроугольный треугольник"
dp["right_iso_tria"] = "Прямой равнобедренный треугольник" #Right isosceles triangle
dp["obtuse_iso_tria"] = "Тупой равнобедренный треугольник" #Obtuse isosceles triangle
dp["acute_iso_tria"] = "Острый равнобедренный треугольник" #Acute isosceles triangle
dp["circle"] = "Круг"
"""
