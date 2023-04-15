# for unsorted
def remove(string):
    string1 = ''
    for i in string:
        if i not in string1:
            string1 = string1 + i
    return string1


def duplval(string):
    rd = remove(string)
    count = 0
    result = []
    for i in rd:
        for j in range(len(string)):
            if i == string[j]:
                count += 1
        result.append([i, count])
        count = 0
    res = ''
    for i, j in result:
        res += str(j)+i
    return res


string = "AAAABBBCCDAAB"
res = duplval(string)
print(res)

# for sorted
# def compress(string):
#     res = ''
#     for i in range(1,len(string)):
#         if string[i]=
