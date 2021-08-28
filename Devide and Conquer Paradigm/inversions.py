#     [ 1 2 3 4 5 6 ]   # standard
# A = [ 1 3 5 2 4 6 ]:
# inversions? 4,  (3, 2) (5, 2) (5, 4)



A   = [1, 3, 5, 2, 4, 6]
A2  = [6, 2, 4, 3, 1, 5]

# Brute Force
# O(n^2)
def countInv_nn(arr):
    numInv = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # print(arr[i], arr[j])
            if arr[i] > arr[j]:
                numInv = numInv + 1
    return numInv
print(countInv_nn(A))
# ==============================================================================
# 0:                                [1, 5, 3, 2, 4, 6]
# 1:                     [1, 5, 3]                     [2, 4, 6]
# 2:                 [1]          [5, 3]            [2]         [4, 6]
# 3:                             [5]   [3]                     [4]   [6]
def countSplitInv_nn(first, second):
    inversions = 0
    for x in range(len(first)):
        for y in range(len(second)):
            if first[x] > second[y]:
                inversions = inversions + 1
    return inversions
def countInv_nn_recursive(arr):
    if len(arr)==0 or len(arr)==1:
        return 0
    else:
        return countInv_nn_recursive(arr[:len(arr)//2])+countInv_nn_recursive(arr[len(arr)//2:])+countSplitInv_nn(arr[:len(arr)//2], arr[len(arr)//2:])
print(countInv_nn_recursive(A))
# ==============================================================================
# 0:                                [6, 2, 4, 3, 1, 5]  ,inv = 9 :(6, 2) (6, 4) (6, 3) (6, 1) (6, 5) (2, 1) (4, 3) (4, 1) (3, 1)
# 1:                     [6, 2, 4]                     [3, 1, 5]
# 2:                 [6]          [2, 4]            [3]         [1, 5]
# 3:                             [2]   [4]                     [1]   [5]
def merge_countSplitInv_n(l, r):
    splitInv_count = 0
    i = j = k = 0
    out = [0] * ( len(l) + len(r) )
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out[k] = l[i]
            i += 1
        else:
            out[k] = r[j]
            j += 1
            splitInv_count += len(l) - i
        k += 1
    if i < len(l):
        out[k:] = l[i:]
    if j < len(r):
        out[k:] = r[j:]
    return out, splitInv_count


def sort_countInv_nlogn(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr, 0
    else:
        l, l_count        = sort_countInv_nlogn(arr[:len(arr)//2])
        r, r_count        = sort_countInv_nlogn(arr[len(arr)//2:])
        a, splitInv_count = merge_countSplitInv_n(l, r)
        return a, l_count + r_count + splitInv_count

sortedA, inversions = sort_countInv_nlogn(A)
print(inversions)
# ==
