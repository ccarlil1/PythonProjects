# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:38:32 2019

@author: Casey
"""

import math   

def distance(a, b):
    return math.sqrt(math.pow((a[0] - b[0]),2) + math.pow((a[1] - b[1]),2))

def in_circle(point, origin):
    if distance(point, origin) <= 1:
        return True
    else:
        return False

origin = []
point = []

print("Origin X-coordinate: ")
origin.append(float(input()))

print("Origin Y-coordinate: ")
origin.append(float(input()))

print("Test point X-coordinate: ")
point.append(float(input()))

print("Test point Y-coordinate: ")
point.append(float(input()))

print("Origin: (" + str(origin[0]) + ", " + str(origin[1]) + ")" )
print("Test Point: (" + str(point[0]) + ", " + str(point[1]) + ")" )

print("Is the point within the unit circle? " + str(in_circle(point, origin)))
