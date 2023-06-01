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


# /**
#  * @param {number[]} nums
#  * @param {number} k
#  * @return {number[]}
#  */
# var topKFrequent = function(nums, k) {
#        res={}
#         for (let i=0;i<nums.length;i++){
#             if(res.hasOwnProperty(nums[i])){res[nums[i]]+=1}
#             else{res[nums[i]] = 1}
#         }console.log(res)
#         valar = Object.values(res)
#         keyar = Object.keys(res)
#         for(let i=0; i<valar.length; i++){
#             let temp =0
#             temp1 = 0
#             for(let j=i+1; j<valar.length; j++){
#                 if(valar[i]<valar[j]){
#                     temp = valar[i]
#                     valar[i]=valar[j]
#                     valar[j]=temp
#                     temp1 = keyar[i]
#                     keyar[i]=keyar[j]
#                     keyar[j]=temp1
#                 }
#             }
#         }console.log({ valar },{ keyar })

#         return keyar.slice(0,k)
#     }
