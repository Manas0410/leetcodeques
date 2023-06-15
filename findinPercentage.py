temp = [52, 56, 60]
x = sum(temp) / len(temp)
t = str(x).split(".")
while len(t[1]) < 2:
    t[1] += "0"
if len(t[1]) > 2:
    t[1] = t[1][:2]
res = ".".join(t)
print(res)
# temp = [52, 56, 60]
# x = sum(temp) / len(temp)
# t = str(x).split(".")
# while len(t[1]) < 2:
#     t[1] += "0"
# res = ".".join(t)
# print(res)
