The code is done on Anaconda Spyder on Python 3.7 and recommended to perform on the same if possible

Libraries and command to install those:

    Virtual Evirobnment with Python 3.7 : conda create -n myenv python=3.7 
    Numpy : conda install -c anaconda numpy
    Matplotlib -: conda install -c conda-forge matplotlib 
    Imutils - conda install -c conda-forge imutils

Instruction to run the code:

    1. Create a Virtual Environment for python 3.7
        conda create -n myenv python=3.7
    2. Activate the Virtual Environment
        conda activate myenv 
    3. Install the Libraries and dependency
        conda install -c anaconda numpy
        conda install -c conda-forge matplotlib 
        conda install -c conda-forge imutils
    4. Then depending on which case you need to run, uncomment the corresponding line
    
        e.g In the code 
        #solve=[[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]        #Test_case_1
        #solve=[[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]       #Test_case_2
        #solve=[[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]        #Test_case_3
        #solve=[[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]         #Test_case_4
        solve=[[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]         #Test_case_5

        If you want to run for the 4th case uncomment ther line test_case_4 
        #solve=[[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]        #Test_case_1
        #solve=[[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]       #Test_case_2
        #solve=[[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]        #Test_case_3
        solve=[[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]          #Test_case_4
        #solve=[[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]        #Test_case_5

        And change the name of the file to the name of Test_case to save into corresponsding file 
        
        file1=open("test_case_5.txt","w")
        For test case 4
        file1=open("test_case_4.txt","w")

        Output in the .txt file will be in the following format

        1 6 2 3 9 5 7 4 0 10 11 8 13 14 15 12    <------ Start State 
        1 6 2 3 0 5 7 4 9 10 11 8 13 14 15 12    <-------Path points
        1 6 2 3 5 0 7 4 9 10 11 8 13 14 15 12 
        1 0 2 3 5 6 7 4 9 10 11 8 13 14 15 12 
        1 2 0 3 5 6 7 4 9 10 11 8 13 14 15 12 
        1 2 3 0 5 6 7 4 9 10 11 8 13 14 15 12 
        1 2 3 4 5 6 7 0 9 10 11 8 13 14 15 12 
        1 2 3 4 5 6 7 8 9 10 11 0 13 14 15 12 
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0    <--------Eng goal state
        
    5. Make sure the all files are in same folder and run the Project1.py


Note the test_case_1.txt is nodePath_test_case_1.txt
