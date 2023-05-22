class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0 or len(s) < 2:
            return False
        main = {"(": ")", "[": "]", "{": "}"}
        if s[0] not in main:
            return False
        stack = []

        for i in s:
            if i in main:
                stack.append(i)
            elif len(stack) == 0 and i not in main:
                return False
            elif i != main[stack[-1]]:
                return False
            else:
                stack.pop()
        if len(stack) == 0:
            return True
        return False


# for i,j in main.items():
#     print (list(i))
