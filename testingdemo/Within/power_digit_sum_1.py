#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:26:20 2018

@author: bobhilt
power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def power_digit_sum(power):
    total = 0
    number = pow(2,power)
    
    while number:
        number, digit = divmod(number, 10)
        total += digit

    return total

import unittest
class PowerDigitSum(unittest.TestCase):

    def test_15(self):
        self.assertEqual(power_digit_sum(15),26)

    def test_10(self):
        self.assertEqual(power_digit_sum(10),7)
        
if __name__ == '__main__':
    unittest.main()