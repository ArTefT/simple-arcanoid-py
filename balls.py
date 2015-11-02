# -*- coding: utf-8 -*-
from pygame import *

BALL_SPEED = 3
WIDTH = 20
HEIGHT = 20
COLOR = "#444455"

class Ball(sprite.Sprite):
    def __init__(self, x,y):
        sprite.Sprite.__init__(self)
        self.xvel = 3
        self.yvel = -3
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x,y, WIDTH, HEIGHT)
        #self.right = False
        #self.down = False
        
    def update(self, hero, block_all): #движем щар
        if self.rect.x <= 20 or self.rect.x + 20 >= 780: # если достагает границы
            self.xvel *=-1                               # устанавливаем скорость
        if self.rect.y <= 20 or self.rect.y +20 >= 640:  # на протовоположную 
            self.yvel *= -1      


        self.rect.x += self.xvel # меняем скорость по х
        self.rect.y += self.yvel # меняем скорость по у
        self.collide(self.xvel, self.yvel, hero, block_all) # проверяем на столкновения


    def collide(self, xvel, yvel, hero, block_all):
        if sprite.collide_rect(self, hero): # контакт с платформой
            if xvel > 0 or xvel < 0:
                self.xvel *= -1
            if yvel > 0 or yvel < 0:
                self.yvel *= -1
                self.xvel *= -1
        for b in block_all:
            if sprite.collide_rect(self, b): # контакт с блоками
                if xvel > 0 or xvel < 0:
                    self.xvel *= -1
                    b.rect = Rect(0,0,0,0)
                    b.kill()
                if yvel > 0 or yvel < 0:
                    self.yvel *= -1
                    self.xvel *= -1
                    b.rect = Rect(0,0,0,0)
                    b.kill()
