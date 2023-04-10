# https://leetcode.com/problems/binary-prefix-divisible-by-5/
def prefixesDivBy5(nums):
    n = 0
    res = []

    for i in range(1, len(nums)+1):
        temp = i-1
        for j in range(0, i):
            n = n + ((nums[j])*(2**temp))
            temp -= 1
        # print(n)
        if n % 5 == 0:
            # print(n,end ='if n')
            res.append('True')
        else:
            # print(n,end ='else n')
            res.append('False')
        n = 0
    return res


print(prefixesDivBy5([0, 1, 1]))
