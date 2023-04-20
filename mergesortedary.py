def merge(arr1, arr2):
    for i in arr1:
        for j in range(0, len(arr2)):
            if i < arr2[j]:
                arr2.insert(j, i)
                continue
            else:
                continue
    return arr2


print(merge([1, 4, 8, 10], [2, 3, 9]))
