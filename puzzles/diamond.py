#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 07:18:35 2018

@author: bobhilt
"""

def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    def get_row(row, height):
        top_half = row < height / 2
        if top_half:
            first, second = "/", "\\"
            pad = ' ' * (height//2 - row -1)
            marks = row + 1
        else:
            first, second = "\\", "/"
            pad = ' ' * (row - height//2)
            marks = height - row
        answer = pad

        for c in range(marks):
            answer += first
        for c in range(marks):
            answer += second
        
        return answer

    diamond_str = ""
    for i in range(height):
        if i > 0:
            diamond_str += '\n'
        diamond_str += get_row(i,height) 
    return diamond_str

print(diamond(8))
