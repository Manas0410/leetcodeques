# https://leetcode.com/problems/zigzag-conversion/description/
class Solution(object):
    def convert(self, s, numRows):
        direction = 1
        temp = []
        if numRows == 1:
            return s
        for i in range(numRows):
            temp.append("")  # ["","",""]
        i = -1
        cal = 0
        last = len(s)
        for j in s:
            i = i + direction  # 0
            temp[i] += j

            if i == numRows - 1 or i == 0 and cal != 0:
                direction = -direction
            else:
                cal = 9

        ans = "".join(i for i in temp)
        return ans
