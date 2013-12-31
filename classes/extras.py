# -*- coding: utf-8 -*-

import os, sys
import subprocess
import colorsys
from classes.simple_vector import Vector2
import random

#the following four color functions take 3 values in range 0 - 255
#h - hue
#s - saturation - s=0 white, s=255 full color
#v - vibrance - v=0 black, v=255 full color
def hsv_to_rgb(h,s,v):
    hsv = [h,s,v]
    hsv_clean = hsv
    for i in range(3):
        if hsv[i] <= 0:
            hsv_clean[i] = 0
        elif hsv[i] >= 255:
            hsv_clean[i] = 1
        else:
            hsv_clean[i] = float(hsv[i])/255.0

    rgb = colorsys.hsv_to_rgb(*hsv_clean)
    return [int(each*255) for each in rgb]

def rgb_to_hsv(r,g,b):
    #pass
    hsv = colorsys.rgb_to_hsv(r/255.0,g/255.0,b/255.0)
    hsv255 = [int(each*255) for each in hsv]
    return hsv255

def hsl_to_rgb(h,s,l):
    hsl = [h,l,s]
    hsl_clean = hsl
    for i in range(3):
        if hsl[i] <= 0:
            hsl_clean[i] = 0
        elif hsl[i] >= 255:
            hsl_clean[i] = 1
        else:
            hsl_clean[i] = float(hsl[i])/255.0

    rgb = colorsys.hls_to_rgb(*hsl_clean)
    return [int(each*255) for each in rgb]

def rgb_to_hsl(r,g,b):
    hsl = colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
    hsl255 = [int(each*255) for each in hsl]
    hsl255 = [hsl255[0],hsl255[2],hsl255[1]]
    return hsl255
    
def unival(value):
    val = value
    if sys.version_info < (3, 0):
        try:
            if not isinstance(value, unicode):
                val = unicode(value, "utf-8")
        except UnicodeDecodeError:
            val = value
        except TypeError:
            val = value
    else:
        val = value
    return val
    
def reverse_x(s, alpha):
    return s
    
def reverse(s, alpha):
    "used with right-to-left languages to reverse text. Takes the string to reverse and a string containing all letters of the rtl alphabet" 
    l = []
    p =" :',.?-"
    s2 = s[:]
    if sys.version_info < (3, 0):
        if not isinstance(s, unicode):
            s = s.decode('utf-8')
        p = p.decode("utf-8")
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
    while i > -1:
        if l[i] in alpha or (mode == "rtl" and l[i] in p):
            ltmp = len(tmp)
            if ltmp > 0:
                if ltmp == 1:
                    l2[ej] = tmp
                else:
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
    if tmp != "":
        l2[ej: j+1] = tmp
        
    return "".join(l2)
    
def rr2(from1,to1,from2,to2,step=1):
    x = random.choice([-1,1])
    if x == -1:
        a = random.randrange(from1,to1,step)
    else:
        a = random.randrange(from2,to2,step)
    return a
    
def rr3(from1,to2, center, exclusion_zone,step=1):
    to1 = center-exclusion_zone
    from2 = center+exclusion_zone
    if from1 < to1 < from2 < to2:
        return rr2(from1, to1, from2, to2, step)
    
def rand_safe_curve(point,width,height):
    x_space = width - point[0] 
    y_space = height - point[1] 
 
    if x_space > point[0]:
        max_x = point[0]
    else:
        max_x = x_space
        
    if y_space > point[1]:
        max_y = point[1]
    else:
        max_y = y_space
        
    x = rr3(point[0]-max_x,point[0]+max_x, point[0], max_x//2)
    y = rr3(point[1]-max_y,point[1]+max_y, point[1], max_y//2)
    return [x,y]

def sqr(num):
    return num*num
 
def cube(num):
    return num*num*num

#points = [[200, 400], [300, 250], [450, 500], [500, 475]]
#points = [[beginning], [beginning_midifier], [end],[end_midifier]]
#points as Vector2
def DrawBezier(points):
    bezier_points = []
    t = 0.0
    while t < 1.02:  # Increment through values of t (between 0 and 1)
       	# Append the point on the curve for the current value of t to the list of Bezier points
        bezier_points.append(GetBezierPoint(points, t))
        t += 0.02
    return bezier_points

def GetBezierPoint(points, t):
    p1 = points[0] * cube(1.0 - t)
    p2 = points[1] * (3 * sqr(1.0 - t) * t)
    p3 = points[2] * cube(t)
    p4 = points[3] * (3 * (1.0 - t) * sqr(t))
    return p1 + p2 + p3 + p4

def inversions(p):
    lp = len(p)
    total_inversions = 0
    for i in range(lp):#pick each number from left to right
        for  j in range(i,lp):#and check it against any numbers to the right
            if p[i] > p[j]:   #if any of them are greater than the number itself
                total_inversions += 1
    return total_inversions

def get_word_list(di):
    'used in touch typing program'
    wl = []
    for i in range(8):
        tmp = set()
        while len(tmp)<10:
            word  = di[i][random.randrange(1,di[i][0])]
            tmp.add(word)
        wl.append(list(tmp))
    return wl
    
def first_upper(text):
    #word_list[i][k][0]) + word_list[i][k][1:]
    if sys.version_info < (3, 0):
        utf = unicode(text, "utf-8")
        #utf = text
        text = utf[0].upper() + utf[1:]
        text = text.encode("utf-8")
    else:
        text = text[0].upper() + text[1:]
        
    return text
    
def word_typing_course(word_list):
    'used in touch typing program to build a list of words to retype'
    #repeats =[3,4,5,6,7,8,9,10]
    repeats = [4,4,3,3,2,2,2,2]
    #repeats = [1,1,1,1,1,1,1,1]
    levels = []
    for i in range(8):
        #tmp = []
        words_line_1 = ""
        words_line_2 = ""
        for k in range(10):
            for j in range(repeats[i]):
                if k<5:
                    words_line_1 += " "+word_list[i][k]
                else:
                    if j == 0:
                        words_line_2 += " " + first_upper(word_list[i][k])
                    else:
                        words_line_2 += " "+word_list[i][k]
            if 0 <= k < 4:
                words_line_1 += ","
            elif k == 4:
                words_line_1 += "."
            elif 5 <= k < 10:
                words_line_2 += "."
        levels.append([[1,1],[words_line_1,words_line_2]])
    return levels
