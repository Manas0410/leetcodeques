def intToRoman(num):
    roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    res = ""
    for value, symbol in roman.items():
        # print(value, symbol)
        while num >= value:
            res += symbol
            num -= value
    return res


print(intToRoman(3994))


# def intToRoman(num):
#     symbols = [
#         "M",
#         "CM",
#         "D",
#         "CD",
#         "C",
#         "XC",
#         "L",
#         "XL",
#         "X",
#         "IX",
#         "V",
#         "IV",
#         "I",
#     ]
#     values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     result = ""
#     i = 0
#     while num > 0:
#         if num >= values[i]:
#             result += symbols[i]
#             num -= values[i]
#         else:
#             i += 1
#     return result
