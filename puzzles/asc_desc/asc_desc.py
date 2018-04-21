#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:31:10 2018

@author: bobhilt
ascending descending sort puzzle
"""
from operator import itemgetter

def get_asc_desc_values(l,n):
    #l = list of tuples
    #n = index into list
    # returns 2nd + 3rd value at index n
    s=sorted(sorted(l, key=itemgetter(2), reverse=True),key=itemgetter(0))
    t = s[n]
    return t[1] + t[2]

with open('asc_desc.csv') as f:
   mylist = [l.strip("\n").split(",") for l in f.readlines()]
   mylist = [[t[0], int(t[1]), float(t[2])] for t in mylist]

#################################################################
print ("500th asc_desc value:",get_asc_desc_values(mylist,499))
#################################################################

########################3
import unittest

class TestGetAscDesc(unittest.TestCase):
    
    def test_sample(self):

        l = [
            ('conductions',2,300.001),
            ('fitchews',5,500.002),
            ('mulches',8,700.003),
            ('conductions',3,500.001),
            ('fitchews',1,600.002),
            ('mulches',5,600.003),
            ('conductions',6,400.001),
            ('mulches',7,500.003)]
        
        self.assertEqual(get_asc_desc_values(l,4), 505.002)
        



if __name__ == '__main__':
    unittest.main()



with open('asc_desc.csv') as f:
     mylist = [l.strip("\n").split(",") for l in f.readlines()]