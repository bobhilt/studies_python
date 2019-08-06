#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 07:50:33 2018

@author: bobhilt
"""

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    found = list()
    table = str.maketrans(dict.fromkeys(',.?'))
    
    for doc_index, doc in enumerate(doc_list):
        words = doc.lower().translate(table).split(' ')
        if keyword.lower() in words:
            found.append(doc_index)
    return found

