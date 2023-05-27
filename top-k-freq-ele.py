# https://leetcode.com/problems/top-k-frequent-elements/submissions/955298074/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_nums = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)
        return sorted_nums[:k]
