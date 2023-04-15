https: // leetcode.com/problems/string-compression/description/


class Solution:
    def compress(self, chars: List[str]) -> int:
        res = ''
        dictval = {}

        for i in chars:
            if i in dictval:
                dictval[i] += 1
            else:
                dictval[i] = 1
        for i, j in dictval.items():
            if j == 1:
                res += i
            else:
                res += i + str(j)
        chars = list(res)
        return len(chars)
