#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:23:48 2021

@author: abhi
"""
from copy import deepcopy
from time import sleep

class Fifteen_board:
    def __init__(self,solve):
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
        self.start=deepcopy(solve)
        self.start_str=self.string(self.start)
        #self.expanded.append(self.ground_truth_str)
    def find_zero(self,solve):
        """
        
        This function finds the position of 0 in the list and return 
        the corresponding index
        Parameters
        ---------
        solve:List
            It is a list of the state from which the index of 0 
            needs to be found
         
        Returns
        -------
        i,j - Int
            Index position of 0 in the list solve
        """
        
        for i,x in enumerate(solve):
            if 0 in x:
                j=x.index(0)
                break
        return i,j
    
    def cost(self,R,h=4):
        """
        
        This Function calculates cost for each move/action

        Parameters
        ----------
        R : the new configuration/state for which cost needs
        to be calculated
        h : length of the board

        Returns
        -------
        cost : Int
            It is the cost of the state i.e. its an factor to 
            decide how close it is to the final/desired state

        """
        #c=0
        cost=0
        for ab in range(h):
            for ac in range(h):
                gx,gy=self.ground_truth[R[ab][ac]]
                
                c=abs(ab-gx)+abs(ac-gy)
                cost=cost+c
        final_counter=self.counter+cost
        #print(final_counter)
        #print(R)
        return final_counter
    
    
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
        solve_t:List
            New list encorporating new movement if possible or None.
    
        """
        if pos_1>0:
            #solve_t=solve_a
            solve_t=deepcopy(list(solve_a))
            
            pos_1=pos_1-1
            temp=solve_t[pos_0][pos_1]
            solve_t[pos_0][pos_1]=0
            solve_t[pos_0][pos_1+1]=temp
            score=self.string(solve_t)
            temp1=deepcopy(list(solve_a))
            parent_score=self.string(temp1)
            
            cost=self.cost(solve_t)
            
            for data in self.expanded:
                if int(score)== int(data):
                    #print("Present")
                    return None
                
                    break
            #self.cost_data[score]=cost    
            self.parent_orignal_data[score]=parent_score
            self.frontier[score]=cost   
            self.orignal_representation[score]=solve_t
            return solve_t
    
    def right_move(self,solve_a,pos_0,pos_1):
        """
        
        This function moves the zero to right of the list
        
      
    
        Parameters
        ----------
        solve_a : List
            It is a list of the current state from which the 
            number zero is moved to the right
        pos_zero : List
            List stores the position of zero.
    
        Returns
        -------
        solve_t:List
            New list encorporating new movement if possible or None.
    
        """
        if pos_1<len(solve_a)-1:
            solve_t=deepcopy(list(solve_a))
            pos_1=pos_1+1     
            temp=solve_t[pos_0][pos_1]
            solve_t[pos_0][pos_1]=0
            solve_t[pos_0][pos_1-1]=temp
            score=self.string(solve_t)
            temp1=deepcopy(list(solve_a))
            parent_score=self.string(temp1)
            
            cost=self.cost(solve_t)
            #score=self.string(solve_t)
            #self.parent_orignal_data[score]=[solve_t,temp]
            cost=self.cost(solve_t)

                    
            for data in self.expanded:
                if int(score)== int(data):
                    #print("Present")
                    return None
                
                    break
            self.parent_orignal_data[score]=parent_score
            self.frontier[score]=cost 
            self.orignal_representation[score]=solve_t
            return solve_t
    
    
    def down_move(self,solve_a,pos_0,pos_1):
        """
        
        This function moves the zero to down of the list
        
      
    
        Parameters
        ----------
        solve_a : List
            It is a list of the current state from which the 
            number zero is moved to the down
        pos_zero : List
            List stores the position of zero.
    
        Returns
        -------
        solve_t:List
            New list encorporating new movement if possible or None.
    
        """
        if pos_0<len(solve_a)-1:
            solve_t=deepcopy(list(solve_a))
            pos_0=pos_0+1     
            temp=solve_t[pos_0][pos_1]
            solve_t[pos_0][pos_1]=0
            solve_t[pos_0-1][pos_1]=temp
            score=self.string(solve_t)
            temp1=deepcopy(list(solve_a))
            parent_score=self.string(temp1)
            
            cost=self.cost(solve_t)
            #self.parent_orignal_data[score]=[solve_t,temp]
            #cost=self.cost(solve_t)
            
            for data in self.expanded:
                if int(score)== int(data):
                    #print("Present")
                    return None
                
                    break
            self.parent_orignal_data[score]=parent_score
            self.frontier[score]=cost 
            self.orignal_representation[score]=solve_t
            return solve_t
    """    for i in self.expanded:
            if int(i)=="""
    
    
    def up_move(self,solve_a,pos_0,pos_1):
        """
        
        This function moves the zero to down of the list
        
      
    
        Parameters
        ----------
        solve_a : List
            It is a list of the current state from which the 
            number zero is moved to the down
        pos_zero : List
            List stores the position of zero.
    
        Returns
        -------
        solve_t:List
            New list encorporating new movement if possible or None.
    
        """
        if pos_0>0:
            solve_t=deepcopy(list(solve_a))
            pos_0=pos_0-1     
            temp=solve_t[pos_0][pos_1]
            solve_t[pos_0][pos_1]=0
            solve_t[pos_0+1][pos_1]=temp
            score=self.string(solve_t)
            temp1=deepcopy(list(solve_a))
            parent_score=self.string(temp1)
            
            cost=self.cost(solve_t)
            #print(self.expanded)
            #print("111")
            #self.parent_orignal_data[score]=[solve_t,temp]
            #cost=self.cost(solve_t)
            
            for data in self.expanded:
                if int(score)== int(data):
                    #print("Present")
                    return None
                
                    break
            self.parent_orignal_data[score]=parent_score
            self.frontier[score]=cost 
            self.orignal_representation[score]=solve_t
            return solve_t