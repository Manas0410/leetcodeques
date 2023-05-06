#https://leetcode.com/problems/string-to-integer-atoi/submissions/943856552/
class Solution(object):
    def myAtoi(self, s):
        # removing space
        i = 0
        if len(s)==0 or s==" ":
            return 0
        while i< len(s) and s[i].isspace():
            i += 1
        # getting sign
        sign = 1  
        if i< len(s) and s[i] == "+":
            sign = +1
            i += 1
        elif i< len(s) and s[i] == "-":
            sign = -1
            i += 1
        if i< len(s):
            if s[i] == "-" or s[i] == "+":
                return 0
        # changing to integer
        n = 0
        for j in range(i, len(s)):
            if s[j].isdigit():
                n = (n*10) + int(s[j])
            
            else:
                break
        n = n*sign
        if n < -2**31:
            return -2**31
        if n > 2**31 - 1:
            return 2**31 - 1
        return n