#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:18:41 2018

@author: bobhilt
"""

class Proxy(object):
    def __init__(self, target_object):
        # WRITE CODE HERE
        # object.__setattr__(self, '_messages', [])
        self._messages = []
        #initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object

    # WRITE CODE HERE
    def __getattr__(self, attr):
        self._messages.append(attr)
        # return getattr(self._obj, attr)
        return self._obj.__getattribute__(attr)

    def __setattr__(self, attr, value):
        if attr != '_obj':
            self._messages.append(attr)
        setattr(self._obj, attr, value)
        
    def messages(self):
        return self._messages
        
    def was_called(self, attr):
        return attr in self._messages

    def number_of_times_called(self, attr):
        return self._messages.count(attr)

proxy = Proxy("hello there")
