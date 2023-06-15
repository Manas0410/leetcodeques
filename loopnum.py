def loop(n):
    l = list(range(1, n + 1))
    print(l)
    direction = 1
    strt = 0
    end = -1
    while len(l) > 0:
        print(l[strt::direction])
        l.pop(strt)
        l.pop(end)
        direction = -direction
        strt, end = end, strt


loop(10)
