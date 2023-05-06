# def merge(arr1, arr2):
#     for i in arr1:
#         for j in range(len(arr2)):
#             if i < arr2[j]:
#                 arr2.insert(j, i)
#                 break
#         else:
#             arr2.append(i)
#     return arr2


# print(merge([1, 4, 8, 10], [9]))

def merge(arr1, arr2):
    merge = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            j += 1
    merge += arr1[i:]
    merge += arr2[j:]
    return merge


print(merge([1, 4, 8, 10], [9]))
