# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order
def generateMatrix(n):
    res = []
    for i in range(n):
        res.append([0] * n)
    start_row = 0
    start_col = 0
    end_row = n - 1
    end_col = n - 1
    pointer = 1
    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            res[start_row][i] = pointer
            pointer += 1
        start_row += 1
        for j in range(start_row, end_row + 1):
            res[j][end_col] = pointer
            pointer += 1
        end_col -= 1
        if end_col >= start_col:
            for k in range(end_col, start_col - 1, -1):
                res[end_row][k] = pointer
                pointer += 1
        end_row -= 1
        if end_row >= start_row:
            for l in range(end_row, start_row - 1, -1):
                res[l][start_col] = pointer
                pointer += 1
        start_col += 1

    return res


print(generateMatrix(5))
# # for i in range(5, -1, -1):
# #     print(i)
