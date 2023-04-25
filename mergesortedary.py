def merge(arr1, arr2):
    for i in arr1:
        for j in range(len(arr2)):
            if i < arr2[j]:
                arr2.insert(j, i)
                break
        else:
            arr2.append(i)
    return arr2


print(merge([1, 4, 8, 10], [9]))
