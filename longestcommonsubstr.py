# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# class Solution(object):
def lengthOfLongestSubstring(self, s):
    if len(s) < 2:
        return len(s)
    pointer = s[0]
    ar = []
    for i in range(1, len(s)):
        if s[i] not in pointer:
            pointer += s[i]
        else:
            ar.append(pointer)
            index = pointer.index(s[i])
            pointer = pointer[index+1:]+s[i]
        ar.append(pointer)
    big = 0
    for i in ar:
        if len(i) > big:
            big = len(i)
    return big

# without index


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)
        k = 0
        pointer = s[k]
        ar = []
        for i in range(1, len(s)):
            if s[i] not in pointer:
                pointer += s[i]
            else:
                ar.append(pointer)
                while s[k] != s[i]:
                    k += 1
                k += 1
                pointer = s[k:i+1]
            ar.append(pointer)
        big = 0
        for i in ar:
            if len(i) > big:
                big = len(i)
        return big
