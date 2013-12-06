# -*- coding: utf-8 -*-

#Translated by Anton Kayukov (Антон Каюков)

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
#shape_names = ["Equilateral Triangle", "Isosceles Triangle", "Obtuse Triangle", "Right Triangle", "Acute Triangle", "Square", "Rectangle", "Right Trapezium", "Isosceles Trapezium", "Rhombus", "Parallelogram", "Pentagon", "Hexagon", "Circle", "Ellipse"]
shape_names = ["Равносторонний треугольник", "Равнобедренный треугольник", "Тупоугольный треугольник", "Прямоугольный треугольник", "Остроугольный треугольник", "Квадрат", "Прямоугольник", "Правильная трапеция", "Равнобедренная трапеция", "Ромб", "Параллелограмм", "Пятиугольник", "Шестиугольник", "Круг", "Эллипс"]

#solid_names = ["Cube", "Square Prism", "Triangular Prism", "Square Pyramid", "Triangular Pyramid", "Sphere", "Cylinder", "Cone", "Torus"]
solid_names = ["Куб", "Квадратная Призма", "Треугольная призма", "Квадратная пирамида", "Треугольная Пирамида", "Сфера", "Цилиндр", "Конус", "Тор"]

numbers = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать", "двадцать один", "двадцать два", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять"]
numbers2090 = ['двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']

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
           
d['abc_flashcards_word_sequence'] = ['Арбуз', 'Бабочка', 'Виноград', 'Гитара','Дом','Еж', 'Ёлка', 'Жираф', 'Зебра',  'Иглу', 'Йога', 'Кошка','Лодка', 'Муравей', 'Нить', 'Окно', 'Попугай', 'Рыба', 'Сова', 'Томат','Утка','Фортепиано', 'Хлеб', 'Цветы', 'Чайник', 'Шимпанзе', 'Щука', 'Съёмка', 'Мышь', 'Нить', 'Экран', 'Юбка', 'Яблоко']
d['abc_flashcards_frame_sequence'] = [26, 27, 6, 28, 7, 29, 31, 30, 25, 8, 32, 43, 1, 0, 24, 22,  15, 5, 14, 33, 3, 34, 35, 36, 19, 37, 38, 39, 12, 24, 40, 41, 42]

#used in telling time activity
#the number lists below are for languages with a bit more complex forms, ie. different suffixes depending on context - if your language is like that check Polish translation to see how to use them
d["minute_numbers_1to29"] = numbers[:]
#last digit when joining numbers of minutes

#hours case 0: full hour, ie. one o'clock, two o'clock, etc.
d["hours_a"] = numbers[0:12]

#hours case 1: ie. ten past one, 22 past three, etc. 
d["hours_b"] = d["hours_a"][:]

#hours case 2: ie. ten to one, 22 to three, etc.
d["hours_c"] = d["hours_a"][:]

d["time_string_one_to"] = "one minute to %s" #if you never use the to the hour form leave this blank
d["time_string_one_past"] = "one minute past %s"
#pick either mh or hm version, or leave these 4 blank if you don't use to the hour form: mh means that number of minutes will appear first in the sentence followed by the number of hours, the hm is the opposite.
d["time_string_to_mh"] = "%s to %s" #ie. five to four
d["time_string_past_mh"] = "%s past %s" #ie. five past four
d["time_string_to_hm"] = "" #ie. 3:55 = four o'clock in five
d["time_string_past_hm"] = "" #ie. 4:05 = four and five minutes

#if you never use the "to the hour" form leave the above fields blank and only fill one of the following two
d["time_string_1_59_past_mh"] = "" 
d["time_string_1_59_past_hm"] = ""
d["time_string_3q_past"] = "" #if you don't use quarter to but rather past use this one to either say it's 3 quarters past or 45 past - and leave the "quarter to" field blanck

d["time_string_q_to"] = "quarter to %s"
d["time_string_q_past"] = "quarter past %s"

d["time_string_half_to"] = "" #ie. in languages using this form, ie. half to four
d["time_string_half_past"] = "half past %s" #ie. half past three or "thirty past %s" if that sounds better
d["time_string_full"] = "%s o'clock"

fruit = ["зеленое яблоко", "красное яблоко", "клубника", "груша", "апельсин", "луковица", "томат", "лимон", "вишня", "перец", "морковь", "банан","арбуз"]
#2,3,4
fruits_1 = ["зеленых яблока", "красных яблока", "клубники", "груши", "апельсина", "луковицы", "помидора", "лимонов", "вишни", "перца", "моркови", "банана", "арбуза"]
#5,6,7
fruits_2 = ["зеленых яблок", "красных яблок", "клубник", "груш", "апельсинов", "луковиц", "помидоров", "лимонов", "вишен", "перцев", "морковей", "бананов", "арбузов"]

plural_rules = [[2,3,4],[5,6,7]]

#alphabet ru: - 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' & 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_lc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet_uc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
#correction of eSpeak pronounciation of single letters if needed
letter_names = [] 

accents_lc = ['-']
accents_uc = []

#game start				
d["Hello"] = "Привет" #Hello
d["Welcome back."] = "Добро пожаловать в игру." #Welcome back in the game.
				
#settings				
d["Preferences"] = "Предпочтения" #Preferences
d["Language"] = "Язык" #Language
d["Reader"] = "Озвучки" #eSpeak
d["Read Instructions"] = "Читайте инструкции в начале игры" #Read Instructions at the start of games
				
#menu categories				
d["Info Category"] = "Информация и параметры" #Info & Settings
d["Keyboard & Mouse"] = "Клавиатура и мышь" #Keyboard & Mouse
d["Discover Letters"] = "Изучение букв" #Discover Letters
d["Learn Words"] = "Учите новые слова" #Learn New Words
#d["Arithmetic"] = "Арифметика" #Arithmetic
d["Maths"] = "Математика" #Arithmetic

d["Numbers & Basic Operations"] = "Числа и основные операции" #Numbers & Basic Operations
d["Basic Operations - exercises"] = "Основные операции"
d["Sorting and Comparing"] = "Сортировка и Сравнение" #Sorting and Comparing
d["Geometry"] = "Геометрия, сравнение форм" #Geometry
d["Art"] = "Художество" #Art
d["Memory"] = "Память" #Memory
d["Games & Mazes"] = "Игры и Лабиринты" #Games & Mazes
d["Multiplayer"] = "Многопользовательские Игры"
				
#games				
d["About."] = "О программе." #About.
d["Game info..."] = "Информация об игре ..." #Game info...
d["Credits"] = "Авторские права и Титры" #Copyright & Credits
d["Hit the Mole"] = "Ударь крота" #Hit the Mole
d["Letters"] = "Буквы" #Letters
d["Letter Flashcards"] = "Учусь буквам по карточкам" #Learn Letters with Flashcards
d["Learn to Write"] = "Учись писать" #Учусь писать
d["Trace Letters"] = "Обвести Букв и Цифр" #Trace Letters and Numbers
d["Complete the ABC"] = "Заполните алфавит" #Complete the ABC
d["English"] = "Английский" #English
d["in your language"] = "Русский" #Русский
d["Sorting Letters"] = "Сортировка букв" #Sorting Letters
d["Lowercase Letters"] = "Строчные буквы" #Lowercase Letters
d["Uppercase Letters"] = "Прописные буквы" #Uppercase Letters
d["Word Builder"] = "Словопостроитель" #Word Builder
d["Word Maze"] = "Словесный лабиринт" #Word Maze
d["Collect all"] = "Соберите все буквы в правильном порядке" #Collect all letters in the right order
d["Word Maze + 4"] = "Словесный лабиринт + 4" #Word Maze + 4
d["Numbers"] = "Числа" #Numbers
d["Number Flashcards"] = "Учусь числам по карточкам" #Learn Numbers with Flashcards
d["Learn to Count"] = "Учись считать" #Learn to Count
#d["Basic A n S"] = "Основы сложения и вычитания" #Basic Addition & Subtraction
d["Basic Addition"] = "Сложения"
d["Basic Subtraction"] = "Вычитания"
d["Shopping List"] = "Список покупок" #Shopping List
d["Plus or Minus"] = "Плюс или минус" #Plus or Minus
d["Basic Operations"] = "Основные операции" #Basic Operations
d["Multiplication Table"] = "Таблица умножения" #Multiplication Table
d["Find the product"] = "Найти произведение" #Find the product
d["Find the multiplier"] = "Найти множитель" #Find the multiplier
d["Division"] = "Деление" #Division
d["Sorting Numbers"] = "Сортировка чисел" #Sorting Numbers
d["Number Comparison"] = "Сравнение чисел" #Number Comparison
d["Addition & Subtraction"] = "Сложение и вычитание" #Addition & Subtraction
d["Comparison"] = "Сравнение" #Comparison
d["Fractions"] = "Обыкновенные дроби" #"Фракции" #Fractions
d["Decimal Fractions"] = "Десятичные дроби" #Decimal Fractions
d["Even or Odd"] = "Четные или Нечетные числа"#"Чет или нечет" #Even or Odd
d["Shapes"] = "Формы" #Shapes
d["Shape Flashcards"] = "Учусь геометрическим фигурам" #Learn Shapes with Flashcards
d["Solids"] = "геометрическое телa"#"Твердые" #Solids
d["Solid Flashcards"] = "пространственная геометрия" #Solid Geometry with Flashcards
d["Shape Matching"] = "Сравнение форм" #Shape Matching
d["help me find my shadow"] = "помогите мне найти мою тень" #help me find my shadow
d["Paint"] = "Красить" #Paint
d["Colour Matching"] = "Соответствие цветов" #Colour Matching
d["label the colours"] = "Названия цветов" #label the colours
d["Follow the Arrows"] = "Следуйте стрелки" #Follow the Arrows
d["remember the directions"] = "запоминайте направления" #remember the directions
d["Photographic Memory"] = "Фотографическая память" #Photographic Memory
d["Training"] = "Обучение" #Training
d["Photographic Memory"] = "Фотографическая память" #Photographic Memory
d["Automatic Levels"] = "Автоматические уровни" #Automatic Levels
d["Mouse Maze"] = "Мышиный лабиринт" #Mouse Maze
d["Let's have some cheese"] = "Давайте немного сыра" #Let's have some cheese
d["Sheep Maze"] = "Овечий лабиринт" #Sheep Maze
d["Find the rest"] = "Найти остальное стадо" #Find the rest of the herd
d["Connect"] = "Соединиться" #Connect
d["Balloons with threads"] = "Воздушные шары с потоками" #Balloons with threads
d["Fifteen"] = "Пятнадцать" #Fifteen
d["With a Twist"] = "С Завихрением" #With a Twist
				
#game instructions				
d["Drag the slider"] = ["Перетащите ползунок вверх или вниз так,","чтобы правильный знак оказался в красном квадрате."] #Drag the slider up or down so that the right sign is in the red square.
d["Take your sheep"] = "Приведите овцу к остальному стаду." #Take your sheep to the rest of the herd.
d["Check the shopping list"] = "Проверьте Список покупок и перетащите все необходимые предметы в корзину." #Check the shopping list and drag all needed items into the basket.
d["Drag lt"] = ["Перетащите один из <,> или = (меньше, больше или равно)","на красный квадрат."] #Drag one of the <, > or  = (greater, lesser or equal) to the red square.
d["Drag lt2"] = "Перетащите один из меньше, больше или равно в красный квадрат." #Drag one of the greater, lesser or equal to the red square.
d["Re-arrange right"] = "Переставьте выше цифры, чтобы они были в правильном порядке" #Re-arrange the above numbers so they are in the right order
d["Complete abc"] = "Заполните алфавит с помощью букв выше." #Complete the abc using the letters above.
d["Write a word:"] = "Напишите слово:" #Write a word:
d["Find and separate"] = "Найдите и отделите четные числа от нечетных чисел в указанной последовательности." #Find and separate the Even Numbers form the Odd Numbers in the above series.
d["Re-arrange alphabetical"] = "Переставьте буквами, чтобы они были в алфавитном порядке." #Re-arrange the above letters so they are in the alphabetical order.
d["Re-arrange ascending"] = "Переставьте цифры, чтобы они были в порядке возрастания." #Re-arrange the above numbers so they are in the ascending order.
				
#game dialogs				
d["Please try again."] = "Пожалуйста, попробуйте еще раз." #Please try again.
d["Sorry! It is wrong."] = "Извините! Это неправильно." #Sorry! It is wrong.
d["Perfect! Task solved!"] = "Великолепно! Задача решена!" #Perfect! Task solved!
d["work harder"] = "Вы должны работать немного усерднее в следующий раз." #You need to work a little bit harder next time.
				
#level_controller				
d["Game Over!"] = "Игра проиграна!" #Game Over!
d["Congratulations! Game Completed."] = "Поздравляем! Вы выполнили все задачи в этой игре." #Congratulations! You have completed all tasks in this game.
d["Great job!"] = ["Отличная работа!"] #["Great job!","Perfect!","Awesome!","Fantastic job!","Well done!"]

d["Perfect! Level completed!"] = "Великолепно! Уровень завершен!" #Perfect! Level completed!
				
#game specific labels:				
d["area:"] = "площадь:" #area:
d["circumference:"] = "окружности:" #circumference:
d["perimeter:"] ="окружности:"
d["surface area:"] = "площадь поверхности" #surface area:
d["volume:"] = "объем" #volume:
d["Perfect!"] = "Великолепно!" #Perfect!
d["divided by"] = "деленное на"#"деленный(ая) на" #divided by
d["multiplied by"] = "умноженное на" #"умноженный(ая) раз" #times
d["equals"] = "равно" #equals
d["Shopping List"] = "Список покупок" #Shopping List
d["Even"] = "Четные"# числа" #"Чет" #Even 
d["Odd"] = "Нечетные"# числа" #"Нечет" #Odd
d["white"] = "Белый" #"white"
d["black"] = "Черный" #"black"
d["grey"] = "Серый" #"grey"
d["red"] = "Красный" #"red"
d["orange"] = "Оранжевый" #"orange"
d["yellow"] = "Желтый" #"yellow"
d["olive"] = "Оливковый" #"olive"
d["green"] = "Зеленые" #"green"
d["sea green"] = "Цвета морской волны" #"sea green"
d["teal"] = "Чирок" #"teal"
d["blue"] = "Синий" #"blue"
d["navy"] = "Темно-синий" #"navy"
d["purple"] = "сиреневый" #"purple"
d["violet"] = "Фиолетовый" #"violet"
d["magenta"] = "пурпурный" #"magenta"
d["indigo"] = "Индиго" #"indigo"
d["pink"] = "Розовый" #"pink"
d["maroon"] = "темно-бордовый" #maroon
d["brown"] = "коричневый" #brown
d["aqua"] = "голубой" #aqua
d["lime"] = "лайм" #lime
				
#new				
d["Keyboard Skills"] = "Радужная клавиатура" #Rainbow Keyboard
d["Touch Typing"] = "Обучение слепой печати" #Touch Typing Training
d["Translators"] = "Переводчики" #Translators
d["English Alphabet"] = "Английский алфавит" #English Alphabet
d["Your Alphabet"] = "Русский алфавит" #Russian Alphabet


#new in 0.3.0
d["Paint Mixer"] = "Mixing Colours for Painting"
d["Mixing RYB"] = "Mix red, yellow, blue, black and white paint"

d["Light Mixer"] = "Additive Colour Mixing - Light"
d["Mixing RGB"] = "Mix red, green and blue light to get other colours"

d["Ink Mixer"] = "Subtractive Colour Mixing - Paints, Dyes, Inks"
d["Mixing CMY"] = "Mix cyan, magenta and yellow paint to get other colours"

d["Find the colour of the circle"] = "Find the colour of the circle"
d["Adjust CMY"] = "Adjust the amount of cyan, magenta and yellow paint"
d["Adjust RGB"] = "Adjust the intensity of red, green and blue light"

#the following is used by colour matching games in spoken hints
#ie. "more red, less green, blue is ok"
d["more color"] = "more"
d["less color"] = "less"
d["color is ok"] = "is ok"
#in some languages to keep the colours gramaticaly correct 
#the ie. red will be a different word in "more red" and "red is ok"
#ie. in Polish "więcej czerwonego" and "czerwony jest ok"
#and in the following 2 element lists first element is used with more, less,
#and the second with the "is ok" - in most languages those will be the same, but not in Polish or Russian
d["of red"] = ["red","red"]
d["of green"] = ["green","green"]
d["of blue"] = ["blue","blue"]
d["of cyan"] = ["cyan","cyan"]
d["of magenta"] = ["magenta","magenta"]
d["of yellow"] = ["yellow","yellow"]

#new in 0.3.1
d["brush size"] = "brush size"

#new in 0.3.2
d["TicTacToe2"] = "Tic Tac Toe 2"
d["TicTacToe3"] = "Tic Tac Toe 3"
d["multiline-tictactoe"] = "Get as many lines of 3 as possible to win"


d["Player"] = "Player"
d["Won"] = "Won"
d["Game Draw"] = "Draw"
d["UserName"] = "User Name"

d["Match Animals Memory"] = "Match Animals"
d["Match Fruits"] = "Match Fruits"
d["Match Vegetables"] = "Match Vegetables"
d["Match Numbers"] = "Match Numbers"
d["Find pairs"] = "Find matching pairs of the same image"

d["Sliced Images"] = "Sliced Images"
d["Sliced Animals"] = "Animals"
d["Sliced Fruits"] = "Fruits"
d["Sliced Numbers"] = "Numbers"

d["Fraction Groups"] = "Fraction Groups"
d["Percentages"] = "Percentages"
d["Ratios"] = "Ratios"
d["Fract instr0"] = "Match fraction charts on the right to the ones on the left"
d["Fract instr1"] = ["Match fraction charts and fractions on the right","to the fraction charts on the left"]
d["Fract instr2"] = "Match fraction charts to the fractions on the left"
d["Fract instr3"] = ["Match fraction charts, fractions and decimal fractions on the right","to their percentage representations"]
d["Fract instr4"] = ["Match charts to the ratios on the left","Ratios are expressed as ratio of coloured pieces to white pieces"]

d["Maths Matching Game"] = "Maths Matching Game"
d["Addition"] = "Addition"
d["Subtraction"] = "Subtraction"
d["Multiplication"] = "Multiplication"
d["Division"] = "Division"

d["Check for newer version..."] = ["","Check for newer version, report bugs, discuss, translate or review this project at:"]
d["Match numbers to their spelling"] = "Match numbers to their spelling"
d["Number Spelling"] = "Number Spelling"

d["Match Animals"] = "Match Animals"
d["Find all matching animals"] = "Find all matching animals"
d["Match animals to their shadows"] = "Match animals to their shadows"

d["ShapeMaker"] = "Shape Maker"

d["draw_instr1"] = "Shape to draw: %s"
d["draw_instr2"] = "Shape to draw: %s" #if the following size_instr turn out to be too long the beginning can be moved here, ie. d["draw_instr2"] = "Shape to draw: %s, such that" 

d["size_instr_0"] = "such that lengths of its bases are equal to %d and %d and height to %d" #for trapeziums
d["size_instr_1"] = "such that lengths of its sides are equal to %d" #square
d["size_instr_2"] = "such that lengths of its sides are equal to %d and %d" #rectangle
d["size_instr_3"] = "such that lengths of its 2 parallel bases are equal to %d and height to %d" #for parallelogram
d["size_instr_4"] = "such that length of its base is equal to %d and height to %d" #for triangles incl. isosceles triangles
d["size_instr_5"] = "such that lengths of its catheti are equal to %d and %d" #for right triangles
d["size_instr_6"] = "such that lengths of both of its catheti are equal to %d" #for right isosceles triangles
d["size_instr_7"] = "such that length of its hypotenuse is equal to %d" #for right isosceles triangles
d["size_instr_8"] = "such that length of one of its sides is equal to %d and height to %d" #for obtuse triangles
d["size_instr_9"] = "such that length of its radius is equal to %d" #for circles

d["square"] = shape_names[5]
d["rectangle"] = shape_names[6]
d["right_trapezium"] = shape_names[7]
d["iso_trapezium"] = shape_names[8] 
d["rhombus"] = shape_names[9]
d["parallelogram"] = shape_names[10]
d["quadrilateral"] = "Четырёхугольник"
d["trapezium"] = "Трапеция"
d["u_trapezium"] = "Трапеция"
d["triangle"] = "Треугольник"

d["squished_quadi"] = "Сплющенные четырехугольник"

d["equi_tria"] = shape_names[0]
d["iso_tria"] = shape_names[1]
d["obtuse_tria"] = shape_names[2]
d["right_tria"] = shape_names[3]
d["acute_tria"] = shape_names[4]
d["right_iso_tria"] = "Right isosceles triangle"
d["obtuse_iso_tria"] = "Obtuse isosceles triangle"
d["acute_iso_tria"] = "Acute isosceles triangle"
d["squished_tria"] = "Ouch... squished triangle" #used to label a drawn "triangle" with angles: 0º, 180º, 0º - all points on one line
d["circle"] = shape_names[13]
d["triangle_not_really"] = "Triangle? Well, not really..." #used to label a drawn "quadrilateral" with one of its angles equal to 180º - in effect making it look like triangle

d["test_yourself"] = "Test yourself"
d["Clock1"] = "Clock"
d["Read time"] = "learn to read the time"
d["Clock2"] = "Clock"
d["Set time"] = "learn to set the clock"
d["Set_clock"] = "Set the clock to:"
d["Set_clock_instr"] = ["","Drag the clock hands","to set the time"]
d["What time"] = "What time is it?"
d["close_confirm"] = "Нажмите еще раз для выхода"
d["answer_enter"] = "Type your answer and hit enter"

d["enable_untranslated"] = "FAO: Translators - enable this to show untranslated languages (for testing):"
d["Fullscreen:"] = "Fullscreen:"
d["Time"] = "Time"
d["Play_w_clock"] = "Turn the clock hands and see what happens."

d["lets_see_what_you_draw"] = "Let's see what shapes you can draw"
d["txt_only"] = "Time in text version only"
d["Clock0"] = "How clock works?"

d["Columnar addition"] = "Columnar addition"
d["Columnar subtraction"] = "Columnar subtraction"
d["Long multiplication"] = "Long multiplication"
d["Long division"] = "Long division"
d["borrow 10"] = "borrow 10"
d["carry"] = "carry" #in columnar addition, ie. in case of 4 + 8 you write 2 under the column and carry 1
d["demo start"] = "Start >>"
d["demo next eg"] = "Next example >>"
d["demo next step"] = "Next step >>"
d["demo write"] = "write " #used to show which digit of the result should be entered in a box, ie. "enter 5"
d["Demonstration"] = "Demonstration"
d["DIY"] = "Do it yourself"
d["Ratio"] = "Ratio"
d["Working with large numbers"] = "Working with large numbers"
d["demo rewrite"] = "rewrite "
d["remainder"] = "remainder"
d["demo_result"] = "result"
d["TimeMatching"] = "Time Matching"