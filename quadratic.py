# -*- coding: utf-8 -*-
#求解一元二次方程
import math
def quadratic(a, b, c):
    for i in (a, b, c):
        if not isinstance(i, (int, float)):
            raise TypeError('bad operand type')
    if(a == 0):
        if(b == 0):
            if(c != 0):
                return '方程不成立'
            return '方程无解'
        return (-c / b)
    elif(b*b > 4*a*c):
        return (math.sqrt(b*b - 4*a*c) - b) / (2*a) , (-math.sqrt(b*b - 4*a*c) - b) / (2*a)
    elif(b*b == 4*a*c):
        return -b/(2*a)
    return '方程不成立'