# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) < 1:
            return []
        values = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        if len(digits) == 1:
            print(1)
            return list(values[int(digits[0])])

        def comb(str1, str2):
            cres = []
            for i in str1:
                for j in str2:
                    cres.append(i + j)
            return cres

        res = comb(values[int(digits[0])], values[int(digits[1])])
        k = len(digits)
        j = 2
        while j < k:
            res = comb(res, values[int(digits[j])])
            j += 1
        return res
