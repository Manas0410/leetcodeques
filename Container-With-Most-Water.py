# https://leetcode.com/problems/container-with-most-water/submissions/945631384/
def maxheightea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 2:
        return 0
    i, j = 0, len(height)-1
    maxar = 0
    while i < j:
        if height[i] > height[j]:
            ar = height[j]*(j-i)
            j -= 1
        elif height[i] <= height[j]:
            ar = (height[i])*(j-i)
            i += 1
        if ar > maxar:
            maxar = ar
    return maxar


print(maxheightea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxheightea([1, 1]))
