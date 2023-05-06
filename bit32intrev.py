# https://leetcode.com/problems/reverse-integer/submissions/941622320/
class Solution(object):
    def reverse(self, x):
        def rev(n):
            rev = 0
            while n > 0:
                rev = (rev*10)+(n % 10)
                n = n//10
            return rev
        if x < 0:
            ans = rev(x*(-1))*(-1)
        else:
            ans = rev(x)
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        else:
            return ans
