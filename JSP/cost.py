# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:09:32 2021

@author: zongsing.huang
"""

import numpy as np

def test():
    Cost = np.array([[2, 3, 5, 3],
                     [3, 4, 4, 4],
                     [3, 4, 6, 6],
                     [6, 2, 5, 3]])
    return Cost

def ft06():
    Cost = np.array([[1, 3, 6, 7, 3, 6],
                     [8, 5, 10, 10, 10, 4],
                     [5, 4,  8,  9,  1, 7],
                     [5, 5,  5,  3,  8, 9],
                     [9, 3,  5,  4,  3, 1],
                     [3, 3,  9, 10,  4, 1]])
    return Cost

def ft10():
    Cost = np.array([[29, 78,  9, 36, 49, 11, 62, 56, 44, 21],
                     [43, 90, 75, 11, 69, 28, 46, 46, 72, 30],
                     [91, 85, 39, 74, 90, 10, 12, 89, 45, 33],
                     [81, 95, 71, 99,  9, 52, 85, 98, 22, 43],
                     [14,  6, 22, 61, 26, 69, 21, 49, 72, 53],
                     [84,  2, 52, 95, 48, 72, 47, 65,  6, 25],
                     [46, 37, 61, 13, 32, 21, 32, 89, 30, 55],
                     [31, 86, 46, 74, 32, 88, 19, 48, 36, 79],
                     [76, 69, 76, 51, 85, 11, 40, 89, 26, 74],
                     [85, 13, 61,  7, 64, 76, 47, 52, 90, 45]])
    return Cost

def ft20():
    Cost = np.array([[29,  9, 49, 62, 44],
                     [43, 75, 69, 46, 72],
                     [91, 39, 90, 12, 45],
                     [81, 71,  9, 85, 22],
                     [14, 22, 26, 21, 72],
                     [84, 52, 48, 47,  6],
                     [46, 61, 32, 32, 30], 
                     [31, 46, 32, 19, 36],
                     [76, 76, 85, 40, 26],
                     [85, 61, 64, 47, 90],
                     [78, 36, 11, 56, 21],
                     [90, 11, 28, 46, 30],
                     [85, 74, 10, 89, 33],
                     [95, 99, 52, 98, 43],
                     [ 6, 61, 69, 49, 53],
                     [ 2, 95, 72, 65, 25],
                     [37, 13, 21, 89, 55],
                     [86, 74, 88, 48, 79],
                     [69, 51, 11, 89, 74],
                     [13, 7, 76, 52, 45]])
    return Cost

def la01():
    Cost = np.array([[21, 53, 95, 55, 34],
                     [21, 52, 16, 26, 71],
                     [39, 98, 42, 31, 12],
                     [77, 55, 79, 66, 77],
                     [83, 34, 64, 19, 37],
                     [54, 43, 79, 92, 62],
                     [69, 77, 87, 87, 93],
                     [38, 60, 41, 24, 83],
                     [17, 49, 25, 44, 98],
                     [77, 79, 43, 75, 96]])
    return Cost

def la02():
    Cost = np.array([[20, 87, 31, 76, 17],
                     [25, 32, 24, 18, 81],
                     [72, 23, 28, 58, 99],
                     [86, 76, 97, 45, 90],
                     [27, 42, 48, 17, 46],
                     [67, 98, 48, 27, 62],
                     [28, 12, 19, 80, 50],
                     [63, 94, 98, 50, 80],
                     [14, 75, 50, 41, 55],
                     [72, 18, 37, 79, 61]])
    return Cost

def la03():
    Cost = np.array([[23, 45, 82, 84, 38],
                     [21, 29, 18, 41, 50],
                     [38, 54, 16, 52, 52],
                     [37, 54, 74, 62, 57],
                     [57, 81, 61, 68, 30],
                     [81, 79, 89, 89, 11],
                     [33, 20, 91, 20, 66],
                     [24, 84, 32, 55,  8],
                     [56,  7, 54, 64, 39],
                     [40, 83, 19,  8,  7]])
    return Cost