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
    
    def string(self,solve_t):
        """
        Converts the list of the state into string for easy comparison 
        when further converted into integer

        Parameters
        ----------
        solve_t : List
            List which contains the state of the game

        Returns
        -------
        c : str
            String of the state 

        """
        #print("solve_t",solve_t)
        c=""
        for i in solve_t:
            for j in i:
                if(j<10):
                    c=str(c)+("0"+str(j))
                else:
                    c=c+str(j)
        return c
    
    
    def is_goal_reached(self,c):
        """
        Checking if the goal is attained by the current state.
        If not attended then adds the selected state to the expanded
        list
        Parameters
        ----------
        c : str
            String with selected state.

        Returns
        -------
        int
            1 : If goal state is attended
            0 : If goal state is  not atttended

        """  
        
        #print(self.counter)
        #print(self.orignal_representation[c])
        #sleep(5)
        #print("int(c)",int(c))
        if int(c)==int(self.ground_truth_str):
            
            return 1
            
        else:
            self.expanded.append(c)
            return 0
        
        
    
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
    
    def calculate(self,solve,pos_0,pos_1):
        
        """
        Recursive function that  selects which move is best to reach 
        the  goal and verifies the new state if it is goal or not 
        and if it is it will stop recurssion.

        Parameters
        ----------
        solve : List
            List of the state on which actions need to be taken
        pos_0 : int
            x position/row index of zero in hte list
        pos_1 : int
            y position/column index of zero in hte list

        Returns
        -------
        path : List
            Returns the optimal path that needs to be followed
            to reach from start goal to end goal0

        """
        
        #self.counter=self.counter+1
        self.counter=self.counter
        #print("counter that is updating",self.counter)
        current_t=deepcopy(solve)
        #Action called
        self.right_move(current_t,pos_0,pos_1)
        self.left_move(current_t,pos_0,pos_1)
        self.up_move(current_t,pos_0,pos_1)
        self.down_move(current_t,pos_0,pos_1)
        #print("self_frontier",self.frontier)
        
        # Selected the best action from the frontier with the help of cost
        c=min(self.frontier,key=self.frontier.get)
        #print(c)
        
        # The explored node is deleted from the Frontier node and is added
        #to the expaneded node
        
        solve=self.orignal_representation[c]
        #print(solve)
        #c=i
        #print("min_c",c)
        del self.frontier[c]
        
        self.expanded.append(c)
        boolean=self.is_goal_reached(c)         
        path=[]   
        #print("boolean",boolean)
        if boolean==0:
            pos_0,pos_1=self.find_zero(solve)
            return self.calculate(solve, pos_0, pos_1)
            
        elif boolean==1:
            #Appends the path that need to be followed
            #by getting the parents of the nodes recursively
            
            loop=self.parent_orignal_data[self.ground_truth_str]
            
            #print(self.expanded)
            #print(loop)
            path.append(self.ground_truth_str)
            while(int(self.start_str)!= int(loop)):
                path.append(loop)
                #sleep(5)
                loop=self.parent_orignal_data[loop]
                #print(loop)
            path.append(self.start_str)
            #print(path)
            #print(self.expanded)
            return path
    
    
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
        #Checks if the move is possible 
        if pos_1>0:
            #solve_t=solve_a
            solve_t=deepcopy(list(solve_a))
            # Makes the move and gives the updated state
            pos_1=pos_1-1
            temp=solve_t[pos_0][pos_1]
            solve_t[pos_0][pos_1]=0
            solve_t[pos_0][pos_1+1]=temp
            #Converted to string for easy comparision and representation
            score=self.string(solve_t)
            temp1=deepcopy(list(solve_a))
            parent_score=self.string(temp1)
            
            cost=self.cost(solve_t)
            
            #Checks if the current node lies in the expanded nodes so 
            #that the pathobtained  is acyclic
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