#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 08:10:36 2018

@author: bobhilt
"""

def conditional_roulette_probs(history):
    """

    Example: 
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5}, 
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """
    numbers = {number : {} for number in history}
    for ndx, number in enumerate(history[:-1]):
        next_num = history[ndx+1]
        if not next_num in numbers[number]:
            numbers[number][next_num] = 1
        else:
            numbers[number][next_num] += 1
    
    for k,v in numbers.items():
        trials = sum(v.values())
        for subsequent_number, frequency in v.items():
            numbers[k][subsequent_number] = frequency/trials

    return numbers

conditional_roulette_probs([1, 3, 1, 5, 1])
