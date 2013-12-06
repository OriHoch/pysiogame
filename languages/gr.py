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
shape_names = ["Ισόπλευρο Τρίγωνο",     "Ισοσκελές Τρίγωνο", "Αμβλυγώνιο Τρίγωνο", "Ορθογώνιο Τρίγωνο", "Οξυγώνιο Τρίγωνο", "Τετράγωνο", "Ορθογώνιο Παραλληλόγραμμο", "Ορθογώνιο Τραπέζιο", "Ισοσκελές Τραπέζιο", "Ρόμβος", "Παραλληλόγραμμο", "Πεντάγωνο", "Εξάγωνο", "Κύκλος", "Έλλειψη"]
#shape_names = ["Equilateral Triangle", "Isosceles Triangle", "Obtuse Triangle",     "Right Triangle",    "Acute Triangle",    "Square",   "Rectangle",             "Right Trapezium", "Isosceles Trapezium", "Rhombus", "Parallelogram", "Pentagon", "Hexagon", "Circle", "Ellipse"]

solid_names = ["Κύβος", "Παραλληλεπίπεδο", "Tριγωνικό Πρίσμα", "Τετραγωνική Πυραμίδα", "Τριγωνική Πυραμίδα", "Σφαίρα", "Κύλινδρος", "Κώνος", "Τόρος"]
numbers = ['ένα', 'δύο', 'τρία', 'τέσσερα', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα', 'δεκατρία', 'δεκατέσσερα', 'δεκαπέντε', 'δεκαέξι', 'δεκαεπτά', 'δεκαοκτώ', 'δεκαεννέα', 'είκοσι', 'είκοσι ένα', 'είκοσι δύο', 'είκοσι τρία', 'είκοσι τέσσερα', 'είκοσι πέντε', 'είκοσι έξι', 'είκοσι επτά', 'είκοσι οκτώ', 'είκοσι εννέα']
numbers2090 = ['είκοσι','τριάντα','σαράντα','πενήντα','εξήντα','εβδομήντα','ογδόντα','ενενήντα']

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
           
d['abc_flashcards_word_sequence'] = ['Άλογο', 'Βάρκα', 'Γάτα', 'Δέντρο', 'Ελέφαντας', 'Ζέβρα', 'Ήλιος', 'Θάμνος', 'Ιπποπόταμος', 'Καμηλοπάρδαλη', 'Λουλούδια', 'Μήλο', 'Ντομάτα', 'Ξυλόφωνο', 'Ομπρέλα', 'Πάπια', 'Ρούχα', 'Σπίτι', 'Τσαγιέρα', 'Ύπνος', 'Φορτηγό', 'Χιμπατζής', 'Ψάρι', 'Ώρα']
d['abc_flashcards_frame_sequence'] = [45,1,2,31,4,25,18,46,47,30,36,42,33,23,20,3,48,7,19,49,50,37,5,51]

#used in telling time activity
#the number lists below are for languages with a bit more complex forms, ie. different suffixes depending on context - if your language is like that check Polish translation to see how to use them
d["minute_numbers_1to29"] = numbers[:]
#last digit when joining numbers of minutes

#hours case 0: full hour, ie. one o'clock, two o'clock, etc.
#d["hours_a"] = ['ένα', 'δύο', 'τρία', 'τέσσερα', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα']
d["hours_a"] = ['μία', 'δύο', 'τρεις', 'τέσσερις', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα']

#hours case 1: ie. ten past one, 22 past three, etc. 
d["hours_b"] = d["hours_a"][:]

#hours case 2: ie. ten to one, 22 to three, etc.
d["hours_c"] = d["hours_a"][:]

d["time_string_one_to"] = "%s παρά ένα λεπτό"
d["time_string_one_past"] = "%s και ένα λεπτό"
d["time_string_to_mh"] = "" #ie. five to four
d["time_string_past_mh"] = "" #ie. five past four

d["time_string_to_hm"] = "%s παρά %s" #ie. 3:55 = four o'clock in five
d["time_string_past_hm"] = "%s και %s" #ie. 4:05 = four and five minutes

d["time_string_half_to"] = "" #ie. in languages using this form, ie. half to four
d["time_string_half_past"] = "%s και μισή" #ie. half past three
#if you never use the "to the hour" form leave the above fields blank and only fill one of the following two
d["time_string_1_59_past_mh"] = "" 
d["time_string_1_59_past_hm"] = ""
d["time_string_3q_past"] = "" #if you don't use quarter to but rather past use this one to either say it's 3 quarters past or 45 past - and leave the "quarter to" field blanck

d["time_string_q_to"] = "%s παρά τέταρτο"
d["time_string_q_past"] = "%s και τέταρτο"
d["time_string_full"] = "%s ακριβώς"

fruit = ["πράσινο μήλο", "κόκκινο μήλο", "φράουλα", "αχλάδι", "πορτοκάλι", "κρεμμύδι", "ντομάτα", "λεμόνι", "κεράσι", "πιπεριά", "καρότο", "μπανάνα", "καρπούζι"]    
fruits_1 = ["πράσινα μήλα", "κόκκινα μήλα", "φράουλες", "αχλάδια", "πορτοκάλια", "κρεμμύδια", "ντομάτες", "λεμόνια", "κεράσια", "πιπεριές", "καρότα", "μπανάνες", "καρπούζια"]     
fruits_2 = []
#[[for this number of fruits (in range of 2-7) use names from fruits_1],[and for those from fruits_2]]
plural_rules = [[2,3,4,5,6,7],[]] #used for some languages where there are more than one form for plurals depending on number

#alphabet gr
alphabet_lc = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
alphabet_uc = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-','ς','ά', 'έ', 'ή', 'ί','ϊ', 'ό', 'ύ', 'ώ']
accents_uc = ['Ά', 'Έ', 'Ή', 'Ί', 'Ϊ', 'Ό', 'Ύ', 'Ώ']
#game start
d["Hello"] = "Χαίρετε" #"Καλωσήλθατε"
d["Welcome back."] = "Καλωσήλθατε πάλι στο παιχνίδι."

#settings
d["Preferences"] = "Επιλογές"
d["Language"] = "Γλώσσα"
d["Reader"] = "Ηλεκτρονικός Αναγνώστης"
d["Read Instructions"] = "Διαβάστε τις οδηγίες στην έναρξη του παιχνιδιού"

#menu categories
d["Info Category"] = "Πληροφορίες και Ρυθμίσεις"
d["Keyboard & Mouse"] = "Πληκτρολόγιο και Ποντίκι"
d["Discover Letters"] = "Ανακαλύψτε τα Γράμματα"
d["Learn Words"] = "Μάθετε νέες λέξεις"
#d["Arithmetic"] = "Αριθμητική"
d["Maths"] = "Μαθηματικά"
d["Numbers & Basic Operations"] = "Αριθμοί και Βασικές Πράξεις"
d["Basic Operations - exercises"] = "Βασικές Πράξεις"
d["Sorting and Comparing"] = "Συλλογή και Σύγκριση"
#d["Geometry"] = "Γεωμετρία και την αναγνώριση σχήμα"
d["Geometry"] = "Γεωμετρία και αναγνώριση σχημάτων"
d["Art"] = "Καλλιτεχνία και χρώμα"
d["Memory"] = "Μνήμη"
d["Games & Mazes"] = "Παιχνίδια και Λαβύρινθοι"
d["Multiplayer"] = "Multi-Player Παιχνίδια"

#games
d["About."] = "Σχετικά με"
d["Game info..."] = "Πληροφορίες Παιχνιδιού"
d["Credits"] = "Πνευματικά δικαιώματα & Συντελεστές"
d["Hit the Mole"] = "Χτύπα τον τυφλοπόντικα"
d["Letters"] = "Γράμματα"
d["Letter Flashcards"] = "Μάθε γράμματα με καρτέλες"
d["Learn to Write"] = "Μάθε να γράφεις"
d["Trace Letters"] = "Σχεδίασε γράμματα και αριθμούς"
d["Complete the ABC"] = "Συμπλήρωσε την Αλφαβήτα"
d["English"] = "Αγγλικά"
d["in your language"] = "Ελληνικά"
d["Sorting Letters"] = "Ταξινόμησε τα γράμματα"
d["Lowercase Letters"] = "Πεζά γράμματα"
d["Uppercase Letters"] = "Κεφαλαία γράμματα"
d["Word Builder"] = "Χτίσιμο λέξεων"
d["Word Maze"] = "Λαβύρινθος με γράμματα"
d["Collect all"] = "Βάλε τα γράμματα στη σωστή σειρά"
d["Word Maze + 4"] = "Λαβύρινθος με γράμματα + 4"
d["Numbers"] = "Αριθμοί"
d["Number Flashcards"] = "Μάθε να μετράς με καρτέλες"
d["Learn to Count"] = "Μάθε να μετράς"
#d["Basic A n S"] = "Πρόσθεση και Αφαίρεση"
d["Basic Addition"] = "Πρόσθεση"
d["Basic Subtraction"] = "Αφαίρεση"
d["Shopping List"] = "Λίστα αγορών"
d["Plus or Minus"] = "Συν ή Μείον"
d["Basic Operations"] = "Βασικές πράξεις"
d["Multiplication Table"] = "Προπαίδεια"
d["Find the product"] = "Βρες το αποτέλεσμα"
d["Find the multiplier"] = "Βρες τον πολλαπλασιαστή"
d["Division"] = "Διαίρεση"
d["Sorting Numbers"] = "Ταξινόμησε τους αριθμούς"
d["Number Comparison"] = "Σύγκρινε τους αριθμούς"
d["Addition & Subtraction"] = "Πρόσθεση και αφαίρεση"
d["Comparison"] = "Σύγκριση"
d["Fractions"] = "Κλάσματα"
d["Decimal Fractions"] = "Δεκαδικά κλάσματα"
d["Even or Odd"] = "Ζυγοί ή μονοί αριθμοί"
d["Shapes"] = "Σχήματα"
d["Shape Flashcards"] = "Μάθε σχήματα με καρτέλες"
d["Solids"] = "Σχήματα"
d["Solid Flashcards"] = "Γεωμετρικά σχήματα με κάρτες"
d["Shape Matching"] = "Ταίριαξε τα σχήματα"
d["help me find my shadow"] = "Βοήθησε με να βρω την σκιά μου"
d["Paint"] = "Χρωμάτισε"
d["Colour Matching"] = "Ταίριαξε τα χρώματα"
d["label the colours"] = "Βάλε ετικέτα στα χρώματα"
d["Follow the Arrows"] = "Ακολούθησε τα βέλη"
d["remember the directions"] = "Να θυμάσαι τις οδηγίες"
d["Photographic Memory"] = "Φωτογραφική μνήμη"
d["Training"] = "Προπόνηση"
d["Photographic Memory"] = "Φωτογραφική μνήμη"
d["Automatic Levels"] = "Αυτόματα επίπεδα"
d["Mouse Maze"] = "Λαβύρινθος με ποντίκι"
d["Let's have some cheese"] = "Ας πάρουμε λίγο τυρί"
d["Sheep Maze"] = "Λαβύρινθος με πρόβατο"
d["Find the rest"] = "Βρες το υπόλοιπο της αγέλης"
d["Connect"] = "Σύνδεση"
d["Balloons with threads"] = "Μπαλόνια με νήματα"
d["Fifteen"] = "Δεκαπέντε"
d["With a Twist"] = "Με μια στροφή"

#game instructions
d["Drag the slider"] = ["Σύρτε την στήλη πάνω ή κάτω","μέχρι το σωστό σύμβολο να βρεθεί στο κόκκινο τετράγωνο"]
d["Take your sheep"] = "Οδήγησε το πρόβατό σου πίσω στο κοπάδι."
d["Check the shopping list"] = "Συμπλήρωσε την λίστα με τα ψώνια και τοποθέτησέ τα μέσα στο καλάθι."
d["Drag lt"] = "Σύρε ένα από τα <, > ή = (μικρότερο, μεγαλύτερο ή ίσο) στο κόκκινο τετράγωνο."
d["Drag lt2"] = "Σύρε ένα από τα μικρότερο, μεγαλύτερο ή ίσο στο κόκκινο τετράγωνο."
d["Re-arrange right"] = "Βάλε τους παραπάνω αριθμούς στη σωστή σειρά."
d["Complete abc"] = "Συμπλήρωσε την αλφάβητο με τα παραπάνω γράμματα."
d["Write a word:"] = "Γράψε μια λέξη:"
d["Find and separate"] = "Βρες και χώρισε τους ζυγούς από τους περιττούς αριθμούς στην παραπάνω σειρά."
d["Re-arrange alphabetical"] = "Βάλε με αλφαβητική σειρά τα παραπάνω γράμματα."
d["Re-arrange ascending"] = ["Βάλε τους παραπάνω αριθμούς στην σειρά,", "από τον μικρότερο προς τον μεγαλύτερο."]

#game dialogs
d["Please try again."] = "Παρακαλώ ξαναπροσπάθησε."
d["Sorry! It is wrong."] = "Λυπάμαι! Είναι Λάθος"
d["Perfect! Task solved!"] = "Τέλεια! Το έλυσες!"
d["work harder"] = "Χρειάζεται να προσπαθήσεις περισσότερο την επόμενη φορά."

#level_controller
d["Game Over!"] = "Τέλος του Παιχνιδιού!"
d["Congratulations! Game Completed."] = "Συγχαρητήρια! Ολοκλήρωσες με επιτυχία το παιχνίδι."
d["Great job!"] = ["Πολύ καλα!", "Τέλεια!", "σούπερ!", "Μπράβο!"]
#d["Great job!"] = ["Great job!","Perfect!","Awesome!","Well done!"]

d["Perfect! Level completed!"] = "Τέλεια! Το στάδιο αυτό ολοκληρώθηκε!"

#game specific labels:
d["area:"] = "επιφάνεια:"
d["perimeter:"] = "περιφέρεια:"
d["surface area:"] = "εμβαδόν επιφάνειας:"
d["volume:"] = "όγκος:"
d["Perfect!"] = "Τέλεια!"
d["divided by"] = "διαιρούμενο με"
d["multiplied by"] = "φορές"
d["equals"] = "ισούται"
d["Shopping List"] = "Λίστα για ψώνια"
d["Even"] = "Ζυγά"
d["Odd"] = "Μονά"
d["white"]="λευκό"
d["black"]="μαύρο"
d["grey"]="γκρι"
d["red"]="κόκκινο"
d["orange"]="πορτοκαλί"
d["yellow"]="κίτρινο"
d["olive"]="λαδί"
d["green"]="πράσινο"
d["sea green"]="σμαραγδί" #"θαλασσί"
d["teal"]="γαλαζοπράσινο" #["πράσινο", "τσαγιού"]

#d["blue"]="γαλάζιο"
#d["navy"]="μπλε"

d["blue"]="μπλε"
d["navy"]="σκούρο μπλε"

d["purple"]="μωβ"
d["violet"]="βιολετί"
d["magenta"]="πορφυρό"
d["indigo"]="λουλάκι"
d["pink"]="ρόζ"
d["maroon"] = "καστανό"
d["brown"] = "καφέ"
d["aqua"] = "κυανό"
d["lime"] = "πρασινολέμονο" #"λεμονί"

#new
d["Keyboard Skills"] = "Πλκτρολόγιο Ουράνιο Τόξο"
d["Touch Typing"] = "Εκμάθηση δακτυλογράφησης με τυφλό σύστημα"
d["Translators"] = "Μεταφραστές" #Μεταφράσεις

d["English Alphabet"] = "Αγγλικό αλφάβητο"
d["Your Alphabet"] = "Ελληνικό αλφάβητο"

#new in 0.3.0
#d["Paint Mixer"] = "Mixing Colours for Painting"
d["Paint Mixer"] = "Μίξη χρωμάτων για ζωγραφική"
#d["Mixing RYB"] = "Mix red, yellow, blue, black and white paint"
d["Mixing RYB"] = "Μίξη κόκκινης, κίτρινης, μπλε, μαύρης και άσπρης μπογιάς" #add black
#d["Light Mixer"] = "Additive Colour Mixing - Light"
d["Light Mixer"] = "Μίξη με ρύθμιση της έντασης των βασικών χρωμάτων" #here again the "- Light" is just to clarify that additive mixing is used when mixing light emitted by screens
#d["Mixing RGB"] = "Mix red, green and blue light to get other colours"
d["Mixing RGB"] = "Ρύθμιση έντασης  κόκκινου, πράσινου και μπλε για δημιουργία άλλων χρωμάτων" #this needs changing + add green to it :)
#d["Ink Mixer"] = "Subtractive Colour Mixing - Paints, Dyes, Inks"
d["Ink Mixer"] = "Μίξη με αφαίρεση χρωμάτων - Μπογιές, βαφές και μελάνια"
#d["Mixing CMY"] = "Mix cyan, magenta and yellow paint to get other colours"
d["Mixing CMY"] = "Μίξη κυανής, ματζέντα και κίτρινης μπογιάς για δημιουργία άλλων χρωμάτων"
#d["Find the colour of the circle"] = "Find the colour of the circle"
d["Find the colour of the circle"] = "Βρες το χρώμα του κύκλου"
#d["Adjust CMY"] = "Adjust the amount of cyan, magenta and yellow paint"
d["Adjust CMY"] = "Προσαρμογή της ποσότητας της κυανής, ματζέντα και κίτρινης μπογιάς"
#d["Adjust RGB"] = "Adjust the intensity of red, green and blue light"
d["Adjust RGB"] = "Προσαρμογή της έντασης του κόκκινου, πράσινου και μπλε φωτός"

#the following is used by colour matching games in spoken hints
#ie. "more red, less green, blue is ok"
d["more color"] = "περισσότερο"
d["less color"] = "λιγότερο"
d["color is ok"] = "είναι εντάξει"
#in some languages to keep the colours gramaticaly correct 
#the ie. red will be a different word in "more red" and "red is ok"
#ie. in Polish "więcej czerwonego" and "czerwony jest ok"
#and in the following 2 element lists first element is used with more, less,
#and the second one with the "is ok" - in most languages those will be the same, but not in Polish or Russian
d["of red"] = ["κόκκινο","το κόκκινο"]
d["of green"] = ["πράσινο","το πράσινο"]
d["of blue"] = ["μπλε","το μπλε"]
d["of cyan"] = ["κυανό","το κυανό"]
d["of magenta"] = ["ματζέντα","το ματζέντα"]
d["of yellow"] = ["κίτρινο","το κίτρινο"]

#new in 0.3.1
d["brush size"] = "Μέγεθος πινέλου"

#new in 0.3.2
d["TicTacToe2"] = "Τρίλιζα 2"
d["TicTacToe3"] = "Τρίλιζα 3"
d["multiline-tictactoe"] = "Κάνε όσες πιο πολλές τρίλιζες μπορείς για να κερδίσεις"


d["Player"] = "Ο παίκτης"
d["Won"] = "Κέρδισε"
d["Game Draw"] = "Ισοπαλία"
d["UserName"] = "Όνομα χρήστη"

d["Match Animals Memory"] = "Ταίριαξε τα ζώα"
d["Match Fruits"] = "Ταίριαξε τα φρούτα"
d["Match Vegetables"] = "Ταίριαξε τα λαχανικά"
d["Match Numbers"] = "Ταίριαξε τους αριθμούς"
d["Find pairs"] = "Βρες τα ζευγάρια της ίδιας φωτογραφίας"

d["Sliced Images"] = "Κομμένες Εικόνες"
d["Sliced Animals"] = "Ζώα"
d["Sliced Fruits"] = "Φρούτα"
d["Sliced Numbers"] = "Αριθμοί"

d["Fraction Groups"] = "Ομάδες κλασμάτων"
d["Percentages"] = "Ποσοστά"
#d["Ratios"] = "Αναλογίες"
d["Ratios"] = "Λόγος"
d["Fract instr0"] = "Ταίριαξε τους πίνακες κλασμάτων στα δεξιά με εκείνους στα αριστερά"
d["Fract instr1"] = ["Ταίριαξε τους πίνακες κλασμάτων και τα κλάσματα στα δεξιά","με τους πίνακες κλασμάτων στα αριστερά"]
d["Fract instr2"] = "Ταίριαξε τους πίνακες κλασμάτων με τα κλάσματα στα αριστερά"
d["Fract instr3"] = ["Ταίριαξε τους πίνακες κλασμάτων, κλάσματα και δεκαδικά κλάσματα στα δεξιά","με την παράστασή τους ως ποσοστά"]
d["Fract instr4"] = ["Ταίριαξε τους χάρτες με τις αναλογίες στα αριστερά","Οι αναλογίες παρουσιάζονται ως τα χρωματιστά κομμάτια","σε σχέση με τα λευκά"]

d["Maths Matching Game"] = "Παιχνίδι με μαθηματικές πράξεις"
d["Addition"] = "Πρόσθεση"
d["Subtraction"] = "Αφαίρεση"
d["Multiplication"] = "Πολλαπλασιασμός"
d["Division"] = "Διαίρεση"

d["Check for newer version..."] = ["Έλεγχος για καινούργιες εκδόσεις, αναφορά σφαλμάτων, συζήτηση,","μετάφραση και επισκόπηση του προγράμματος στη διεύθυνση:"]
d["Match numbers to their spelling"] = "Ταίριαξε τους αριθμούς με την γραφή τους σαν λέξεις"
d["Number Spelling"] = "Γραφή αριθμών ως λέξεις"

d["Match Animals"] = "Ταίριαξε τα ζώα"
d["Find all matching animals"] = "Βρες τα όμοια ζώα"
d["Match animals to their shadows"] = "Ταίριαξε τα ζώα με τις σκιές τους"

d["ShapeMaker"] = "Δημιουργία Σχημάτων"

d["draw_instr1"] = "Σχεδίασε το σχήμα: %s"
d["draw_instr2"] = "Σχεδίασε το σχήμα: %s, τέτοιο ώστε το μήκος"
d["size_instr_0"] = "των βάσεων του να είναι ίσο με %d και %d, και το ύψος του %d" #for trapeziums
d["size_instr_1"] = "των πλευρών του να είναι ίσο με %d" #square
d["size_instr_2"] = "των πλευρών του να είναι ίσο με %d και %d" #rectangle
d["size_instr_3"] = "των 2 παράλληλων πλευρών του να είναι ίσο με %d και το ύψος του με %d" #for parallelogram
d["size_instr_4"] = "της βάσης του να είναι ίσο με %d και το ύψος του με %d" #for triangles incl. isosceles triangles
d["size_instr_5"] = "των καθέτων πλευρών να είναι ίσο με %d και %d" #for right triangles
d["size_instr_6"] = "και των δύο καθέτων πλευρών να είναι ίσο με %d" #for right isosceles triangles
d["size_instr_7"] = "της υποτοίνουσας να είναι ίσο με %d" #for right isosceles triangles
d["size_instr_8"] = "μιας από τις πλευρές του να είναι ισο με %d και το ύψος του με %d" #for obtuse triangles
d["size_instr_9"] = "της ακτίνας να είναι ίσο με %d" #for circles

d["square"] = shape_names[5]
d["rectangle"] = shape_names[6]
d["right_trapezium"] = shape_names[7]
d["iso_trapezium"] = shape_names[8]
d["rhombus"] = shape_names[9]
d["parallelogram"] = shape_names[10]

d["equi_tria"] = shape_names[0]
d["iso_tria"] = shape_names[1]
d["obtuse_tria"] = shape_names[2]
d["right_tria"] = shape_names[3]
d["acute_tria"] = shape_names[4]
d["circle"] = shape_names[13]
    
d["quadrilateral"] = "Τετράπλευρο"
d["trapezium"] = "Τραπέζιο"
d["u_trapezium"] = "Τραπέζιο"
d["triangle"] = "Τρίγωνο"
#d["squished_quadi"] = ""#"ouch... squished quadrilateral" #used to label a drawn "quadrilateral" with angles: 0º, 180º, 0º, 180º - all points on one line
#d["squished_quadi"] = "Ωχ... ένα συμπιεσμένο τετράπλευρο"
d["squished_quadi"] = "Ωχ... ένα στραπατσαρισμένο τετράπλευρο"
d["right_iso_tria"] = "Ορθογώνιο ισοσκελές τρίγωνο"
d["obtuse_iso_tria"] = "Αμβλυγώνιο ισοσκελές τρίγωνο"
d["acute_iso_tria"] = "Οξυγώνιο ισοσκελές τρίγωνο"
#d["squished_tria"] = ""#"Ouch... squished triangle" #used to label a drawn "triangle" with angles: 0º, 180º, 0º - all points on one line #used to label a drawn "triangle" with angles: 0º, 180º, 0º - all points on one line
#d["squished_tria"] = "Ωχ... ένα συμπιεσμένο τρίγωνο"
d["squished_tria"] = "Ωχ... ένα στραπατσαρισμένο τρίγωνο"
d["triangle_not_really"] = "Τρίγωνο; Λοιπόν, δεν είναι..." #used to label a drawn "quadrilateral" with one of its angles equal to 180º - in effect making it look like triangle

d["test_yourself"] = "Δοκίμασε τον εαυτό σου"
d["Clock1"] = "Ωρολόι"
d["Read time"] = "Μάθε να διαβάζεις την ώρα"
d["Clock2"] = "Ωρολόι"
d["Set time"] = "Μάθε πως να βάζεις την ώρα"
d["Set_clock"] = "Ρύθμισε την ώρα σε:"
d["Set_clock_instr"] = ["Μετακίνησε τους δείκτες","του ωρολογιού","για να βάλεις την ώρα"]
d["What time"] = "Τι ώρα είναι;"
d["close_confirm"] = "Κάνε κλικ ξανά για να βγεις από το παιχνίδι"
d["answer_enter"] = "Πληκτρολόγισε την απάντηση σου και πάτα enter"


d["enable_untranslated"] = "FAO: Μεταφραστές - ενεργοποιήστε το για να δείτε τις μη μεταφρασμένες γλώσσες (για δοκιμή):"
d["Fullscreen:"] = "Πλήρης Οθόνη:"

d["Time"] = "Ώρα"
d["Play_w_clock"] = "Γύρνα τους δείκτες του ωρολογιού και δες τι θα γίνει."

d["lets_see_what_you_draw"] = "Ας δούμε τι σχήματα μπορείς να σχεδιάσεις"
d["txt_only"] = "Ώρα σε μορφή κειμένου μόνο"
d["Clock0"] = "Πως δουλεύει η ώρα;"
"""
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
d["Ratio"] = "Ratio" #or abbreviation if possible
d["Working with large numbers"] = "Working with large numbers"
d["demo rewrite"] = "rewrite "
d["remainder"] = "remainder" #in integer division 5 / 2 = 2 remainder 1
d["demo_result"] = "result"
"""
d["Columnar addition"] = "Κάθετη πρόσθεση"
d["Columnar subtraction"] = "Κάθετη αφαίρεση"
d["Long multiplication"] = "Κάθετος πολλαπλασιασμός"
d["Long division"] = "Κάθετη διαίρεση"
d["borrow 10"] = "πάρε δανεικό 10 (δανείσου μια δεκάδα)"
d["carry"] = "κρατούμενο" #in columnar addition, ie. in case of 4 + 8 you write 2 under the column and carry 1
d["demo start"] = "Ξεκίνα >>"
d["demo next eg"] = "Επόμενο παράδειγμα >>"
d["demo next step"] = "Επόμενο βήμα >>"
d["demo write"] = "γράψε " #used to show which digit of the result should be entered in a box, ie. "enter 5"
d["Demonstration"] = "Επίδειξη"
d["DIY"] = "Κάνε το μόνος σου"
#d["Ratio"] = "Αναλογία" #or abbreviation if possible
d["Ratio"] = "Λόγος"
d["Working with large numbers"] = "Πράξεις με μεγάλους αριθμούς"
d["demo rewrite"] = "κατέβασε το "
d["remainder"] = "υπόλοιπο" #in integer division 5 / 2 = 2 remainder 1
d["demo_result"] = "αποτέλεσμα"
d["TimeMatching"] = "Ταίριαξε τα ωρολόγια"