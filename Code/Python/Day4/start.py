# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:35:07 2019

@author: DavidSM
"""
'''
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
'''
import numpy as np
from collections import Counter

MIN_VALUE = 248345
END_VALUE = 746315

vals = np.arange(MIN_VALUE, END_VALUE, 1)

def test(number):
    digits = []
    n = 5
    while n>0:
        dig = np.floor(number/np.power(10,n))
        dig1 = np.floor((number%np.power(10,n))/np.power(10,n-1))
        #print(number, n)
        if dig <= dig1:
            digits.append(dig)
            if n == 1:
                digits.append(dig1)
            number = number%np.power(10,n)
            n -= 1
        else:
            return False
    test = Counter(digits)
    if max(test.values()) >= 2:
        return True
    return False

def test2(number):
    digits = []
    n = 5
    while n>0:
        dig = np.floor(number/np.power(10,n))
        dig1 = np.floor((number%np.power(10,n))/np.power(10,n-1))
        #print(number, n)
        if dig <= dig1:
            digits.append(dig)
            if n == 1:
                digits.append(dig1)
            number = number%np.power(10,n)
            n -= 1
        else:
            return False
    test = Counter(digits)
    for i in test.values():
        if i == 2:
            return True
    return False


check1 = np.vectorize(test)
check2 = np.vectorize(test2)

valid_vals = check1(vals)
valid_vals2 = check2(vals)

phase1 = sum(valid_vals)
phase2 = sum(valid_vals2)

print(phase1, phase2)
          