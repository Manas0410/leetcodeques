# for i in range(1, 1):
#     print(i)
# for i in range(1, 0):
#     print(i)
# print([1]*5)
def pascalCreate(row):
    pascal = [[1]*(i+1) for i in range(row)]
    for i in range(row):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
    return pascal


print(pascalCreate(10))
[[1], 
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1],
 [1, 5, 10, 10, 5, 1],
 [1, 6, 15, 20, 15, 6, 1],
 [1, 7, 21, 35, 35, 21, 7, 1],
 [1, 8, 28, 56, 70, 56, 28, 8, 1],
 [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
