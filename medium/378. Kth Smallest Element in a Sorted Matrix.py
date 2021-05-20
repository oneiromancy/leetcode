def kthSmallest(matrix, k):
    l = []

    for m in matrix:
        l += m

    return sorted(l)[k - 1]
        

print(kthSmallest([[1,2],[1,3]], 2))

# [[1,5,9],[10,11,13],[12,13,15]], k = 8
# [[1,2],[1,3]], k = 2