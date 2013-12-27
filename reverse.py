#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This is a test program used to prepare rtl languages

import os, sys
import shutil
from classes.extras import unival

def reverse_old(s, alpha):
    l = []
    
    for each in s:
        l.append(each)
    
    ln = len(l)
    l2 = [str(i) for i in range(ln)]
    print(l2)
    tmp = []
    
    for i in range(ln):
        if l[i] in alpha:
            if tmp == []:
                l2[ln-i-1] = l[i]
            else:
                l2[ln-i: ln-i+len(tmp)] = tmp[:]
                l2[ln-i-1] = l[i]
                tmp = []
        else:
            tmp.append(l[i])
            
        if i == ln-1 and tmp != []:
            l2[ln-i-len(tmp):ln-i] = tmp[:]
                
                
    return "".join(l2)
    
def reverse_old2(s, alpha):
    l = []
    p =" :',.?"
    for each in s:
        l.append(each)
    
    ln = len(l)
    l2 = [str(i) for i in range(ln)]
    print(l2)
    tmp = []
    mode = None
    #change it start from right when switching the modes...
    for i in range(ln):
        if l[i] in alpha or (l[i] in p and mode == "rtl"):
            mode = "rtl"
            if tmp == []:
                l2[ln-i-1] = l[i]
            else:
                l2[ln-i-1: ln-i+len(tmp)-1] = tmp[:]
                l2[ln-i-1] = l[i]
                tmp = []
        else:
            mode = "ltr"
            tmp.append(l[i])
            
        if i == ln-1 and tmp != []:
            l2[ln-i-len(tmp):ln-i] = tmp[:]
            
    return "".join(l2)

def reverse(s, alpha):
    l = []
    p =" :',.?()"
    if sys.version_info < (3, 0):
        p = p.decode("utf-8")
        s = s.decode('utf-8')
        alpha = alpha.decode("utf-8")
        
    for each in s:
        l.append(each)
    
    ln = len(l)
    l2 = [' '] * ln
    tmp = ""
    mode = None
    i = ln-1
    j = 0
    ej = None
    print(l)
    while i > -1:
        if l[i] in alpha or (mode == "rtl" and l[i] in p):
            ltmp = len(tmp)
            if ltmp > 0:
                if ltmp == 1:
                    l2[ej] = tmp
                else:
                    #l2[ej:j+1] = tmp
                    l2[ej-1:j-1] = tmp
                tmp = ""
                ej = None
            l2[j] = l[i]
            mode = "rtl"
        else:
            if ej == None:
                ej = j
            tmp = l[i] + tmp
            mode = "ltr"
        j = j+1
        i = i-1
        print(l2)
    if tmp != "":
        l2[ej: j+1] = tmp
        
    return "".join(l2)
    
def test():
    a = "חיטבאהננבהרטיג"
    alpha = "אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ׳״"
    for each in a:
        if each not in alpha:
            print(each)

if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    
    #alpha = "abcdef"
    alpha = "אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ׳״"
    #s = "in as:מחובר כ. Lo."
    s = ",מחובר,"   
    s = "חיטבא" 
    s = "חיטבאהננבהרטיג"
    s = "הזינו סיסמה קודמת באורך של לפחות 4 תוים"
    s = "לפחות 4 תוים"
    #s = u"abcxyzd1123,abc. 345.abc"
    #alpha = "abc"
    #s = "x.y.z .a b c .e" 
    s2 = reverse(s, alpha)
    print(s)
    print(s2)
    print("Done!")