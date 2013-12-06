#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

all_lng = ["ru_R2", "pl", "en"]
default_lang = "en_GB"
os_lang = ['ru_RU', 'UTF-8'] #os.environ.get('LANG', '').split('.')
if os_lang[0] in all_lng:
    default_lang = os_lang[0][:]
    
else:
    lcount = len(all_lng)
    for i in range(lcount):
        if os_lang[0][0:2] == all_lng[i][0:2]:
            default_lang = all_lng[i]
            continue
print("os lang %s" % os_lang)
print("default_lang %s" % default_lang)