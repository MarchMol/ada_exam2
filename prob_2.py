import numpy as np
from pprint import pprint
# Bottom up
def biggest_cross_aux(left, right, top, bottom, grid):
    N = len(grid)
    
    # Top y left: ascendiente 0,1,2, ... ,n-1
    for a in range(0,N):
        for b in range(0,N):
            if b>0:
                if grid[b][a]==1:
                    top[b][a] = top[b-1][a] + 1
                if grid[a][b]==1:
                    left[a][b] = left[a][b-1] + 1
                    
    # Bottom y right: descendiente n-1,n-2, ... ,1,0
    for a in range(N-1,-1,-1):
        for b in range(N-1,-1,-1):
            if b<N-1:
                if grid[b][a]==1:
                    bottom[b][a] = bottom[b+1][a] + 1
                if grid[a][b]==1:
                    right[a][b] = right[a][b+1] + 1
                
    return left, right, top, bottom
            

def get_best_value(left, right, top, bottom, N):
    # init
    rslt = np.zeros((N,N))
    f_i, f_j = 0, 0
    best_val = -float("inf")
    # Ciclos
    for i in range(0,N):
        for j in range(0,N):
            # Minimo, es decir, tamaño de la cruz para (i,j)
            val = min(
                left[i][j],
                right[i][j],
                top[i][j],
                bottom[i][j]
            )
            # *4 para cada direccion, y +1 contando la casilla (i,j)
            val = val*4 +1 
            if val>best_val:
                best_val = val
                # Se guarda la ubicacion
                f_i, f_j = i,j
            
            rslt[i][j] = val

    return best_val, f_i, f_j
        
def print_cross(grid, i, j, best):
    expansion = np.floor(best/4)
    tem = [row[:] for row in grid]
    tem[i][j] = "  +"
    for b in range(1,int(expansion)+1):
        tem[i][j+b] = "--"
        tem[i][j-b] = "--"
        tem[i+b][j] = "  |"
        tem[i-b][j] = "  |"
        
    for row in tem:
        print(" ".join(f"{val:3}" for val in row))

def biggest_cross(grid):
    # Init
    N = len(grid)
    left = np.zeros((N,N))
    right = np.zeros((N,N))
    top = np.zeros((N,N))
    bottom = np.zeros((N,N))
    # Calculo Bottom Up
    left, right, top, bottom = biggest_cross_aux(left, right, top, bottom, grid)
    # Obtener tamaño y posicion
    best, i, j = get_best_value(left, right, top, bottom, N)
    # Impresion
    print_cross(grid, i, j, best)
    print(f"Cruz mas grande: {best}")
    

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