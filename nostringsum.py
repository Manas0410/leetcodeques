def stringSum(num1, num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    sum = 0
    res = ''
    while i >= 0 or j >= 0 or carry > 0:
        if i > 0:
            sum += int(num1[i])
        else:
            sum += 0
        if j > 0:
            sum += int(num2[j])
        else:
            sum += 0
        sum += carry
        res += str(sum % 10)
        carry = sum//10
        i -= 1
        j -= 1
        sum = 0
    return res[::-1]


print(stringSum('11', '123'))
