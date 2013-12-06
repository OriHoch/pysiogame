# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The color names in other languages than English are already in smaller font.

#when translating the "d" dictionary please translate the values
#and leave keys as they are (the keys are sometimes shortened to save on space)

#Example in German:
# - d["Welcome back."] = "Welcome back in the game."
# + d["Welcome back."] = "Willkommen zurück im Spiel."

d=dict()

#word lists
shape_names = ["Equilateral Triangle", "Isosceles Triangle", "Obtuse Triangle", "Right Triangle", "Acute Triangle", "Square", "Rectangle", "Right Trapezoid", "Isosceles Trapezoid", "Rhombus", "Parallelogram", "Pentagon", "Hexagon", "Circle", "Ellipse"]

solid_names = ["Cube", "Square Prism", "Triangular Prism", "Square Pyramid", "Triangular Pyramid", "Sphere", "Cylinder", "Cone", "Torus"]
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
numbers2090 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

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
           
#The following 2 lines are not to be translated but replaced with a sequence of words starting in each of the letters of your alphabet in order, best if these words have a corresponding picture in images/flashcard_images.jpg. The second line has the number of the image that the word describes. 
#The images are numbered from left to bottom such that the top left is numbered 0, the last image is 73, if none of the available things have names that start with any of the letters we can add new pictures.
d['abc_flashcards_word_sequence'] = ['Apple', 'Butterfly', 'Cat', 'Dolphin', 'Elephant', 'Fortepiano', 'Guitar', 'Hedgehog', 'Igloo', 'Jar', 'Koala', 'Lion', 'Monitor', 'Notebook', 'Ocean', 'Parrot', 'Queen', 'Rabbit', 'Street', 'Tomato', 'Umbrella', 'Violin', 'Watermelon', 'Xylophone', 'Yarn', 'Zebra']
d['abc_flashcards_frame_sequence'] = [42, 27, 2, 59, 4, 34, 28, 29, 8, 9, 72, 11, 40, 13, 52, 15, 16, 17, 53, 33, 20, 21, 26, 23, 24, 25]  

#used in telling time activity
#the number lists below are for languages with a bit more complex forms, ie. different suffixes depending on context - if your language is like that check Polish translation to see how to use them
d["minute_numbers_1to29"] = numbers[:]

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

fruit = ["green apple", "red apple", "strawberry", "pear", "orange", "onion", "tomato", "lemon", "cherry", "pepper", "carrot", "banana", "watermelon"]    
fruits_1 = ["green apples", "red apples", "strawberries", "pears", "oranges", "onions", "tomatoes", "lemons", "cherries", "peppers", "carrots", "bananas", "watermelons"]     
fruits_2 = []
#[[for this number of fruits (in range of 2-7) use names from fruits_1],[and for those from fruits_2]]
plural_rules = [[2,3,4,5,6,7],[]] #used for some languages where there are more than one form for plurals depending on number
#alphabet en
alphabet_lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-']
accents_uc = []

#game start
d["Hello"] = "Hello"
d["Welcome back."] = "Welcome back in the game."

#settings
d["Preferences"] = "Preferences"
d["Language"] = "Language"
d["Reader"] = "eSpeak"
d["Read Instructions"] = "Read Instructions at the start of games"

#menu categories
d["Info Category"] = "Info & Settings"
d["Keyboard & Mouse"] = "Keyboard & Mouse"
d["Discover Letters"] = "Discover Letters"
d["Learn Words"] = "Learn New Words"
d["Maths"] = "Mathematics"
d["Numbers & Basic Operations"] = "Numbers & Basic Operations"
d["Basic Operations - exercises"] = "Basic Operations - Exercises"
d["Sorting and Comparing"] = "Sorting and Comparing"
d["Geometry"] = "Geometry and Shape Recognition"
d["Art"] = "Art and Color"
d["Memory"] = "Memory"
d["Games & Mazes"] = "Games & Mazes"
d["Multiplayer"] = "Multiplayer Games"

#games
d["About."] = "About."
d["Game info..."] = "Game info..."
d["Credits"] = "Copyright & Credits"
d["Hit the Mole"] = "Hit the Mole"
d["Letters"] = "Letters"
d["Letter Flashcards"] = "Learn Letters with Flashcards"
d["Learn to Write"] = "Learn to Write"
d["Trace Letters"] = "Trace Letters and Numbers"
d["Complete the ABC"] = "Complete the ABC"
d["English"] = "English"
d["in your language"] = "English 2"
d["Sorting Letters"] = "Sorting Letters"
d["Lowercase Letters"] = "Lowercase Letters"
d["Uppercase Letters"] = "Uppercase Letters"
d["Word Builder"] = "Word Builder"
d["Word Maze"] = "Word Maze"
d["Collect all"] = "Collect all letters in the right order"
d["Word Maze + 4"] = "Word Maze + 4"
d["Numbers"] = "Numbers"
d["Number Flashcards"] = "Learn Numbers with Flashcards"
d["Learn to Count"] = "Learn to Count"
d["Basic Addition"] = "Basic Addition"
d["Basic Subtraction"] = "Basic Subtraction"
d["Shopping List"] = "Shopping List"
d["Plus or Minus"] = "Plus or Minus"
d["Basic Operations"] = "Basic Operations"
d["Multiplication Table"] = "Multiplication Table"
d["Find the product"] = "Find the product"
d["Find the multiplier"] = "Find the multiplier"
d["Division"] = "Division"
d["Sorting Numbers"] = "Sorting Numbers"
d["Number Comparison"] = "Number Comparison"
d["Addition & Subtraction"] = "Addition & Subtraction"
d["Comparison"] = "Comparison"
d["Fractions"] = "Fractions"
d["Decimal Fractions"] = "Decimal Fractions"
d["Even or Odd"] = "Even or Odd"
d["Shapes"] = "Shapes"
d["Shape Flashcards"] = "Learn Shapes with Flashcards"
d["Solids"] = "Solids"
d["Solid Flashcards"] = "Solid Geometry with Flashcards"
d["Shape Matching"] = "Shape Matching"
d["help me find my shadow"] = "help me find my shadow"
d["Paint"] = "Paint"
d["Colour Matching"] = "Color Matching"
d["label the colours"] = "label the colors"
d["Follow the Arrows"] = "Follow the Arrows"
d["remember the directions"] = "remember the directions"
d["Photographic Memory"] = "Photographic Memory"
d["Training"] = "Training"
d["Photographic Memory"] = "Photographic Memory"
d["Automatic Levels"] = "Automatic Levels"
d["Mouse Maze"] = "Mouse Maze"
d["Let's have some cheese"] = "Let's have some cheese"
d["Sheep Maze"] = "Sheep Maze"
d["Find the rest"] = "Find the rest of the herd"
d["Connect"] = "Connect"
d["Balloons with threads"] = "Balloons with threads"
d["Fifteen"] = "Fifteen"
d["With a Twist"] = "With a Twist"

#game instructions
d["Drag the slider"] = "Drag the slider up or down so that the right sign is in the red square."
d["Take your sheep"] = "Take your sheep to the rest of the herd."
d["Check the shopping list"] = "Check the shopping list and drag all needed items into the basket."
d["Drag lt"] = "Drag one of the <, > or = (lesser, greater or equal) to the red square."
d["Drag lt2"] = "Drag one of the lesser, greater or equal to the red square."
d["Re-arrange right"] = "Re-arrange the above numbers so they are in the right order"
d["Complete abc"] = "Complete the abc using the letters above."
d["Write a word:"] = "Write a word:"
d["Find and separate"] = "Find and separate the Even Numbers form the Odd Numbers in the above series."
d["Re-arrange alphabetical"] = "Re-arrange the above letters so they are in the alphabetical order."
d["Re-arrange ascending"] = "Re-arrange the above numbers so they are in the ascending order."

#game dialogs
d["Please try again."] = "Please try again."
d["Sorry! It is wrong."] = "Sorry! It is wrong."
d["Perfect! Task solved!"] = "Perfect! Task solved!"
d["work harder"] = "You need to work a little bit harder next time."

#level_controller
d["Game Over!"] = "Game Over!"
d["Congratulations! Game Completed."] = "Congratulations! You have completed all tasks in this game."
d["Great job!"] = ["Great job!","Perfect!","Awesome!","Super!","Fantastic job!","Well done!"]
d["Perfect! Level completed!"] = "Perfect! Level completed!"

#game specific labels:
d["area:"] = "area:"
d["perimeter:"] = "perimeter:"
d["surface area:"] = "surface area:"
d["volume:"] = "volume:"
d["Perfect!"] = "Perfect!"
d["divided by"] = "divided by"
d["multiplied by"] = "times"
d["equals"] = "equals"
d["Shopping List"] = "Shopping List"
d["Even"] = "Even"
d["Odd"] = "Odd"
d["white"]="white"
d["black"]="black"
d["grey"]="gray"
d["red"]="red"
d["orange"]="orange"
d["yellow"]="yellow"
d["olive"]="olive"
d["green"]="green"
d["sea green"]="sea green"
d["teal"]="teal"
d["blue"]="blue"
d["navy"]="navy"
d["purple"]="purple"
d["violet"]="violet"
d["magenta"]="magenta"
d["indigo"]="indigo"
d["pink"]="pink"
d["maroon"] = "maroon"
d["brown"] = "brown"
d["aqua"] = "aqua"
d["lime"] = "lime"

#new
d["Keyboard Skills"] = "Rainbow Keyboard"
d["Touch Typing"] = "Touch Typing Tutor"
d["Translators"] = "Translators"
d["English Alphabet"] = "English Alphabet"
d["Your Alphabet"] = "English Alphabet 2"

#new in 0.3.0
d["Paint Mixer"] = "Mixing Colors for Painting"
d["Mixing RYB"] = "Mix red, yellow, blue, black and white paint"

d["Light Mixer"] = "Additive Color Mixing - Light"
d["Mixing RGB"] = "Mix red, green and blue light to get other colors"

d["Ink Mixer"] = "Subtractive Color Mixing - Paints, Dyes, Inks"
d["Mixing CMY"] = "Mix cyan, magenta and yellow paint to get other colors"

d["Find the colour of the circle"] = "Find the color of the circle"
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
d["quadrilateral"] = "Quadrilateral"
d["trapezium"] = "Trapezoid"
d["u_trapezium"] = "Trapezoid"
d["triangle"] = "Triangle"
d["squished_quadi"] = "Ouch... squished quadrilateral" #used to label a drawn "quadrilateral" with angles: 0º, 180º, 0º, 180º - all points on one line

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
d["close_confirm"] = "Click again to exit"
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