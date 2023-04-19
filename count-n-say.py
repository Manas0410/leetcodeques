def fragment(n):  # to get the fragments
    sum, i = 0, 1
    frag = ''
    while sum <= n:
        counter = sum
        sum += i
        if sum < n:
            frag += str(i)
            i += 1
        elif sum > n:
            sum = counter
            i = 1
        else:
            frag += str(i)
            break
    return frag


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


str = fragment(3)
print(compress(str))
