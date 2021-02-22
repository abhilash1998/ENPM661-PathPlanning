#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:25:46 2021

@author: abhi
"""


"""
Main body of the code . Goal state is saved in the variable. 
Gets the goal state calls the functions from the class Fifteen_board
to solve the path planning problem i.e. Calculate the optimal path from
start goal to end goal. The p[ath is recieved as an output
That output is then saved to the text.                          

The time is optimised by assigning a cost function to every state which
 is consider while deciding the path 
"""

import numpy as np
from Fifteen_board import Fifteen_board


data=[]


#solve=[[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]        #Test_case_1
#solve=[[1, 0, 3, 4],[ 5, 2, s7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]       #Test_case_2
#solve=[[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]        #Test_case_3
#solve=[[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]         #Test_case_4
solve=[[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]         #Test_case_5
Fifteen_board=Fifteen_board(solve)
pos_x,pos_y=Fifteen_board.find_zero(solve)  #gets the x,y location of zero
explored=Fifteen_board.calculate(solve,pos_x,pos_y) # Calculates the optimal path



explored.reverse()

# Code to save the text in the output
file1=open("test_case_5.txt","w")
for element in explored:
    for n in range(0,len(element),2):
        entry=int(element[n:n+2])
        file1.write(str(entry))
        file1.write(" ")
    file1.write("\n")
    
file1.close()