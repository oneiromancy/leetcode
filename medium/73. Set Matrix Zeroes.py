def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_size = len(matrix)
    target_indices = []
    is_zero_row = False

    for r in range(row_size):
        column_size = len(matrix[r])

        for c in range(column_size):
            if matrix[r][c] == 0:
                is_zero_row = True
                target_indices += [(i, c) for i in range(row_size) if i != r]

        if is_zero_row:
            matrix[r] = [0] * column_size
            is_zero_row = False

    while target_indices:
        r, c = target_indices.pop()
        matrix[r][c] = 0

    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

# [[0],[0]]
        