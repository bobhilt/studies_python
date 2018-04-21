#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 07:33:18 2018

@author: bobhilt
"""

def MSB( n ):
  """ returns Most Significant Non-zero Bit of n"""
  ndx = 0
  while ( 1 < n ):
    n = ( n >> 1 )
    ndx += 1
 
  return ndx
