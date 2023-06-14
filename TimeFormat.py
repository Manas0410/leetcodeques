def timeConversion(s):
    # Write your code here
    tr = s[:-2].split(":")
    flag = s[-2:]
    if flag == "AM":
        if tr[0] == "12":
            tr[0] = "00"
        return tr[0] + ":" + tr[1] + ":" + tr[2]
    if flag == "PM":
        if tr[0] == "12":
            return tr[0] + ":" + tr[1] + ":" + tr[2]

        return str(int(tr[0]) + 12) + ":" + tr[1] + ":" + tr[2]


print(timeConversion("12:40:22AM"))
print(timeConversion("12:40:22PM"))
