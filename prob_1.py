
def nokia_teclas_aux(a, n, memo,d):
    # Si existe memoizacion, usar esa
    if memo[n-1][d] != 0:
        return memo[n-1][d]
    # si es caso base, solo obtener cuantos adyacentes hay
    if n == 1:
        q = len(a[d])
    # Recursion
    else:
        q = 0
        # Para todas las adyacencias, del digito actual, recursion
        for j in a[d]:
            q+=nokia_teclas_aux(a,n-1,memo,j)
        # Guardar en memoizacion (no hay que maximizar, solo guardar)
        memo[n-1][d] = q
    return q

def nokia_teclas(a,n):
    # Inicializacion de memoizacion
    memo = []
    for i in range(0,n):
        tem = []
        for i in range(0,10):
            tem.append(0)
        memo.append(tem)
    # suma de 
    rslt_ = 0
    for i in range(0,10): # para todos los botones 0-9
        rslt_+= nokia_teclas_aux(a,n,memo,i)
    return rslt_
   
# 1 2 3
# 4 5 6
# 7 8 9
#   0

# adyacencia
a_ = {
    0: [0,8],
    1: [1,2,4],
    2: [1,2,3,5],
    3: [2,3,6],
    4: [1,4,5,7],
    5: [2,4,5,6,8],
    6: [3,5,6,9],
    7: [4,7,8],
    8: [5,7,8,9,0],
    9: [6,8,9]
}
# n
n_ = 1
# resultado
rslt = nokia_teclas(a_,n_)
print(rslt)

