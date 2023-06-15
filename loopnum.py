def loop(n):
    l = list(range(1, n + 1))
    direction = 1
    strt = 0
    end = -1
    while len(l) > 0:
        nums = l[strt::direction]
        print("".join(str(x) for x in nums))
        l.pop(strt)
        l.pop(end)
        direction = -direction
        strt, end = end, strt


loop(11)
