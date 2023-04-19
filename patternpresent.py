# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/935283073/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)
        for i in range(0, (a-b+1)):
            if haystack[i:(i+b)] == needle:
                return i
        else:
            return -1
