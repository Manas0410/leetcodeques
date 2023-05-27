# https://leetcode.com/problems/zigzag-conversion/
def convert(s, numRows):
    t = []
    for i in range(numRows):
        t.append([])
    print(t)
    k = 0
    z = len(s)
    i = 0
    while i < numRows:
        if k >= z:
            break
        t[i].append(s[k])
        k += 1
        i += 1
        if i >= numRows:
            i = 0

    return t


print(convert("PAYPALISHIRING", 3))
# PAHNAPLSIIGYIR
