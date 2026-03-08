import numpy as np

def matrix_transpose(A):
    rows = len(A)
    cols = len(A[0])
    
    T = [[0]*rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            T[j][i] = A[i][j]
            
    return np.array(T)
            
        
        
