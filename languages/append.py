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
if len(argv) == 2:
    line = argv[1]
else:
    print("Enter the line to be added to all files (or press ENTER to exit):")
    line = raw_input()

if len(line) > 2 and line not in ["exit", "exit()", "cancel", "cancel()"]:
    for i in range(len(langs)):
        FILE = langs[i]
        with open(FILE,"a") as f:
            f.write("\n"+line)
    print("Completed...")
else:
    print("Aborting...")
    