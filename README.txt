pySioGame - Educational Activity Pack for Kids

Please note - this game is playable but still unfinished - or rather is being continuously improved (not so much recently - not enough hours in a day).

Please let me know if you find any errors or bugs in the game or in translations, formulas or other game content.

pySioGame is built with Linux users in mind - written in python and tested on Ubuntu, however it does work on Windows just not tested as thoroughly as on Linux.

The game is intended to be compatible with python 2.7.3+ including python 3.x.

----------------------------------------------

Linux installation:

In order to run this game you need the python-pygame package installed.
To check if you have it run the following lines in terminal (Ctrl+Atl+T):
$ python
>>> import pygame
>>> exit()
If you have no errors importing it you are set, else you need to install it, in Debian based distros run: 
$ sudo apt-get install python-pygame

And if you want to enable the voice in game you also need eSpeak which - if you are using Linux, is most likely already installed, if you are using any other OS - well no luck - I'm afraid it won't work - but can't test it really.

In some cases you may also need to install fonts-freefont-ttf (Debian/Ubuntu) or gnu-free-sans-fonts (Fedora) or equivalent in your distro - maintainers please add it to dependencies.

To start the game from terminal:
python /home/user/path/to/the/game/pysiogame.py

#or using python3:
python3 /home/user/path/to/the/game/pysiogame.py

Should start with double click if marked as executable (Right-click -> Properties -> Permissions -> Allow executing file as program) or if you like you can create a custom launcher using one of the above lines for the command line field (obviously after changing the path to the program first). The pysiogame_icon_48.png file from res/pysiogame_icon folder can be used as the icon for the launcher.

----------------------------------------------

Windows installation (instructions by OriHoch):

Download and install python 2.7 32bit - http://www.python.org/getit/
Download and install espeak 32bit - http://espeak.sourceforge.net/download.html
Download and install pygame for python 2.7 + 32bit  - http://www.pygame.org/install.html

Add espeak to your path (sorry, but this requires some technical windows knowledge)
you should have something like this in your PATH variable:
C:\Program Files (x86)\eSpeak\command_line;(... other paths ...)

Download pysiogame and extract it somewhere, for example c:\pysiogame

To run pysiogame you can add a shortcut on the desktop to:
c:\python27\python.exe c:\pysiogame\pysiogame.py

----------------------------------------------

The first time the game is run will be in normal windowed mode (not in fullscreen).
To display it in fullscreen press Ctrl+F at the start of the game 
or go to Preferences and enable full screen - this will be saved and game will start full screen next time.

----------------------------------------------
Translating:
If you would like to help translating this game please use one of the included files within the i18n/po directory.
If your langauage is not there yet copy the default.pot file rename it temporarily to te_ST.po and start working with the new file using ie. the Poedit.
To test your translation save the file - Poedit will create the .mo file for you - move the .mo file to the locale/te_ST/ directory and rename the file to pysiogame.mo and start the game select the Test Language.
Alternatively you can run the cleanup.py program to get the file renamed and moved where it should be (this program will also remove .pyc and some other temp files under pysiogame - this is used to automate the process of stripping pysiogame before compressing/packaging).

There are some things translated using custom translation files in custom directory - these are usually done by me - but I might need some help to do them - I will get in touch with you if I'll be struggling.

When everything is working ok please email me your .po file.

The es_di.py, fr_di.py, etc. are lists of words used by word building activities. 
These are partial (google) translations from English. The English version is just a list of words most commonly used in English - you may like to check these as well for any words not necessarily suitable for children.
----------------------------------------------

Interface:
Menu Panel - left:
    left column         - list of categories
    right column        - list of games in the current category
    
Score Panel:
    sound               - toggle game sound effects
    voice               - toggle espeak voice synthesiser (if espeak is not installed this icon will not be available)
    score               - shows user's score
    user name           - displays name of currently logged in user
    logout link         - takes you back to the initial screen where you can login as a different user
    
Game Panel - centre - the largest part of screen:
    piece of screen where all game objects are placed for you to drag around :)
    
Game Controls - bottom:
    (some of these buttons are being hidden in some games if they are not needed)

    tick button (ok)      - used to let the app know you have completed the task 
                            and it's ready to be checked you can use ENTER instead to speed this up
                            
    reload                - used to reload the task, or reset it to the start position
                            may be useful in the Connect games if rendered game is unsolvable

    game title            - displays current game title (optional) when cursor is over the game panel
                            and acts as a hint text when cursor is over game/category icons in menu

    left/right arrows     - change levels or just some aspect of the game (ie. photo to piece together)
                            
    left/right            - fast forward/backward - will move by preset amount of levels or 
    double arrows           to skip to the next type of activity (available in some games 
                            with large number of levels)

    level indicator       - top number is the level you are on, the bottom pair of numbers is usually 
                            current game in the level / number of games per level
                            if there's no number of games at the bottom it's up to you to change the level
                            when ready for harder task.
 
    close button          - closes the game (2 clicks needed)

    mini arrow pad        - in games requiring arrows to navigate in the game
                            the mini arrow buttons will appear in the left bottom corner
                            this is to enable it for use with touch screen devices (running ie. Ubuntu)
                            

Technical Stuff:
	This game used to be optimized for 1024x768, but later rebuild to work on larger (and smaller) screens as well.
	The layout is a mixture of fluid, elastic and fixed elements.
	The menu is fixed to the left with static size (doesn't scale, but is scrollable)
	
	The actual game panel is scalable up to either the width or height whichever is smaller,
	On wider screens there will be a gap between the menu and the game panel in some games with fixed width,
	however some games are adjusting its configuration/number of squares to fill the whole screen or as much as possible
	and often number of horizontal squares may be different depending on whether the game is in full screen or in window mode
	and for that reason when changing mode (or resizing window) your current activity gets restarted - so don't do it in the middle of working on something or you will lose it.
	Images on Game Panel will scale - might cause some visual degradation on large screens,
	Bottom panel stretches its width to match that of the game panel, but size of buttons stays the same on all resolutions (and so do the menu icons),
	so on small screens you may end up with no space for game at all, but anything with width over 800 and height over 480 should be fine.
	
Sorry for all the mess in the code, but this is my first and only project after reading some books/tutorials, so do not expect professional product - this was my programming sand-box.
It was intended as a tool for my son to learn. He liked it so hopefully your kid(s) will like it too.

Enjoy!

Ireneusz Imiolek
