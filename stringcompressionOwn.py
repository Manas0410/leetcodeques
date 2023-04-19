# AAAABBBCCD  -- 4A3B2C1D
def compress(s):
    res = ''
    dictval = {}

    for i in s:
        if i in dictval:
            dictval[i] += 1
        else:
            dictval[i] = 1
    for i, j in dictval.items():
        res += str(j) + i
    return res


print(compress('AAAABBBCCDAA'))
