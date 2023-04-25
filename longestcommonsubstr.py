# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)
        pointer = s[0]
        ar = []
        for i in range(1, len(s)-1):
            if s[i] not in pointer:
                pointer += s[i]
            else:
                ar.append(pointer)
                pointer = s[i]
            ar.append(pointer)
        big = 0
        for i in ar:
            if len(i) > big:
                big = len(i)
        return big
