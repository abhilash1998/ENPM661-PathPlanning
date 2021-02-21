#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:23:48 2021

@author: abhi
"""
from copy import deepcopy
from time import sleep
#import pandas
class Fifteen_board:
    def __init__(self):
        self.ground_truth={}
        for keys in range(15):
            self.ground_truth[keys+1]=(keys//4,keys%4)
            
        
        self.ground_truth[0]=(3,3)
        #print('ground_truth',self.ground_truth)
        self.expanded=[]
        self.ground_truth_str="01020304050607080910111213141500"
        self.ground_truth_list=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        self.cost_data={}
        self.parent_orignal_data={}
        self.orignal_representation={}
        self.frontier={}
        self.counter=0
    def left_move(self,solve_a,pos_0,pos_1):
        """
        
        This function moves the zero to left of the list
        
        Parameters
        ----------
        solve_a: List
            It is a list of the current state from which the 
            number zero is moved to the left
        pos_zero : List
            List stores the position of zero.
    
        Returns
        -------
        New list encorporating new movement if possible or None.
    
        """
        if pos_1>0:
            #solve_t=solve_a
            solve_t=deepcopy(list(solve_a))
            temp=deepcopy(list(solve_a))
            pos_1=pos_1-1     
            temp=solve_t[pos_0][pos_1]
            solve_t[pos_0][pos_1]=0
            solve_t[pos_0][pos_1+1]=temp
            score=self.string(solve_t)
            self.parent_orignal_data[score]=[solve_t,temp]
            cost=self.cost(solve_t)
            
            for data in self.expanded:
                if int(score)== int(data):
                    #print("Present")
                    return None
                
                    break
            #self.cost_data[score]=cost    
            self.frontier[score]=cost   
            self.orignal_representation[score]=solve_t
            return solve_t
    