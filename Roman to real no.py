def romantointeger(s):
    roman = [['I', 1], ['V', 5], ['X', 10], [
        'L', 50], ['C', 100], ['D', 500], ['M', 1000]]
    # change the string into corresponding no array
    noary = []
    for i in s:
        for j in roman:
            if i == j[0]:
                noary.append(j[1])
    # channge the no ary into integer
    k = len(noary)-1
    res = 0
    while k >= 0:
        if k > 0 and noary[k] > noary[k-1]:
            res += (noary[k]-noary[k-1])
            k -= 1
        else:
            res += noary[k]
        k -= 1
    return res


print(romantointeger('MCMXCIV'))
