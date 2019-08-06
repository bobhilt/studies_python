#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:26:20 2018

@author: bobhilt
power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

For extracting tests:
* no need for adding test-run code to main file(s), e.g,
** if __name__ == '__main__':
**    unittest.main()
* create ./tests folder
* create ./tests/__init__.py to hook up the path
* create test_*.py files
* command palette: configure tests
** in this case: unittest; tests folder; test files named test_*.py
* command palette: show test output
* discover tests

"""


def power_digit_sum(power):

    total = 0

    # if power < 0:
    #     raise ValueError("power must be a positive integer")

    number = pow(2,power)
    
    while number:
        number, digit = divmod(number, 10)
        total += digit

    return total

