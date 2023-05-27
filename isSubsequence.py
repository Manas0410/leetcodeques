# https://leetcode.com/problems/is-subsequence/description/
class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) < 1:
            return True
        if len(s) > len(t):
            return False
        res = 0
        for i in t:
            if s[res] == i:
                res += 1
                if res == len(s):
                    return True
        return False
