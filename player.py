# -*- coding: utf-8 -*-
from pygame import *

MOVE_SPEED_RIGHT = 7
MOVE_SPEED_LEFT = -7
WIDTH = 100
HEIGHT = 21
COLOR = "#888888"

class Player(sprite.Sprite):
    def __init__(self, x,y):
        sprite.Sprite.__init__(self)
        self.xvel = 0 # скорость перемещения
        self.startX = x # начальное положение
        self.startY = y 
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x,y, WIDTH, HEIGHT) #физический размер платформы

    def update(self, left, right):
        if left:
            self.xvel = MOVE_SPEED_LEFT # Лево

        if right:
            self.xvel = MOVE_SPEED_RIGHT # Вправо

        if not(left or right): # стоим
            self.xvel = 0
        self.collide(self.xvel)
        self.rect.x += self.xvel # переносим свое положение
         # проверяем на столкновения


    def collide(self, xvel):            # пересекается платформа и стена
        if self.rect.x <= 20:           # если движемся влево
            self.xvel = MOVE_SPEED_RIGHT 
        if self.rect.x + 20 >= 700:     # если движемся вправо
            self.xvel = MOVE_SPEED_LEFT # то стоим
