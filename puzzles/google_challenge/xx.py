#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:57:21 2018

@author: bobhilt
"""
m, n = 8, 5

the_map = []
row = [0] * n
for i in range(m): # create empty map
    the_map.append(list(row))
the_map