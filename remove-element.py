# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums)
        i = j - 1
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
                j -= 1
            i -= 1
        return j
