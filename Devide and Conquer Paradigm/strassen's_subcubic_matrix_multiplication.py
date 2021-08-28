# n x n Mtricies, n is powers of 2.
# Matrix Multiplication seems straightforward ?
# strassens sub_cubic is a mind blowing example of how algorithmic ingenuity can improve over straightforward solutions.


# 1 2 3      # 9 2 4     # 1*9+2*1+3*6      1*2+2*3+3*7     1*4+2*5+3*8
# 4 5 6   x  # 1 3 5  =  # 4*9+5*1+6*6      4*2+5*3+6*7     4*4+5*5+6*8
# 7 8 9      # 6 7 8     # 7*9+8*1+9*6      7*2+8*3+9*7     7*4+8*5+8*8
# 1*9+2*1+3*6:  This line of operation is n * plus additional sums
# we need n*n of that linear work.. so Total amount of work to tradition matrix multiplication is O(n^3)


# n = int(input())
# A = []
# for i in range(0,n):
#     A.append([int(j) for j in input().split()])
# print(A)
# B = []
# for i in range(0,n):
#     B.append([int(j) for j in input().split()])
# print(B)
# =====================================
# straightforward O(n^3)
def matrix_multiplication(x, y):
    z = []
    for i in range(n):
        z.append([0]*(n))
        for j in range(n):
            z[i][j] = 0
            for k in range(n):
                z[i][j] += a[i][k] * b[k][j]
    return z
# print(matrix_multiplication(a, b))
# =====================================
# =======================================================================

# Phase0
#       X: 1   2   3   7         Y: 9   2    4   14
#          4  -5   6  -9            1  -3    5   -6
#          7   8   9  15    x       6   7    8   -4
#         -2  -1   5  -3           -8   3   11   -2
# Phase1:
#      A:  1   2      B: 3   7        E: 9   2         F: 4   14
#          4  -5         6  -9           1  -3            5   -6
#                                 x
#      C:  7   8      D: 9  15        G: 6   7         H: 8   -4
#         -2  -1         5  -3          -8   3            11  -2
# Phase2: ex-> A x E
#        a:1     b:2             e:9     f:2

#        c:4    d:-5             g:1    h:-3
# Phase3: BASE CASE
# 1 * 9 + 2 * 1
#

def sumM(X, Y):
    n = len(X)
    Z = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = X[i][j] + Y[i][j]
    return Z
# straightforward divide and conquer version
def matrix_divide_and_conquer(X, Y):
    n = len(X)
    if n == 1:
        return  [ [ X[0][0]*Y[0][0] ] ]
    else:
        A = [X[i][:n//2] for i in range( n//2 )]
        B = [X[i][n//2:] for i in range( n//2 )]
        C = [X[i][:n//2] for i in range(n//2,n)]
        D = [X[i][n//2:] for i in range(n//2,n)]

        E = [Y[i][:n//2] for i in range( n//2 )]
        F = [Y[i][n//2:] for i in range( n//2 )]
        G = [Y[i][:n//2] for i in range(n//2,n)]
        H = [Y[i][n//2:] for i in range(n//2,n)]

        # Z00
        AE = matrix_divide_and_conquer(A, E)
        BG = matrix_divide_and_conquer(B, G)
        # Z01
        AF = matrix_divide_and_conquer(A, F)
        BH = matrix_divide_and_conquer(B, H)
        # Z10
        CE = matrix_divide_and_conquer(C, E)
        DG = matrix_divide_and_conquer(D, G)
        # Z11
        CF = matrix_divide_and_conquer(C, F)
        DH = matrix_divide_and_conquer(D, H)

        Z = [[0 for x in range(n)] for y in range(n)]
        # Z[[AE+BG, AF+BH],
        #   [CE+DG, CF+DH]]

        for i in range(n):
            for j in range(n):
                Z[i][j] =

        # return

# =======================================================================
# strassens Matrix Multiplication: sub_cubic













# ==
