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
shape_names = ["Triángulo equilátero", "Triángulo isósceles", "Triángulo obtuso", "Triángulo rectángulo", "Triángulo agudo", "Cuadrado", "Rectángulo", "Trapecio rectángulo", "Trapecio isósceles", "Rombo", "Paralelogramo", "Pentágono", "Hexágono", "Círculo", "Elipse"]

solid_names = ["Cubo", "Prisma cuadrado", "Prisma triangular", "Pirámide de base cuadrada", "Pirámide de base triangular", "Esfera", "Cilindro", "Cono", "Toro"]
numbers = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce' , 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte', 'veintiuno','veintidós','veintitrés','veinticuatro','veinticinco','veintiséis','veintisiete','veintiocho','veintinueve']
numbers2090 = ['veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa']

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
                return [tens + " y ", ones]
            else:
                return tens + " y " + ones
    return ""
           
d['abc_flashcards_word_sequence'] = ['Abeto', 'Búho', 'Casa', 'Dormir','Elefante', 'Fortepiano', 'Gato','Hormiga', 'Iglú', 'Jirafa', 'Koala', 'Loro', 'Manzana', 'Narciso','Ñu','Océano','Pescado', 'Queso','Ratón', 'Sol', 'Tomate', 'Uvas', 'Violín','Wagon', 'Xilófono', 'Yoga','Zapatos']
d['abc_flashcards_frame_sequence'] = [31, 14, 7, 49,4,34, 2,0, 8, 30, 72,15, 42, 69, 70,52,5, 57,12,18, 33,6, 22, 58,23,32,60]

#used in telling time activity
#the number lists below are for languages with a bit more complex forms, ie. different suffixes depending on context - if your language is like that check Polish translation to see how to use them
d["minute_numbers_1to29"] = numbers[:]

#hours case 0: full hour, ie. one o'clock, two o'clock, etc.
d["hours_a"] = ['La una', 'Las dos', 'Las tres', 'Las cuatro', 'Las cinco', 'Las seis', 'Las siete', 'Las ocho', 'Las nueve', 'Las diez', 'Las once', 'Las doce']

#hours case 1: ie. ten past one, 22 past three, etc. 
d["hours_b"] = d["hours_a"][:]

#hours case 2: ie. ten to one, 22 to three, etc.
d["hours_c"] = d["hours_a"][:]

d["time_string_one_to"] = "%s menos un minuto"
d["time_string_one_past"] = "%s y un minuto"
d["time_string_to_mh"] = "" #ie. five to four
d["time_string_past_mh"] = "" #ie. five past four
d["time_string_to_hm"] = "%s menos %s" #ie. 3:55 = four o'clock in five
d["time_string_past_hm"] = "%s y %s" #ie. 4:05 = four and five minutes
d["time_string_half_to"] = "" #ie. in languages using this form, ie. half to four
d["time_string_half_past"] = "%s y media" #ie. half past three
#if you never use the "to the hour" form leave the above fields blank and only fill one of the following two
d["time_string_1_59_past_mh"] = "" 
d["time_string_1_59_past_hm"] = ""
d["time_string_3q_past"] = "" #if you don't use quarter to but rather past use this one to either say it's 3 quarters past or 45 past - and leave the "quarter to" field blanck

d["time_string_q_to"] = "%s menos cuarto"
d["time_string_q_past"] = "%s y cuarto"
d["time_string_full"] = "%s en punto"

fruit = ["manzana verde","manzana roja","fresa","pera","naranja","cebolla","tomate","limón","cereza","pimiento","zanahoria","plátano","sandía"]
fruits_1 = ["manzanas verdes","manzanas rojas","fresas","peras","naranjas","cebollas","tomates","limones","cerezas","pimientos","zanahorias","plátanos","sandías"]
fruits_2 = []
#[[for this number of fruits (in range of 2-7) use names from fruits_1],[and for those from fruits_2]]
plural_rules = [[2,3,4,5,6,7],[]] #used for some languages where there are more than one form for plurals depending on number

alphabet_lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['á','é','í','ó','ú','ü','-']
accents_uc = ['Á','É','Í','Ó','Ú','Ü']

#game start
d["Hello"] = "Hola"
d["Welcome back."] = "Te damos nuevamente la bienvenida a pysiogame."

#settings
d["Preferences"] = "Preferencias"
d["Language"] = "Idioma"
d["Reader"] = "eSpeak"
d["Read Instructions"] = "Lea las instrucciones en el inicio de los juegos"

#menu categories
d["Info Category"] = "Información y Ajustes"
d["Keyboard & Mouse"] = "Teclado y Ratón"
d["Discover Letters"] = "Descubre las letras"
d["Learn Words"] = "Aprende nuevas palabras"
d["Maths"] = "Matemáticas"
d["Numbers & Basic Operations"] = "Números y operaciones básicas"
d["Basic Operations - exercises"] = "Operaciones básicas - Ejercicios"
d["Sorting and Comparing"] = "Ordena y Compara"
d["Geometry"] = "Geometría y Formas"
d["Art"] = "Arte y Color"
d["Memory"] = "Memoria"
d["Games & Mazes"] = "Juegos y Laberintos"
d["Multiplayer"] = "Juegos multijugador"

#games
d["About."] = "Sobre pySioGame"
d["Game info..."] = "Información sobre el juego"
d["Credits"] = "Autoría y Créditos"
d["Hit the Mole"] = "Golpea al topo"
d["Letters"] = "Letras"
d["Letter Flashcards"] = "Aprende las letras con tarjetas didácticas"
d["Learn to Write"] = "Aprende a escribir"
d["Trace Letters"] = "Dibuja las letras y los números"
d["Complete the ABC"] = "Completa el abecedario"
d["English"] = "Inglés"
d["in your language"] = "Español"
d["Sorting Letters"] = "Ordenar letras"
d["Lowercase Letters"] = "Letras minúsculas"
d["Uppercase Letters"] = "Letras mayúsculas"
d["Word Builder"] = "Construye las palabras"
d["Word Maze"] = "Laberinto de palabras"
d["Collect all"] = "Recoge todas las letras en el orden correcto"
d["Word Maze + 4"] = "Laberinto de palabras + 4"
d["Numbers"] = "Números"
d["Number Flashcards"] = "Aprende los números con tarjetas didácticas"
d["Learn to Count"] = "Aprende a contar"
d["Basic Addition"] = "Suma básica"
d["Basic Subtraction"] = "Resta básica"
d["Shopping List"] = "Lista de la compra"
d["Plus or Minus"] = "Más o menos"
d["Basic Operations"] = "Operaciones básicas"
d["Multiplication Table"] = "Tabla de multiplicar"
d["Find the product"] = "Encuentra el producto"
d["Find the multiplier"] = "Encuentra el multiplicador"
d["Division"] = "División"
d["Sorting Numbers"] = "Ordena los números"
d["Number Comparison"] = "Compara los números"
d["Addition & Subtraction"] = "Suma y Resta"
d["Comparison"] = "Comparación"
d["Fractions"] = "Fracciones"
d["Decimal Fractions"] = "Fracciones decimales"
d["Even or Odd"] = "Par or Impar"
d["Shapes"] = "Formas"
d["Shape Flashcards"] = "Aprende las formas con tarjetas didácticas"
d["Solids"] = "Sólidos"
d["Solid Flashcards"] = "Aprende geometría de los sólidos con tarjetas didácticas"
d["Shape Matching"] = "Empareja las formas"
d["help me find my shadow"] = "ayúdame a encontrar mi sombra"
d["Paint"] = "Pinta"
d["Colour Matching"] = "Empareja los colores"
d["label the colours"] = "Etiqueta los colores"
d["Follow the Arrows"] = "Sigue las flechas"
d["remember the directions"] = "recuerda las direcciones"
d["Photographic Memory"] = "Memoria fotográfica"
d["Training"] = "Entrenamiento"
d["Photographic Memory"] = "Memoria fotográfica"
d["Automatic Levels"] = "Niveles automáticos"
d["Mouse Maze"] = "Laberinto del ratón"
d["Let's have some cheese"] = "Tomemos algo de queso"
d["Sheep Maze"] = "Laberinto de la oveja"
d["Find the rest"] = "Encuentra al resto del rebaño"
d["Connect"] = "Conecta"
d["Balloons with threads"] = "Globos con hilos"
d["Fifteen"] = "Quince"
d["With a Twist"] = "Con un giro"

#game instructions
d["Drag the slider"] = "Mueve arriba o abajo y pon el símbolo adecuado en el cuadrado rojo."
d["Take your sheep"] = "Lleva tu oveja hasta donde está el resto del rebaño."
d["Check the shopping list"] = "Comprueba la lista de la compra y arrastra dentro de la cesta todas las cosas necesarias."
d["Drag lt"] = "Arrastra hasta el cuadrado rojo: <, > ó = (menor, mayor, o igual que)."
d["Drag lt2"] = "Arrastra hasta el cuadrado rojo uno de los símbolos de menor que, mayor que, o igual."
d["Re-arrange right"] = "Reordena los números de arriba para que estén en el orden correcto"
d["Complete abc"] = "Completa el abecedario utilizando las letras de arriba."
d["Write a word:"] = "Escribe una palabra:"
d["Find and separate"] = "Encuentra y separa los números pares de los números impares en la serie de arriba."
d["Re-arrange alphabetical"] = "Reordena las letras de arriba para que estén en orden alfabético."
d["Re-arrange ascending"] = "Reordena los números de arriba para que estén en orden ascendente."

#game dialogs
d["Please try again."] = "Por favor, inténtalo de nuevo."
d["Sorry! It is wrong."] = "Lo siento, está mal."
d["Perfect! Task solved!"] = "¡Perfecto! ¡Tarea solucionada!"
#d["work harder"] = "You need to work a little bit harder next time."
d["work harder"] = "Tienes que esforzarte un poco más la próxima vez."
#level_controller
d["Game Over!"] = "¡Fin del juego!"
d["Congratulations! Game Completed."] = "¡Enhorabuena! Has terminado todas las actividades en este juego."
d["Great job!"] = ["¡Buen trabajo!","¡Perfecto!","¡Maravilloso!","¡Genial!","¡Bien hecho!"]
d["Perfect! Level completed!"] = "¡Perfecto! ¡Nivel terminado!"

#game specific labels:
d["area:"] = "área:"
d["perimeter:"] = "perímetro:"
d["surface area:"] = "área de la superficie:"
d["volume:"] = "volumen:"
d["Perfect!"] = "¡Perfecto!"
d["divided by"] = "dividido entre"
d["multiplied by"] = "multiplicado por"
d["equals"] = "es igual a"
d["Shopping List"] = "Lista de la compra"
d["Even"] = "Par"
d["Odd"] = "Impar"
d["white"]="blanco"
d["black"]="negro"
d["grey"]="gris"
d["red"]="rojo"
d["orange"]="naranja"
d["yellow"]="amarillo"
d["olive"]="verde oliva"
d["green"]="verde"
d["sea green"]="verde mar"
d["teal"]="verde azulado"
d["blue"]="azul"
d["navy"]="azul marino"
d["purple"]="púrpura"
d["violet"]="violeta"
d["magenta"]="magenta"
d["indigo"]="añil"
d["pink"]="rosa"
d["maroon"] = "granate"
d["brown"] = "marrón"
d["aqua"] = "ciano"
d["lime"] = "lima"

#new
d["Keyboard Skills"] = "Habilidad con el teclado" #Not available for this language
d["Touch Typing"] = "Mecanografía"
d["Translators"] = "Traducción"
d["English Alphabet"] = "Alfabeto inglés"
d["Your Alphabet"] = "Alfabeto español"

#new in 0.3.0
d["Paint Mixer"] = "Mezcla de colores para pintar"
d["Mixing RYB"] = "Mezcla pintura roja, amarilla, azul, negra y blanca"

d["Light Mixer"] = "Mezcla aditiva de colores: Luz"
d["Mixing RGB"] = "Mezcla luz roja, verde y azul para obtener otros colores"

d["Ink Mixer"] = "Mezcla sustractiva de colores: Pinturas, Tintes"
d["Mixing CMY"] = "Mezcla pintura ciano, magenta y amarilla para obtener otros colores"

d["Find the colour of the circle"] = "Encuentra el color del círculo"
d["Adjust CMY"] = "Ajusta la cantidad de pintura ciano, magenta y amarilla"
d["Adjust RGB"] = "Ajusta la intensidad de la luz roja, verde y azul"

#the following is used by colour matching games in spoken hints
#ie. "more red, less green, blue is ok"
d["more color"] = "más"
d["less color"] = "menos"
d["color is ok"] = "está bien"
#in some languages to keep the colours gramaticaly correct 
#the ie. red will be a different word in "more red" and "red is ok"
#ie. in Polish "więcej czerwonego" and "czerwony jest ok"
#and in the following 2 element lists first element is used with more, less,
#and the second with the "is ok" - in most languages those will be the same, but not in Polish or Russian
d["of red"] = ["rojo","el rojo"]
d["of green"] = ["verde","el verde"]
d["of blue"] = ["azul","el azul"]
d["of cyan"] = ["ciano","el ciano"]
d["of magenta"] = ["magenta","el magenta"]
d["of yellow"] = ["amarillo","el amarillo"]

#new in 0.3.1
d["brush size"] = "tamaño de la brocha"

#new in 0.3.2
#d["TicTacToe"] = "Tres en raya"
d["TicTacToe2"] = "Tres en raya 2 - Consigue la mayor..."
d["TicTacToe3"] = "Tres en raya 3 - Consigue la mayor..."
#d["multiline-tictactoe"] = "Consigue la mayor cantidad posible de líneas de 3 para ganar"
d["multiline-tictactoe"] = "cantidad posible de líneas de 3 para ganar"


d["Player"] = "Participante"
d["Won"] = "Ha ganado"
d["Game Draw"] = "Empate"
d["UserName"] = "Tu nombre"

d["Match Animals Memory"] = "Empareja los animales"
d["Match Fruits"] = "Empareja las frutas"
d["Match Vegetables"] = "Empareja los vegetales"
d["Match Numbers"] = "Empareja los números"
d["Find pairs"] = "Encuentra las parejas de la misma imagen"

d["Sliced Images"] = "Imágenes troceadas"
d["Sliced Animals"] = "Animales"
d["Sliced Fruits"] = "Frutas"
d["Sliced Numbers"] = "Números"

d["Fraction Groups"] = "Grupos de fracciones"
d["Percentages"] = "Porcentajes"
d["Ratios"] = "Relaciones"
d["Fract instr0"] = "Empareja las imágenes de la derecha con las de la izquierda"
d["Fract instr1"] = ["Empareja las imágenes y las fracciones de la derecha","con las imágenes de la izquierda"]
d["Fract instr2"] = "Empareja las imágenes con las fracciones de la izquierda"
d["Fract instr3"] = ["Empareja las imágenes, fracciones y números decimales de la derecha","con sus representaciones en forma de porcentaje"]
d["Fract instr4"] = ["Empareja las gráficas con las relaciones de la izquierda","expresadas como una proporción entre partes coloreadas y partes blancas"]
d["Ratio"] = "Relac."

d["Maths Matching Game"] = "Empareja los números"
d["Addition"] = "Suma"
d["Subtraction"] = "Resta"
d["Multiplication"] = "Multiplicación"
d["Division"] = "División"

d["Check for newer version..."] = ["","Busca una versión más actualizada, reporta fallos, debate, traduce o revisa este proyecto en:"]
d["Match numbers to their spelling"] = "Relaciona los números con su forma escrita"
d["Number Spelling"] = "Escritura de números"

d["Match Animals"] = "Empareja los animales"
d["Find all matching animals"] = "Encuentra todos los animales que coinciden"
d["Match animals to their shadows"] = "Empareja los animales con sus sombras"

d["ShapeMaker"] = "Creador de figuras"

d["draw_instr1"] = "Figura a dibujar: %s"
d["draw_instr2"] = "Figura a dibujar: %s de forma que " #if the following size_instr turn out to be too long the beginning can be moved here, ie. d["draw_instr2"] = "Shape to draw: %s, such that" 

d["size_instr_0"] = "las longitudes de sus bases sean iguales a %d y a %d y que su altura sea igual a %d" #for trapeziums
d["size_instr_1"] = "la longitud de sus lados sea igual a %d" #square
d["size_instr_2"] = "las longitudes de sus lados sean iguales a %d y %d" #rectangle
d["size_instr_3"] = "la longitud de sus dos bases paralelas sea igual a %d y que su altura sea igual a %d" #for parallelogram
d["size_instr_4"] = "la longitud de su base sea igual a %d y que su altura sea igual a %d" #for triangles incl. isosceles triangles
d["size_instr_5"] = "las longitudes de sus catetos sean iguales a %d y %d" #for right triangles
d["size_instr_6"] = "la longitud de sus dos catetos sea igual a %d" #for right isosceles triangles
d["size_instr_7"] = "la longitud de su hipotenusa sea igual a %d" #for right isosceles triangles
d["size_instr_8"] = "la longitud de uno de sus lados sea igual a %d y que su altura sea igual a %d" #for obtuse triangles
d["size_instr_9"] = "la longitud de su radio sea igual a %d" #for circles

d["square"] = shape_names[5]
d["rectangle"] = shape_names[6]
d["right_trapezium"] = shape_names[7] 
d["iso_trapezium"] = shape_names[8] 
d["rhombus"] = shape_names[9] 
d["parallelogram"] = shape_names[10] 
d["quadrilateral"] = "Cuadrilátero"
d["trapezium"] = "Trapecio"
d["u_trapezium"] = "Trapecio"
d["triangle"] = "Triángulo"
d["squished_quadi"] = "cuadrilátero 'aplastado'"

d["equi_tria"] = shape_names[0]
d["iso_tria"] = shape_names[1]
d["obtuse_tria"] = shape_names[2]
d["right_tria"] = shape_names[3]
d["acute_tria"] = shape_names[4]
d["right_iso_tria"] = "Triángulo isósceles rectángulo"
d["obtuse_iso_tria"] = "Triángulo isósceles obtuso"
d["acute_iso_tria"] = "Triángulo isósceles agudo"
d["squished_tria"] = "Vaya... Triángulo 'aplastado'" #used to label a drawn "triangle" with angles: 0º, 180º, 0º - all points on one line
d["circle"] = shape_names[13]
d["triangle_not_really"] = "¿Triángulo? Bueno, realmente no..." #used to label a drawn "quadrilateral" with one of its angles equal to 180º - in effect making it look like triangle

d["test_yourself"] = "Ponte a prueba"
d["Clock1"] = "Reloj"
d["Read time"] = "Aprende a leer el reloj"
d["Clock2"] = "Reloj"
d["Set time"] = "Aprende a ajustar el reloj"
d["Set_clock"] = "Ajustar el reloj a:"
d["Set_clock_instr"] = ["","Arrastra las manecillas","para ajustar el reloj"]
d["What time"] = "¿Qué hora es?"
d["close_confirm"] = "Pulsa clic de nuevo para salir"
d["answer_enter"] = "Escribe tu respuesta y pulsa intro"

d["enable_untranslated"] = "Mostrar los lenguajes todavía sin traducción (para pruebas):"
d["Fullscreen:"] = "Pantalla completa:"

d["Time"] = "Tiempo"
d["Play_w_clock"] = "Gira las manecillas del reloj y observa qué ocurre."

d["lets_see_what_you_draw"] = "Veamos qué figuras puedes dibujar"
d["txt_only"] = "Tiempo solo en versión de texto"
d["Clock0"] = "¿Cómo funciona un reloj?"
d["Columnar addition"] = "Suma de la columna"
d["Columnar subtraction"] = "Resta de la columna"

d["Long multiplication"] = "Multiplicación larga"
d["Long division"] = "División larga"

d["borrow 10"] = "tomo 10"
d["carry"] = "me llevo" #in columnar addition, ie. in case of 4 + 8 you write 2 under the column and carry 1
d["demo start"] = "Comenzar >>"
d["demo next eg"] = "Siguiente ejemplo >>"
d["demo next step"] = "Siguiente paso >>"
d["demo write"] = "escribe " #used to show which digit of the result should be entered in a box, ie. "write 5"
d["Demonstration"] = "Demostración"
d["DIY"] = "Hazlo tú"
d["Working with large numbers"] = "Trabajando con números grandes"
d["demo rewrite"] = "reescribir "
d["remainder"] = "resto"
d["demo_result"] = "resultado"
d["TimeMatching"] = "Empareja los relojes"