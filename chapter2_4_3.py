
def sumRegion(matrix, row1, col1, row2, col2):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i >= row1 and i <= row2 and j >= col1 and j <= col2:
                sum += matrix[i][j]

    return sum


if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5],
              ]
    print(sumRegion(matrix, 2, 1, 4, 3))
