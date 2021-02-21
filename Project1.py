#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:25:46 2021

@author: abhi
"""

import numpy as np
from Fifteen_board import Fifteen_board


data=[]


#solve=[[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]
#solve=[[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]
#solve=[[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]
#solve=[[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]"
solve=[[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]
Fifteen_board=Fifteen_board(solve)
pos_x,pos_y=Fifteen_board.find_zero(solve)
explored=Fifteen_board.calculate(solve,pos_x,pos_y)
#solve.index(1)


explored.reverse()
file1=open("test_case_5.txt","w")
for element in explored:
    for n in range(0,len(element),2):
        entry=int(element[n:n+2])
        file1.write(str(entry))
        file1.write(" ")
    file1.write("\n")
    
file1.close()