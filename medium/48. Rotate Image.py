def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_size = len(matrix)

    for r in range(row_size):
        column_size = len(matrix[r])

        for c in range(r, column_size):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        matrix[r] = matrix[r][::-1]

    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    