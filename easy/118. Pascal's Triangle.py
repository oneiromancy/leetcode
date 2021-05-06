def generate(numRows):
        pascal = [[1], [1,1]]

        for row in range(2, numRows):
            newRow = [1] * (row + 1)
            prevRow = pascal[len(pascal) - 1]

            for idx in range(0, len(prevRow) - 1):
                newRow[idx + 1] = prevRow[idx] + prevRow[idx + 1]

            pascal.append(newRow)

        return pascal[:numRows]

print(generate(6))