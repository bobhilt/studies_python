#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 23:41:01 2018

@author: bobhilt
"""

import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        print(event)
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()


            
