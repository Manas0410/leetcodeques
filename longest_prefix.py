def pref(ar):
    ar.sort(key=len)
    temp = False
    count = 0
    for i in range(1, len(ar)):
        for j in range(len(ar[0])):
            if ar[0][j] != ar[i][j]:
                temp = False
        else:
            temp = True
        if temp:
            count += 1
    return ar[0][0:count]


strs = ["flower", "flow", "flight"]
print(pref(strs))
