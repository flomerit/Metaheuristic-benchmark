# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:10:21 2021

@author: zongsing.huang
"""

import numpy as np

def test():
    Sequence = np.array([[2, 1, 3, 0],
                         [3, 0, 1, 2],
                         [1, 3, 2, 0],
                         [2, 0, 1, 3]], dtype=int)
    return Sequence

def ft06():
    Sequence = np.array([[2, 0, 1, 3, 5, 4],
                         [1, 2, 4, 5, 0, 3],
                         [2, 3, 5, 0, 1, 4],
                         [1, 0, 2, 3, 4, 5],
                         [2, 1, 4, 5, 0, 3],
                         [1, 3, 5, 0, 4, 2]], dtype=int)
    return Sequence

def ft10():
    Sequence = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [0, 2, 4, 9, 3, 1, 6, 5, 7, 8],
                         [1, 0, 3, 2, 8, 5, 7, 6, 9, 4],
                         [1, 2, 0, 4, 6, 8, 7, 3, 9, 5],
                         [2, 0, 1, 5, 3, 4, 8, 7, 9, 6],
                         [2, 1, 5, 3, 8, 9, 0, 6, 4, 7],
                         [1, 0, 3, 2, 6, 5, 9, 8, 7, 4], 
                         [2, 0, 1, 5, 4, 6, 8, 9, 7, 3],
                         [0, 1, 3, 5, 2, 9, 6, 7, 4, 8],
                         [1, 0, 2 ,6, 8, 9, 5, 3, 4, 7]], dtype=int)
    return Sequence

def ft20():
    Sequence = np.array([[0, 1, 2, 3, 4],
                         [0, 1, 3, 2, 4],
                         [1, 0, 2, 4, 3],
                         [1, 0, 4, 2, 3],
                         [2, 1, 0, 3, 4],
                         [2, 1, 4, 0, 3],
                         [1, 0, 2, 3, 4], 
                         [2, 1, 0, 3, 4],
                         [0, 3, 2, 1, 4],
                         [1, 2, 0, 3, 4],
                         [1, 3, 0, 4, 2],
                         [2, 0, 1, 3, 4],
                         [0, 2, 1, 3, 4],
                         [2, 0, 1, 3, 4],
                         [0, 1, 4, 2, 3],
                         [1, 0, 3, 4, 2],
                         [0, 2, 1, 3, 4],
                         [0, 1, 4, 2, 3],
                         [1, 2, 0, 3, 4],
                         [0, 1, 2, 3, 4]], dtype=int)
    return Sequence

def la01():
    Sequence = np.array([[1, 0, 4, 3, 2],
                         [0, 3, 4, 2, 1],
                         [3, 4, 1, 2, 0],
                         [1, 0, 4, 2, 3],
                         [0, 3, 2, 1, 4],
                         [1, 2, 4, 0, 3],
                         [3, 4, 1, 2, 0],
                         [2, 0, 1, 3, 4],
                         [3, 1, 4, 0, 2],
                         [4, 3, 2, 1, 0]], dtype=int)
    return Sequence

def la02():
    Sequence = np.array([[0, 3, 1, 4, 2],
                         [4, 2, 0, 1, 3],
                         [1, 2, 4, 0, 3],
                         [2, 1, 4, 0, 3],
                         [4, 0, 3, 2, 1],
                         [1, 0, 4, 3, 2],
                         [4, 1, 3, 0, 2],
                         [1, 0, 2, 3, 4],
                         [4, 0, 2, 1, 3],
                         [4, 2, 1, 3, 0]], dtype=int)
    return Sequence

def la03():
    Sequence = np.array([[1, 2, 0, 4, 3],
                         [2, 1, 0, 4, 3],
                         [2, 3, 4, 0, 1],
                         [4, 0, 2, 1, 3],
                         [4, 0, 1, 3, 2],
                         [4, 0, 1, 2, 3],
                         [3, 2, 0, 4, 1],
                         [4, 1, 0, 2, 3],
                         [4, 0, 3, 2, 1],
                         [4, 1, 0, 2, 3]], dtype=int)
    return Sequence