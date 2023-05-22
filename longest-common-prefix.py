def longestCommonPrefix(strs):
    if not strs:
        return ""

    res = 0
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                return strs[0][:res]

        res += 1

    return strs[0][:res]


print(longestCommonPrefix(["flower", "flow", "flight"]))
