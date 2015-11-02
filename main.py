# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import *
from player import *
from platform import *
from balls import *

#BLOK_W = 69
#BLOK_H = 20
#BLOCK = (BLOK_W, BLOK_H)
#BLOK_COLOR = "#32B9FF"

#WALL_W = 20
#WALL_H = 20
#WALL = (WALL_W, WALL_H)
#WALL_COLOR = "#E30000"

BACK_COLOR = "#004400"
WIN_W = 800 #Ширина создаваемого окна
WIN_H = 640 # Высота
DISP = (WIN_W, WIN_H)

def main():
    pygame.init()#инициализация пайгейм
    screen = pygame.display.set_mode(DISP)#делаем окошко
    pygame.display.set_caption("Tennis")#называем шапку
    bg = Surface(DISP)#указываем фону размер
    bg.fill(Color(BACK_COLOR))#цвет фона
    hero = Player(350, 570)
    ball = Ball(350, 550)
    left = right = False


    entiti = pygame.sprite.Group()
    block_all = pygame.sprite.Group()
    block_all = []
    entiti.add(hero)
    entiti.add(ball)
    level = [
        "----------------------------------------",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "-                                      -",
        "----------------------------------------"]
    blocks = [
        "+++++++++++",
        "+++++++++++",
        "+++++++++++",
        "+++++++++++",
        "+++++++++++"]
    timer = pygame.time.Clock()
    x=y=0
    for row in level: # для строки 
        for col in row: # для каждого символа
            if col == "-": # делаем стенку
                wall = Wall(x,y)
                entiti.add(wall)
                    #wall = Surface(WALL)
                    #wall.fill(Color(WALL_COLOR)) 
                    #screen.blit(wall,(x,y))
            x += WALL_W # все одной ширины
        y += WALL_H # и высоты
        x =0 # с каждой строки начинаем сначала
    x=y=20
    for block in blocks:  #аналогично для блоков только 
        for col in block: # с другим размером самого блока
            if col == "+":
                bloc = Block(x,y)
                entiti.add(bloc)
                block_all.append(bloc)
                #bloc = Surface(BLOCK)
                #bloc.fill(Color(BLOK_COLOR)) 
                #screen.blit(bloc,(x,y))
            x += BLOK_W
        y += BLOK_H
        x = 20
    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False

            
        screen.blit(bg, (0,0))#каждую итерацию перересовка
        entiti.draw(screen)
        ball.update(hero, block_all)
        hero.update(left, right)        
        pygame.display.update()#обновление вывод изменений на экран
        

if __name__ == "__main__":
    main()
