import math
import numpy as np
import utils
import copy


def Tetris(target):

    import copy
    target2 = copy.deepcopy(target)
    row = len(target)
    col = len(target[0])
   
    
    solution = np.zeros((row,col), dtype = 'i,i').tolist()    
    
    count = 0 #starts the count at zero for the second element of each tuple
    for i in range(row): #defining index range for i and j (i = number of rows, j = number of columns)
        for j in range(col):
            #the next line restricts the i and j value to be below whatever is defined in the shape ID eg for j+2 the restraint is if j <= col + 3
            if i <= row - 2 and j <= col -2 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+1][j+1] == 1 and target[i][j+1] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i][j+1] == (0,0):
                    count = count + 1 #increase count by 1 each time
                    solution[i][j] = (1,count) #place piece at coordinate
                    solution[i+1][j] = (1,count)
                    solution[i+1][j+1] = (1,count)
                    solution[i][j+1] = (1,count) 
            #Saying that if the piece fits in a given coordinate, place it. Very basic but finds a moderately accurate solution very quickly.
            
            #now repeat for each piece until no pieces can be placed
            
            
            if i <= row - 4 and j <= col -1 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+2][j] == 1 and target[i+3][j] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0) and solution[i+3][j] == (0,0):
                    count = count + 1
                    solution[i][j] = (2,count)
                    solution[i+1][j] = (2,count)
                    solution[i+2][j] = (2,count)
                    solution[i+3][j] = (2,count)



            if i <= row - 1 and j <= col -4 and target[i][j] == 1 and target[i][j+1] == 1 and target[i][j+2] == 1 and target[i][j+3] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0) and solution[i][j+3] == (0,0):
                    count = count + 1
                    solution[i][j] = (3,count)
                    solution[i][j+1] = (3,count)
                    solution[i][j+2] = (3,count)
                    solution[i][j+3] = (3,count)
                
            if i <= row - 3 and j <= col -2 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+2][j] == 1 and target[i+2][j+1] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0) and solution[i+2][j+1] == (0,0):
                    count = count + 1
                    solution[i][j] = (4,count)
                    solution[i+1][j] = (4,count)
                    solution[i+2][j] = (4,count)
                    solution[i+2][j+1] = (4,count)

            if i <= row - 2 and j >= 2 and target[i][j] == 1 and target[i+1][j-2] == 1 and target[i+1][j-1] == 1 and target[i+1][j] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j-2] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+1][j] == (0,0):
                    count = count + 1
                    solution[i][j] = (5,count)
                    solution[i+1][j-2] = (5,count)    
                    solution[i+1][j-1] = (5,count)
                    solution[i +1][j] = (5,count)            
            
            if i <= row - 3 and j <= col - 2 and target[i][j] == 1 and target[i][j+1] == 1 and target[i+1][j+1] == 1 and target[i+2][j+1] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+2][j+1] == (0,0):
                    count = count + 1
                    solution[i][j] = (6,count)
                    solution[i][j+1] = (6,count)    
                    solution[i+1][j+1] = (6,count)
                    solution[i+2][j+1] = (6,count) 

            if i <= row - 3 and j <= col -3 and target[i][j] == 1 and target[i][j+1] == 1 and target[i][j+2] == 1 and target[i+1][j] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0) and solution[i+1][j] == (0,0):
                    count = count + 1
                    solution[i][j] = (7,count)
                    solution[i][j+1] = (7,count)
                    solution[i][j+2] = (7,count)
                    solution[i+1][j] = (7,count)
            
            if i <= row - 3 and j >= 1 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+2][j-1] == 1 and target[i+2][j] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j-1] == (0,0) and solution[i+2][j] == (0,0):
                    count = count + 1 
                    solution[i][j] = (8,count)
                    solution[i+1][j] = (8,count)
                    solution[i+2][j-1] = (8,count)
                    solution[i+2][j] = (8,count)
        
            if i <= row - 2 and j <= col -3 and target[i][j] == 1 and target[i][j+1] == 1 and target[i][j+2] == 1 and target[i+1][j+2] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0) and solution[i+1][j+2] == (0,0):
                    count = count + 1 
                    solution[i][j] = (9,count)
                    solution[i][j+1] = (9,count)
                    solution[i][j+2] = (9,count)
                    solution[i+1][j+2] = (9,count)  
        
            if i <= row - 3 and j <= col -2 and target[i][j] == 1 and target[i][j+1] == 1 and target[i+1][j] == 1 and target[i+2][j] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0):
                    count = count + 1 
                    solution[i][j] = (10,count)
                    solution[i][j+1] = (10,count)
                    solution[i+1][j] = (10,count)
                    solution[i+2][j+1] = (10,count)              
        
            if i <= row - 2 and j <= col -3 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+1][j+1] == 1 and target[i+1][j+2] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+1][j+2] == (0,0):
                    count = count + 1 
                    solution[i][j] = (11,count)
                    solution[i+1][j] = (11,count)
                    solution[i+1][j+1] = (11,count)
                    solution[i+1][j+2] = (11,count)     
        
            if i <= row - 3 and j <= col -2 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+1][j+1] == 1 and target[i+2][j] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+2][j] == (0,0):
                    count = count + 1 
                    solution[i][j] = (12,count)
                    solution[i+1][j] = (12,count)
                    solution[i+1][j+1] = (12,count)
                    solution[i+2][j] = (12,count)
        
            if i <= row - 2 and j <= col -2 and j >= 1 and target[i][j] == 1 and target[i+1][j-1] == 1 and target[i+1][j] == 1 and target[i+1][j+1] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0):
                    count = count + 1 
                    solution[i][j] = (13,count)
                    solution[i+1][j-1] = (13,count)
                    solution[i+1][j] = (13,count)
                    solution[i+1][j+1] = (13,count)    
        
            if i <= row - 3 and j >= 1 and target[i][j] == 1 and target[i+1][j-1] == 1 and target[i+1][j] == 1 and target[i+2][j] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0):
                    count = count + 1
                    solution[i][j] = (14,count)
                    solution[i+1][j-1] = (14,count)
                    solution[i+1][j] = (14,count)
                    solution[i+2][j] = (14,count)
        
            if i <= row - 2 and j <= col -3 and target[i][j] == 1 and target[i][j+1] == 1 and target[i][j+2] == 1 and target[i+1][j+1] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0) and solution[i+1][j+1] == (0,0):
                    count = count + 1
                    solution[i][j] = (15,count)
                    solution[i][j+1] = (15,count)
                    solution[i][j+2] = (15,count)
                    solution[i+1][j+1] = (15,count)
        
            if i <= row - 2 and j <= col -2 and j >= 1 and target[i][j] == 1 and target[i][j+1] == 1 and target[i+1][j-1] == 1 and target[i+1][j] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+1][j] == (0,0):
                    count = count + 1
                    solution[i][j] = (16,count)
                    solution[i][j+1] = (16,count)
                    solution[i+1][j-1] = (16,count)
                    solution[i+1][j] = (16,count)
        
            if i <= row - 3 and j <= col -2 and target[i][j] == 1 and target[i+1][j] == 1 and target[i+1][j+1] == 1 and target[i+2][j+1] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+2][j+1] == (0,0):
                    count = count + 1
                    solution[i][j] = (17,count)
                    solution[i+1][j] = (17,count)
                    solution[i+1][j+1] = (17,count)
                    solution[i+2][j+1] = (17,count)
        
        
            if i <= row - 2 and j <= col -3 and target[i][j] == 1 and target[i][j+1] == 1 and target[i+1][j+1] == 1 and target[i+1][j+2] == 1:
                if solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+1][j+2] == (0,0):
                    count = count + 1
                    solution[i][j] = (18,count)
                    solution[i][j+1] = (18,count)
                    solution[i+1][j+1] = (18,count)
                    solution[i+1][j+2] = (18,count)
        
            if i <= row - 3 and j >= 1 and target[i][j] == 1 and target[i+1][j-1] == 1 and target[i+1][j] == 1 and target[i+2][j-1] == 1:
                if solution[i][j] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j-1] == (0,0):
                    count = count + 1
                    solution[i][j] = (19,count)
                    solution[i+1][j-1] = (19,count)
                    solution[i+1][j] = (19,count)
                    solution[i+2][j-1] = (19,count)
    
    return solution