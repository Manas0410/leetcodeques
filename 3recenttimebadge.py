def recent(bgt):
    b = {}
    for i, j in bgt:
        if i not in b:
            b[i] = int(j)
        else:
            if int(j) > b[i]:
                b[i] = int(j)
            # b[i].sort(reverse=True)
            # if len(b[i]) > 3:
            #     b[i].pop()
    return b


badgeTimes = [
    ["Paul", "1355"],
    ["Jennifer", "1930"],
    ["Jose", "835"],
    ["Jose", "830"],
    ["Paul", "1315"],
    ["Chloe", "0"],
    ["Chloe", "1910"],
    ["Jose", "1615"],
    ["Jose", "1640"],
    ["Paul", "1405"],
    ["Jose", "855"],
    ["Jose", "930"],
    ["Jose", "915"],
    ["Jose", "730"],
    ["Jose", "940"],
    ["Jennifer", "1335"],

    ["Jose", "1630"],
    ["Jennifer", "5"],
    ["Chloe", "1909"],
    ["Zhang", "1"],
    ["Zhang", "10"],
    ["Zhang", "109"],
    ["Zhang", "110"],
    ["Amos", "1"],
    ["Amos", "2"],
    ["Amos", "400"],
    ["Amos", "500"],
    ["Amos", "503"],
    ["Amos", "504"],
    ["Amos", "601"],
    ["Amos", "602"],
    ["Paul", "1416"]
]
print(recent(badgeTimes))
