# -*- coding: utf-8 -*-

import pygame

class PuzzleBoard():
    def __init__(self,x_count,y_count):
        self.x_count = x_count
        self.y_count = y_count
        self.image = None
        self.create_puzzles(x_count,y_count)
        
    def create_puzzles(x_count,y_count):
        pass
        
    def update(self):
        #draw puzzles on board
        pass
    
class PuzzlePiece():
    def __init__(self):
        pass
    
class MenuState():
    def __init__(self,mainloop):
        pass
        
    def handle(self,event):
        pass
        
    def update(self):
        pass
    
class SolvingState():
    def __init__(self,mainloop):
        pass
    
    def handle(self,event):
        pass
        
    def update(self):
        pass
