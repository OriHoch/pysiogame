#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
a = os.listdir(os.path.join('res','images','art4apps'))

for each_dir in a:
    print(each_dir)
    b = os.listdir(os.path.join('res','images','art4apps',each_dir))
    c = ['_("'+each[:-4]+'")' for each in b]
    print(c)
    c = [each[:-4] for each in b]
    print(c)
    
"""
a = os.listdir(os.path.join('res','images','art4apps','body'))
#print(a)
b = ['_("'+each[:-4]+'")' for each in a]
print(b)
b = [each[:-4] for each in a]
print(b)
"""
"""
actions
['_("lick")', '_("slam")', '_("beg")', '_("fell")', '_("scratch")', '_("touch")', '_("sniff")', '_("see")', '_("climb")', '_("dig")', '_("howl")', '_("sleep")', '_("explore")', '_("draw")', '_("hug")', '_("teach")', '_("nap")', '_("clay")', '_("catch")', '_("clap")', '_("cry")', '_("sing")', '_("meet")', '_("sell")', '_("peck")', '_("beat")', '_("kneel")', '_("find")', '_("dance")', '_("cough")', '_("cut")', '_("think")', '_("bark")', '_("speak")', '_("cheer")', '_("bake")', '_("write")', '_("punch")', '_("strum")', '_("study")', '_("plow")', '_("dream")', '_("post")', '_("dive")', '_("whisper")', '_("sob")', '_("shake")', '_("feed")', '_("crawl")', '_("camp")', '_("spill")', '_("clean")', '_("scream")', '_("tear")', '_("float")', '_("pull")', '_("ate")', '_("kiss")', '_("sit")', '_("hatch")', '_("blink")', '_("hear")', '_("smooch")', '_("play")', '_("wash")', '_("chat")', '_("drive")', '_("drink")', '_("fly")', '_("juggle")', '_("bit")', '_("sweep")', '_("look")', '_("knit")', '_("lift")', '_("fetch")', '_("read")', '_("croak")', '_("stare")', '_("eat")']
['lick', 'slam', 'beg', 'fell', 'scratch', 'touch', 'sniff', 'see', 'climb', 'dig', 'howl', 'sleep', 'explore', 'draw', 'hug', 'teach', 'nap', 'clay', 'catch', 'clap', 'cry', 'sing', 'meet', 'sell', 'peck', 'beat', 'kneel', 'find', 'dance', 'cough', 'cut', 'think', 'bark', 'speak', 'cheer', 'bake', 'write', 'punch', 'strum', 'study', 'plow', 'dream', 'post', 'dive', 'whisper', 'sob', 'shake', 'feed', 'crawl', 'camp', 'spill', 'clean', 'scream', 'tear', 'float', 'pull', 'ate', 'kiss', 'sit', 'hatch', 'blink', 'hear', 'smooch', 'play', 'wash', 'chat', 'drive', 'drink', 'fly', 'juggle', 'bit', 'sweep', 'look', 'knit', 'lift', 'fetch', 'read', 'croak', 'stare', 'eat']

"""