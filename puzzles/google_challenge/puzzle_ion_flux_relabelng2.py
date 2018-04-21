#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ion_flux_relabeling2.py
BinaryTreeParentslist
google foobar challenge, 'ion_flux_relabeling' 

Return a list of parent vertices from a list of nodes.
This version is memory-efficient because it doesn't build the whole tree (2**h-1 nodes)
Performance - O(log n)

Created on Fri Apr 20 18:43:36 2018

@author: bobhilt

Algorithm described:
https://stackoverflow.com/questions/20405346/getting-parent-of-a-vertex-in-a-perfect-binary-tree?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
"""

"""    

1  While ((x+1) & x) != 0 and ((x+2) & (x+1)) != 0 repeat step 2.
# Until x is in one of the two left-most positions of level.
2. Clear most-significant non-zero bit and add 1. Accumulate the difference.
# Move x to same relative position of next left subtree (divide problem in half)
3. If ((x+1) & x) == 0, multiply by 2 and add 1; otherwise if ((x+2) & (x+1)) == 0, add 1.
# parent of left child of left-most branch. is 2x+1. parent of right is x+1
4. Add back all differences accumulated on step 2.
# parents have same relative differences

For example, 12 (in binary form 0b1100) is transformed on step #2 to 0b0101, 
then to 0b0010 (or 2 in decimal). Accumulated difference is 10. Step #3 adds 1 and step #4 adds back  10, so the result is 13.

Other example: 10 (in binary form 0b1010) is transformed on step #2 to 0b0011 (or 3 in decimal). Step #3 doubles it (6), then adds 1 (7). Step #4 adds back accumulated difference (7), so the result is 14.
"""
def MSB( n ):
  """ returns Most Significant Bit of n"""
  ndx = 0
  while ( 1 < n ):
    n = ( n >> 1 )
    ndx += 1
 
  return ndx

def get_parent(n,h):
    """
    returns parent node of complete/perfect post-order traversal binary tree.
    -1 if not in scope of tree of h levels.
    """
    if n < 1 or n >= 2**h -1:
        return -1
    
    accumulator = 0
    x = n
    delta = 0
    #get lefmost sib
    while ((x+1) & x) and ((x+2) & (x+1)):
        delta = 2**MSB(x) - 1
        accumulator += delta
        x -= delta

    #then calculate parent
    if ((x+1) & x) == 0: 
        x = x * 2 + 1; 
    
    elif ((x+2) & (x+1)) == 0:
        x+= 1.
    
    x += accumulator
    return int(x)

def answer(h, q):
    answer = [get_parent(x,h) for x in q]
    return answer