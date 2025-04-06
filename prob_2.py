import numpy as np
from pprint import pprint
# Bottom up
def biggest_cross_aux(left, right, top, bottom, grid):
    N = len(grid)
    
    # Calculo de matrices left, right, top y down 
    for a in range(0,N):
        for b in range(0,N):
            if b>0:
                if grid[b][a]==1:
                    top[b][a] = top[b-1][a] + 1
                if grid[a][b]==1:
                    left[a][b] = left[a][b-1] + 1
            
    for a in range(N-1,-1,-1):
        for b in range(N-1,-1,-1):
            if b<N-1:
                if grid[b][a]==1:
                    bottom[b][a] = bottom[b+1][a] + 1
                if grid[a][b]==1:
                    right[a][b] = right[a][b+1] + 1
                
    # optimizacio
    rslt = np.zeros((10,10))
    f_i, f_j = 0, 0
    best_val = -float("inf")
    for i in range(0,N):
        for j in range(0,N):
            val = min(
                left[i][j],
                right[i][j],
                top[i][j],
                bottom[i][j]
            )
            if val>best_val:
                best_val = val
                f_i, f_j = i,j
            # print(f"{i},{j}:\n L {left[i][j]} R {right[i][j]} T {top[i][j]} B {bottom[i][j]}\n Min {val}\n\n")
            rslt[i][j] = val
    return best_val, f_i, f_j
            
    

def print_cross(grid, i, j, best):
    tem = [row[:] for row in grid]
    tem[i][j] = "  +"
    for b in range(1,int(best)):
        tem[i][j+b] = "--"
        tem[i][j-b] = "--"
        tem[i+b][j] = "  |"
        tem[i-b][j] = "  |"
        
    for row in tem:
        print(" ".join(f"{val:3}" for val in row))

        

def biggest_cross(grid):
    left = np.zeros((10,10))
    right = np.zeros((10,10))
    top = np.zeros((10,10))
    bottom = np.zeros((10,10))
    best, i, j = biggest_cross_aux(left, right, top, bottom, grid)
    print(best)
    print_cross(grid, i, j, best)

grid_ = [
    [1,0,1,1,1,1,0,1,1,1],
    [1,0,1,0,1,1,1,0,1,1],
    [1,1,1,0,1,1,0,1,0,1],
    [0,0,0,0,1,0,0,1,0,0],
    [1,1,1,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,0],
    [1,0,0,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,0,0,1,1],
    [1,1,0,0,1,0,1,0,0,1],
    [1,0,1,1,1,1,0,1,0,0],
]
biggest_cross(grid_)