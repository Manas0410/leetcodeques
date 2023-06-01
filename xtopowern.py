# https://leetcode.com/problems/powx-n/submissions/960721010/
class Solution(object):
    def myPow(self, x, n):
        if x == 0:
            if n == 0:
                return 1
            return 0
        if n < 0:
            return self.myPow(1 / x, -n)
        ans = 1
        while n > 0:
            if n % 2 == 0:
                n = n / 2
                x *= x
            elif n % 2 == 1:
                n = n - 1
                ans *= x
        return ans
