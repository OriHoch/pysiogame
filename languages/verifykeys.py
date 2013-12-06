"""
A helper program to add new keys to all language files at once.
"""
import os, sys
import inspect

def where_am_I(): pass
a = os.path.split(os.path.abspath(inspect.getsourcefile(where_am_I)))[0]
os.chdir(a)

#list of language files
langs = ["en_gb.py", "en_us.py", "pl.py", "gr.py", "es.py","pt.py","fr.py","it.py","de.py","ru.py","fi.py"]

argv = sys.argv
if len(argv) == 3:
    l1 = argv[1]
    l2 = argv[1]
else:
    print("Enter first module name:")
    l1 = raw_input()
    l1m = __import__(l1)
    
    print("Enter second module name:")
    l2 = raw_input()
    l2m = __import__(l2)

if len(l1) > 1 and len(l2) > 1 and l1 not in ["exit", "exit()", "cancel", "cancel()"]:
    d1 = l1m.d
    d2 = l2m.d
    for each in d1:
        if each not in d2:
            print each
    print("Completed...")
else:
    print("Aborting...")
    