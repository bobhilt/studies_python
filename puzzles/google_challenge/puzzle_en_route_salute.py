#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
puzzle_en_route_salue.py
Google foobar challenge #2.2
Compute how many "salutes" from passes
Created on Sat Apr 21 09:08:50 2018

@author: bobhilt

Write a program that counts how many salutes are exchanged during a typical walk 
along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', 
an employee walking to the right; '<', an employee walking to the left; 
and '-', an empty space. 
Every employee walks at the same speed either to right or to the left, 
according to their direction. Whenever two employees cross, each of them salutes 
the other. They then continue walking until they reach the end, 
finally leaving the hallway. In the above example, they salute 10 times.

Write a function answer(s) which takes a string representing employees walking 
along a hallway and returns the number of times the employees will salute. 
s will contain at least 1 and at most 100 characters, each one of -, >, or <.

Test cases
==========

Inputs:
    (string) s = ">----<"
Output:
    (int) 2

Inputs:
    (string) s = "<<>><"
Output:
    (int) 4
"""
import re
from bisect import bisect_right

def get_char_indices(findstr,s):
   return [m.start() for m in re.finditer(findstr, s)]

def find_gt_ndx(a, x):
    'Find index of leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return i
        #return a[i]
    raise ValueError

def answer(s):
    r_indices = []
    l_indices = []

    #where are the characters? Ignore hyphens.    
    r_indices = get_char_indices('>',s)
    l_indices = get_char_indices('<',s)
    if l_indices == [] or r_indices == []:
        #no values, short circuit.
        return 0
    
    left_len = len(l_indices)
    encounters = 0
    
#    print('rights at:',r_indices)
#    print('lefts at: ',l_indices)

    for pos in r_indices:
        try:
            first_greater_left = find_gt_ndx(l_indices,pos)
        except ValueError:
            #not found
            continue
        
        encounters += left_len - first_greater_left

    return encounters * 2 # 2 salutes per encounter

assert(answer('>----<') == 2)
assert(answer('<>') == 0)
assert(answer("<<>><") == 4)
assert(answer("--->-><-><-->-") == 10)
assert(answer('') == 0)
assert(answer('>>>>>>>>>>>>>>>>>>>>>>>>>>') == 0)
assert(answer('>>>>>>>>>><<<<<<<<<<') == 200)
assert(answer('><<<<<<<<<<>>>>>>>>>') == 20)