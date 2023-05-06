# https://leetcode.com/problems/longest-palindromic-substring/submissions/940678426/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def rev(st):
            return st[::-1]

        if s == rev(s):
            return s
        str = ""

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == rev(s[i:j]):
                    if len(s[i:j]) > len(str):
                        str = s[i:j]
        return str
