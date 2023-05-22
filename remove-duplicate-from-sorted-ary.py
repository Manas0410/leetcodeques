# https://leetcode.com/problems/remove-duplicates-from-sorted-array
def removeDuplicates(nums):
    res = 0
    temp = []
    for i in range(0, len(nums) - 1):
        if nums[i + 1] == nums[i]:
            nums.pop(i + 1)
            temp.append(nums[i + 1])
    res = len(nums)
    nums = nums + temp
    print(nums)
    return res


print(removeDuplicates([1, 1, 2]))


# if len(nums) == 0:
#     return 0

# count = 0
# for i in range(1, len(nums)):
#     if nums[i] != nums[count]:
#         count += 1
#         nums[count] = nums[i]

# nums = nums[:count+1]
# print(nums)
# return count + 1


def removeDuplicates(nums):
    res = 0
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            res += 1
    res += 1  # Increment res for the first unique element
    return res


print(removeDuplicates([1, 1, 2]))  # Output: 2
