
def nokia_teclas_aux(a, n, memo,d):
    if memo[n-1][d-1] != 0:
        return memo[n-1][d-1]
    if n == 1:
        q = 0
    else:
        q= -10000
        for i in range(1,n):
            tem = 0
            for j in range(0,10):
                tem+= nokia_teclas_aux(a,i-1,memo,j)
            q = max(
                q,
                len(a[i-1]) + tem
            )
        memo[n-1][d-1] = q
    return q

def nokia_teclas(a,n):
    memo = [[0]*10]*n
    val = 0
    for i in range(0,10): # 0-9
        val+= nokia_teclas_aux(a,n,memo,i)
    return val
   
# 1 2 3
# 4 5 6
# 7 8 9
#   0
#      0  1  2  3  4  5  6  7  8  9
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
n_ = 2
rslt = nokia_teclas(a_,n_)
print(rslt)

