# -*- coding: utf-8 -*-
import pygame
from pygame import *

#Константы
WALL_W = 20
WALL_H = 20
WALL = (WALL_W, WALL_H)
WALL_COLOR = "#E30000"

BLOK_W = 69
BLOK_H = 20
BLOCK = (BLOK_W, BLOK_H)
BLOK_COLOR = "#32B9FF"

class Wall(sprite.Sprite):
    def __init__(self, x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface(WALL)
        self.image.fill(Color(WALL_COLOR))
        self.rect = Rect(x,y, WALL_W, WALL_H)


class Block(sprite.Sprite):
    def __init__(self, x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface(BLOCK)
        self.image.fill(Color(BLOK_COLOR))
        self.rect = Rect(x,y, BLOK_W, BLOK_H)
