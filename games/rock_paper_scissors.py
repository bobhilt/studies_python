#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple rock-paper-scissors implementation - code study
Focus on simple but solid principles. 
Iteration ideas: 
    - player v computer
    - add file for results
    - add machine learning 
    - graphics / web
    - computer vs computer (tournament)
Created on Sat Jun 16 08:16:27 2018

@author: bobhilt
"""
from random import choice

class rps(object):
    def __eq__(self, other):
        return isinstance(self, type(other))
    def __str__(self):
        return('rock paper scissors choice')

class rock(rps):
    def __lt__(self,other):
        return isinstance(other,paper)
    def __str__(self):
        return 'rock'
class paper(rps):
    def __lt__(self,other):
        return isinstance(other,scissors)
    def __str__(self):
        return 'paper'
class scissors(rps):
    def __lt__(self,other):
        return isinstance(other,rock)
    def __str__(self):
        return 'scissors'

    
def compare(x,y):
    
    if x == y:
        return 0
    if x < y:
        return -1
    else:
        return 1
    
choices = (rock(), paper(), scissors())

def play_round(verbose=True):
    x = choice(choices)
    y = choice(choices)
    result = compare(x,y)
    values = {0 : "draw", -1: "Player 2 wins.", 1 : "Player 1 wins"}
    if verbose:
        print('{0} vs {1}: {2}'.format(x,y, values[result]))
        
    return result

score = 0
rounds= 10000
draws = 0
wins = 0
losses = 0
for _ in range(rounds):
    round_score = play_round(verbose=False)
    score += round_score
    draws += round_score == 0
    wins += round_score == 1
    losses += round_score == -1
print('Player 1 is  {0}-{1}-{2} ({5}) over {3} rounds, score {4}'.format(wins, losses, draws, rounds, score,wins/losses))
