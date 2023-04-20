# AAAABBBCCDAA  -- 6A3B2C1D

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

# AAAABBBCCDAA  -- 4A3B2C1D2A


def compress(s):

    count = 1
    cmprs = ''
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            cmprs += str(count)+s[i-1]
            count = 1
    cmprs += str(count)+s[-1]
    return cmprs
