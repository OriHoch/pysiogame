# -*- coding: utf-8 -*-

# traduzido para português da europa por Américo Monteiro (a_monteiro@gmx.com)

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
shape_names = ["Triângulo Equilátero", "Triângulo Isósceles", "Triângulo Obtuso", "Triângulo Rectângulo", "Triângulo Agudo", "Quadrado", "Rectângulo", "Trapézio Rectângulo", "Trapézio Isósceles", "Losango", "Paralelograma", "Pentágono", "Hexágono", "Círculo", "Elipse"]
#solid_names = ["Cube", "Square Prism", "Triangular Prism", "Square Pyramid", "Triangular Pyramid", "Sphere", "Cylinder", "Cone", "Torus"]
solid_names = ["Cubo", "Prisma Quadrado", "Prisma Triangular", "Pirâmide Quadrada", "Pirâmide Triangular", "Esfera", "Cilindro", "Cone", "Toro"]
#numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
#numbers2090 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
numbers = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte', 'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco', 'vinte e seis', 'vinte e sete', 'vinte e oito', 'vinte e nove']
numbers2090 = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']

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
    return ""
           
d['abc_flashcards_word_sequence'] = ['Abeto', 'Barco', 'Casa', 'Dormir','Elefante', 'Formiga', 'Girafa', 'Hipopótamo','Iglu', 'Janela','Koala', 'Leão', 'Maçã', 'Narciso-amarelo', 'Ouriço', 'Peixe', 'Queijo', 'Rainha', 'Sol', 'Tomate', 'Uvas', 'Violino', 'Windsurf', 'Xilofone', 'Y', 'Zebra']
d['abc_flashcards_frame_sequence'] = [31,1,7, 49,4,0,30, 47,8,22, 72,11,42, 69,29,5, 57,16,18,33,6,21, 66,23, 43,25]

#used in telling time activity
#the number lists below are for languages with a bit more complex forms, ie. different suffixes depending on context - if your language is like that check Polish translation to see how to use them
d["minute_numbers_1to29"] = numbers[:]
#last digit when joining numbers of minutes

#hours case 0: full hour, ie. one o'clock, two o'clock, etc.
#d["hours_a"] = numbers[0:12]
d["hours_a"] = ['uma hora', 'duas horas', 'três horas', 'quatro horas', 'cinco horas', 'seis horas', 'sete horas', 'oito horas', 'nove horas', 'dez horas', 'onze horas', 'doze horas']

#hours case 1: ie. ten past one, 22 past three, etc. 
d["hours_b"] = d["hours_a"][:]

#hours case 2: ie. ten to one, 22 to three, etc.
d["hours_c"] = d["hours_a"][:]

d["time_string_one_to"] = "um minuto para %s"
d["time_string_one_past"] = "%s e um minuto"
#d["time_string_to_mh"] = "%s para %s" #ie. five to four
#d["time_string_past_mh"] = "%s depois das %s" #ie. five past four
#d["time_string_to_hm"] = "%s menos %s" #ie. 3:55 = four o'clock in five
#d["time_string_past_hm"] = "%s e %s" #ie. 4:05 = four and five minutes
d["time_string_to_mh"] = "%s minutos para %s" #ie. five to four
d["time_string_past_mh"] = "" #ie. five past four
d["time_string_to_hm"] = "" #ie. 3:55 = four o'clock in five
d["time_string_past_hm"] = "%s e %s minutos" #ie. 4:05 = four and five minutes
#if you never use the "to the hour" form leave the above fields blank and only fill one of the following two
d["time_string_1_59_past_mh"] = "" 
d["time_string_1_59_past_hm"] = ""
d["time_string_3q_past"] = "" #if you don't use quarter to but rather past use this one to either say it's 3 quarters past or 45 past - and leave the "quarter to" field blanck

d["time_string_half_to"] = "" #ie. in languages using this form, ie. half to four
d["time_string_half_past"] = "%s e meia" #ie. half past three
d["time_string_q_to"] = "um quarto para %s"
d["time_string_q_past"] = "%s e um quarto"
d["time_string_full"] = "%s em ponto"

fruit = ["maçã verde", "maçã vermelha", "morango", "pêra", "laranja", "cebola", "tomate", "limão", "cereja", "pimentão", "cenoura", "banana", "melancia"]    
fruits_1 = ["maçãs verdes", "maçãs vermelhas", "morangos", "pêras", "laranjas", "cebolas", "tomates", "limões", "cerejas", "pimentões", "cenouras", "bananas", "melancias"]     
fruits_2 = []
#[[for this number of fruits (in range of 2-7) use names from fruits_1],[and for those from fruits_2]]
plural_rules = [[2,3,4,5,6,7],[]] #used for some languages where there are more than one form for plurals depending on number

#alphabet - pt - "abcdefghijlmnopqrstuvxz"
alphabet_lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['á','â','ã','à','ç','é','ê','í','ó','ô','õ','ú','-']
accents_uc = ['Á','Â','Ã','À','Ç','É','Ê','Í','Ó','Ô','Õ','Ú']


#game start
d["Hello"] = "Olá"
d["Welcome back."] = "Bem vindo de volta ao jogo."

#settings
d["Preferences"] = "Preferências"
d["Language"] = "Linguagem"
d["Reader"] = "Utilizar programa eSpeak"
d["Read Instructions"] = "Ler as Instruções no inicio dos jogos"

#menu categories
d["Info Category"] = "Informação & Definições"
d["Keyboard & Mouse"] = "Teclado & Rato"
d["Discover Letters"] = "Descobrir Letras"
d["Learn Words"] = "Aprender Palavras Novas"
d["Maths"] = "Matemáticas"
d["Numbers & Basic Operations"] = "Números & Operações Básicas"
d["Basic Operations - exercises"] = "Operações Básicas - Exercícios"
d["Sorting and Comparing"] = "Organizar e Comparar"
d["Geometry"] = "Geometria e Reconhecimento de Formas"
d["Art"] = "Arte e Cor"
d["Memory"] = "Memória"
d["Games & Mazes"] = "Jogos & Labirintos"
d["Multiplayer"] = "Jogos de Vários Jogadores"

#games
d["About."] = "Sobre."
d["Game info..."] = "Informação do Jogo..."
d["Credits"] = "Copyright & Créditos"
d["Hit the Mole"] = "Acerta na Toupeira"
d["Letters"] = "Letras"
d["Letter Flashcards"] = "Aprende Letras com Figuras"
d["Learn to Write"] = "Aprende a Escrever"
d["Trace Letters"] = "Traça Letras e Números"
d["Complete the ABC"] = "Completa o ABC"
d["English"] = "Inglês"
d["in your language"] = "Português"
d["Sorting Letters"] = "Ordenar Letras"
d["Lowercase Letters"] = "Letras Minúsculas"
d["Uppercase Letters"] = "Letras Maiúsculas"
d["Word Builder"] = "Compositor de Palavras"
d["Word Maze"] = "Labirinto de Palavras"
d["Collect all"] = "Recolhe todas as letras na ordem certa"
d["Word Maze + 4"] = "Labirinto de Palavras + 4"
d["Numbers"] = "Números"
d["Number Flashcards"] = "Aprende Números com Figuras"
d["Learn to Count"] = "Aprende a Contar"
d["Basic Addition"] = "Adição Básica"
d["Basic Subtraction"] = "Subtração Básica"
d["Shopping List"] = "lista de Compras"
d["Plus or Minus"] = "Mais ou Menos"
d["Basic Operations"] = "Operações Básicas"
d["Multiplication Table"] = "Tabela de Multiplicação"
d["Find the product"] = "Encontra o produto"
d["Find the multiplier"] = "Encontra o multiplicador"
d["Division"] = "Divisão"
d["Sorting Numbers"] = "Ordenar Números"
d["Number Comparison"] = "Comparação de Números"
d["Addition & Subtraction"] = "Adição & Subtração"
d["Comparison"] = "Comparação"
d["Fractions"] = "Frações"
d["Decimal Fractions"] = "Frações Decimais"
d["Even or Odd"] = "Par ou Ímpar"
d["Shapes"] = "Formas"
d["Shape Flashcards"] = "Aprende Formas com Figuras"
d["Solids"] = "Sólidos"
d["Solid Flashcards"] = "Aprende Geometrias Sólidas com Figuras"
d["Shape Matching"] = "Correspondência de Formas"
d["help me find my shadow"] = "ajuda-me a encontrar a minha sombra"
d["Paint"] = "Pintura"
d["Colour Matching"] = "Correspondência de Cores"
d["label the colours"] = "nomeia as cores"
d["Follow the Arrows"] = "Segue as Setas"
d["remember the directions"] = "lembra as direções"
d["Photographic Memory"] = "Memória Fotográfica"
d["Training"] = "Treinar"
d["Photographic Memory"] = "Memória Fotográfica"
d["Automatic Levels"] = "Níveis Automáticos"
d["Mouse Maze"] = "Labirinto do Rato"
d["Let's have some cheese"] = "Vamos apanhar o queijo"
d["Sheep Maze"] = "Labirinto da Ovelha"
d["Find the rest"] = "Encontra o resto do rebanho"
d["Connect"] = "Liga"
d["Balloons with threads"] = "Balões com rolos de fio"
d["Fifteen"] = "Jogo Puzzle dos Quinze"
d["With a Twist"] = "Troca as Posições das Peças"

#game instructions
d["Drag the slider"] = ["Arrasta os sinais para cima ou para baixo","para que o sinal certo fique no quadrado certo"] #"Drag the slider up or down so that the right sign is in the red square."
d["Take your sheep"] = "Leva a tua ovelha para o resto do rebanho." #"Take your sheep to the rest of the herd."
d["Check the shopping list"] = "Consulta a lista de compras e arrasta todas as coisas que precisas para o cesto" #"Check the shopping list and drag all needed items into the basket."
d["Drag lt"] = "Arrasta um dos <, > ou = (menor, maior ou igual) para o quadrado vermelho." #"Drag one of the <, > or = (lesser, greater or equal) to the red square."
d["Drag lt2"] = "Arrasta um dos menor, maior ou igual para o quadrado vermelho." #"Drag one of the lesser, greater or equal to the red square."
d["Re-arrange right"] = "Organiza os números em cima para que fiquem na ordem certa." #"Re-arrange the above numbers so they are in the right order"
d["Complete abc"] = "Completa o abecedário usando as letras em cima." #"Complete the abc using the letters above."
d["Write a word:"] = "Escreve uma palavra." #"Write a word:"
d["Find and separate"] = "Encontra e separa os Números Pares dos Ímpares nas séries em cima." #"Find and separate the Even Numbers form the Odd Numbers in the above series."
d["Re-arrange alphabetical"] = "Organiza as letras em cima para que fiquem em ordem alfabética" #"Re-arrange the above letters so they are in the alphabetical order."
d["Re-arrange ascending"] = "Organiza os números em cima para que fiquem em ordem crescente." #"Re-arrange the above numbers so they are in the ascending order."

#game dialogs
d["Please try again."] = "Por favor tenta outra vez." #"Please try again."
d["Sorry! It is wrong."] = "Desculpa mas está errado." #"Sorry! It is wrong."
d["Perfect! Task solved!"] = "Perfeito! Tarefa resolvida!" #"Perfect! Task solved!"
d["work harder"] = "Precisas de te esforçar um pouco mais na próxima vez." #"You need to work a little bit harder next time."

#level_controller
d["Game Over!"] = "Fim de Jogo!" #"Game Over!"
d["Congratulations! Game Completed."] = "Parabéns! Conseguiste completar todas as tarefas deste jogo." #"Congratulations! You have completed all tasks in this game."
d["Great job!"] = ["Bom trabalho!","Perfeito!","Maravilhoso!","Super!","Muito Bem!"] #["Great job!","Perfect!","Awesome!","Super!","Well done!"]
d["Perfect! Level completed!"] = "Perfeito! Nível completo!" #"Perfect! Level completed!"

#game specific labels:
d["area:"] = "área:"
d["perimeter:"] = "perímetro:"
d["surface area:"] = "área de superfície:"
d["volume:"] = "volume:"
d["Perfect!"] = "Perfeito!"
d["divided by"] = "a dividir por"
d["multiplied by"] = "vezes"
d["equals"] = "igual"
d["Shopping List"] = "Lista de Compras"
d["Even"] = "Par"
d["Odd"] = "Ímpar"
d["white"]="branco"
d["black"]="preto"
d["grey"]="cinzento"
d["red"]="vermelho"
d["orange"]="laranja"
d["yellow"]="amarelo"
d["olive"]="verde azeitona"
d["green"]="verde"
d["sea green"]="verde mar"
d["teal"]="azul petróleo"
d["blue"]="azul"
d["navy"]="azul marinha"
d["purple"]="púrpura"
d["violet"]="violeta"
d["magenta"]="magenta"
d["indigo"]="índigo"
d["pink"]="rosa"
d["maroon"] = ["castanho-","avermelhado"]
d["brown"] = "castanho"
d["aqua"] = "azul ciano"
d["lime"] = "lima"

#new
d["Keyboard Skills"] = "Teclado Colorido" #"Rainbow Keyboard"
d["Touch Typing"] = "Instrutor de Escrita em Teclado" #"Touch Typing Tutor"
d["Translators"] = "Tradutores" #"Translators"
d["English Alphabet"] = "Alfabeto Inglês" #"English Alphabet"
d["Your Alphabet"] = "Alfabeto Português" #"Portuguese Alphabet"

#new in 0.3.0
d["Paint Mixer"] = "Misturar Cores para Pintar" #"Mixing Colours for Painting"
d["Mixing RYB"] = "Mistura tintas vermelha, amarela, azul, preta e branca" #"Mix red, yellow, blue, black and white paint"

d["Light Mixer"] = "Mistura de Cores Aditiva - Luz Colorida" #"Additive Colour Mixing - Light"
d["Mixing RGB"] = "Mistura as cores da luz vermelha, verde e azul para obter outras cores" #"Mix red, green and blue light to get other colours"

d["Ink Mixer"] = "Mistura de Cores Subtractiva - Bases e Corantes" #"Subtractive Colour Mixing - Paints, Dyes, Inks"
d["Mixing CMY"] = "Mistura ciano, magenta e amarelo para obter outras cores" #"Mix cyan, magenta and yellow paint to get other colours"

d["Find the colour of the circle"] = "Encontra a cor do círculo" #"Find the colour of the circle"
d["Adjust CMY"] = "Ajusta a quantidade das tintas ciano, magenta e amarelo" #"Adjust the amount of cyan, magenta and yellow paint"
d["Adjust RGB"] = "Ajusta a intencidade das luzes vermelha, verde e azul" #"Adjust the intensity of red, green and blue light"

#the following is used by colour matching games in spoken hints
#ie. "more red, less green, blue is ok"
d["more color"] = "mais"
d["less color"] = "menos"
d["color is ok"] = "está certo"
#in some languages to keep the colours gramaticaly correct 
#the ie. red will be a different word in "more red" and "red is ok"
#ie. in Polish "więcej czerwonego" and "czerwony jest ok"
#and in the following 2 element lists first element is used with more, less,
#and the second with the "is ok" - in most languages those will be the same, but not in Polish or Russian
d["of red"] = ["vermelho","vermelho"]
d["of green"] = ["verde","verde"]
d["of blue"] = ["azul","azul"]
d["of cyan"] = ["ciano","ciano"]
d["of magenta"] = ["magenta","magenta"]
d["of yellow"] = ["amarelo","amarelo"]

#new in 0.3.1
d["brush size"] = "tamanho do pincel"

#new in 0.3.2
d["TicTacToe2"] = "Jogo do Galo para 2 Jogadores" #"Tic Tac Toe 2"
d["TicTacToe3"] = "Jogo do Galo para 3 Jogadores" #"Tic Tac Toe 3"
d["multiline-tictactoe"] = "Ganha quem fizer mais linhas de 3 seguidos" #"Get as many lines of 3 as possible to win"


d["Player"] = "Jogador"
d["Won"] = "Venceu"
d["Game Draw"] = "Empate"
d["UserName"] = "Nome de Utilizador"

d["Match Animals Memory"] = "Animais que Correspondem"
d["Match Fruits"] = "Frutas que Correspondem"
d["Match Vegetables"] = "Vegetais que Correspondem"
d["Match Numbers"] = "Números que Correspondem"
d["Find pairs"] = "Encontra pares correspondentes da mesma imagem" #"Find matching pairs of the same image"

d["Sliced Images"] = "Imagens Baralhadas" #"Sliced Images"
d["Sliced Animals"] = "Animais"
d["Sliced Fruits"] = "Frutas"
d["Sliced Numbers"] = "Números"

d["Fraction Groups"] = "Grupos de Frações"
d["Percentages"] = "Percentagens"
d["Ratios"] = "Relações"
d["Fract instr0"] = "Corresponde os mapas de frações da direita com os da esquerda" #"Match fraction charts on the right to the ones on the left"
d["Fract instr1"] = ["Corresponde os mapas de frações e as frações da direita","com os mapas de frações da esquerda"] #["Match fraction charts and fractions on the right","to the fraction charts on the left"]
d["Fract instr2"] = "Corresponde os mapas de frações com as frações da esquera" #"Match fraction charts to the fractions on the left"
d["Fract instr3"] = ["Corresponde os mapas de frações, frações e frações decimais da direita","com as suas representações de percentagem"] #["Match fraction charts, fractions and decimal fractions on the right","to their percentage representations"]
d["Fract instr4"] = ["Corresponde os mapas com as relações da esquerda","As relações são expressadas na diferença entre peças coloridas e peças brancas"] #["Match charts to the ratios on the left","Ratios are expressed as ratio of coloured pieces to white pieces"]

d["Maths Matching Game"] = "Jogo de Correspondências Matemáticas" #"Maths Matching Game"
d["Addition"] = "Adição"
d["Subtraction"] = "Subtração"
d["Multiplication"] = "Multiplicação"
d["Division"] = "Divisão"

d["Check for newer version..."] = ["Verifique novas versões, reporte erros, discuta, traduza ou reveja este projecto em:"] #["","Check for newer version, report bugs, discuss, translate or review this project at:"]
d["Match numbers to their spelling"] = "Corresponder números com a sua ortografia" #"Match numbers to their spelling"
d["Number Spelling"] = "Ortografia de Números" #"Number Spelling"

d["Match Animals"] = "Correspondência de Animais" #"Match Animals"
d["Find all matching animals"] = "Encontra todos os animais correspondentes" #"Find all matching animals"
d["Match animals to their shadows"] = "Corresponde os animais com as suas sombras" #"Match animals to their shadows"

d["ShapeMaker"] = "Criador de Formas" #"Shape Maker"

d["draw_instr1"] = "Forma a desenhar: %s"
d["draw_instr2"] = "Forma a desenhar: %s de modo que " #if the following size_instr turn out to be too long the beginning can be moved here, ie. d["draw_instr2"] = "Shape to draw: %s, such that" 

d["size_instr_0"] = "os comprimentos das suas bases sejam iguais a %d e %d e a altura a %d" #"such that lengths of its bases are equal to %d and %d and height to %d" #for trapeziums
d["size_instr_1"] = "os comprimentos dos seus lados sejam iguais a %d" #"such that lengths of its sides are equal to %d" #square
d["size_instr_2"] = "os comprimentos dos seus lados sejam iguais a %d e %d" #"such that lengths of its sides are equal to %d and %d" #rectangle
d["size_instr_3"] = "os comprimentos das suas 2 bases paralelas sejam iguais a %d e a altura igual a %d" #"such that lengths of its 2 parallel bases are equal to %d and height to %d" #for parallelogram
d["size_instr_4"] = "o comprimento seja igual a %d e a altura a %d" #"such that length of its base is equal to %d and height to %d" #for triangles incl. isosceles triangles
d["size_instr_5"] = "os comprimentos dos catetos sejam iguais a %d e %d" #"such that lengths of its catheti are equal to %d and %d" #for right triangles
d["size_instr_6"] = "os comprimentos de ambos catetos sejam iguai a %d" #"such that lengths of both of its catheti are equal to %d" #for right isosceles triangles
d["size_instr_7"] = "o comprimento da hipotenusa seja igual a %d" #"such that length of its hypotenuse is equal to %d" #for right isosceles triangles
d["size_instr_8"] = "o comprimento de um dos lados seja igual a %d e a altura igual a %d" #"such that length of one of its sides is equal to %d and height to %d" #for obtuse triangles
d["size_instr_9"] = "o comprimento do seu raio seja igual a %d" #"such that length of its radius is equal to %d" #for circles

d["square"] = shape_names[5]
d["rectangle"] = shape_names[6]
d["right_trapezium"] = shape_names[7] 
d["iso_trapezium"] = shape_names[8] 
d["rhombus"] = shape_names[9] 
d["parallelogram"] = shape_names[10] 
d["quadrilateral"] = "Quadrilátero"
d["trapezium"] = "Trapézio"
d["u_trapezium"] = "Trapézio"
d["triangle"] = "Triângulo"
d["squished_quadi"] = "Auuu... um quadrilátero esmagado" #used to label a drawn "quadrilateral" with angles: 0º, 180º, 0º, 180º - all points on one line

d["equi_tria"] = shape_names[0]
d["iso_tria"] = shape_names[1]
d["obtuse_tria"] = shape_names[2]
d["right_tria"] = shape_names[3]
d["acute_tria"] = shape_names[4]
d["right_iso_tria"] = "Triângulo isósceles rectângulo"
d["obtuse_iso_tria"] = "Triângulo isósceles obtuso"
d["acute_iso_tria"] = "Triângulo isósceles agudo"
d["squished_tria"] = "Auuu... triângulo esmagado" #used to label a drawn "triangle" with angles: 0º, 180º, 0º - all points on one line
d["circle"] = shape_names[13]
d["triangle_not_really"] = "Triângulo? Bem, nem por isso..." #"Triangle? Well, not really..." #used to label a drawn "quadrilateral" with one of its angles equal to 180º - in effect making it look like triangle

d["test_yourself"] = "Agora faz tu"
d["Clock1"] = "Relógio"
d["Read time"] = "aprende a ler as horas"
d["Clock2"] = "Relógio"
d["Set time"] = "aprende a acertar o relógio"
d["Set_clock"] = "Acerta o relógio para:"
d["Set_clock_instr"] = ["","Arrasta os ponteiros do relógio","para acertar as horas"]
d["What time"] = "Que horas são?"
d["close_confirm"] = "Clica outra vez para sair"
d["answer_enter"] = "Escreve a tua resposta e carrega no enter"

d["enable_untranslated"] = "FAO: Tradutores - activar para mostrar linguagens não traduzidas (para testes):" #enable this to show untranslated languages (for testing):"
d["Fullscreen:"] = "Écran completo:"
d["Time"] = "Horas"
d["Play_w_clock"] = "Roda os ponteiros do relógio para veres o que acontece."


d["lets_see_what_you_draw"] = "Vamos ver que formas consegues desenhar" #"Let's see what shapes you can draw"
d["txt_only"] = "Com as horas apenas em texto" #"Time in text version only"
d["Clock0"] = "Como é que funciona o relógio?" #"How clock works?"
d["Columnar addition"] = "Adição em colunas" #"Columnar addition"
d["Columnar subtraction"] = "Subtração em colunas" #"Columnar subtraction"
d["Long multiplication"] = "Multiplicação longa" #"Long multiplication"
d["Long division"] = "Divisão longa" #"Long division"
d["borrow 10"] = "pede 10 emprestado" #"borrow 10"
d["carry"] = "e vai " #in columnar addition, ie. in case of 4 + 8 you write 2 under the column and carry 1
d["demo start"] = "Começar >>"
d["demo next eg"] = "Próximo exemplo >>"
d["demo next step"] = "Próximo passo >>"
d["demo write"] = "escreve " #used to show which digit of the result should be entered in a box, ie. "enter 5"
d["Demonstration"] = "Demonstração"
d["DIY"] = "Agora faz tu"
d["Ratio"] = "Relação"
d["Working with large numbers"] = "Trabalhar com números grandes" #"Working with large numbers"
d["demo rewrite"] = "escreve"
d["remainder"] = "resto"
d["demo_result"] = "resultado"
d["TimeMatching"] = "Correspondência de Relógios"