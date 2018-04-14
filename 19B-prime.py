# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 12:55:25 2018

@author: jungw
"""

x = int(input("? "))
d = 2

while d <= x:
    if x % d == 0:
        print(d)
        x = x / d
    else:
        d = d + 1