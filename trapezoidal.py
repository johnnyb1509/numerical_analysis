# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:18:28 2020

@author: Nguyen Son
"""
import numpy as np
import math
import pandas as pd
#=============================================================================
"""COMPUTING INTEGRAL"""

# TRAPEZOIDAL:
def trapezoidal(f, a, b, n = 100):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1,n):
        result += f(a+i*h)
    result *= h
    return result

v = lambda t: 3*(t**2)*math.exp(t**3)
n = 4
num = trapezoidal(v, 0, 1)
print(num)
