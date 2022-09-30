def summ(nmbrs):
    s = 0
    for i in range(len(nmbrs)):
        if (i % 2 == 1):
            s += nmbrs[i]
        else:
            continue
    print(s)

numbrs = [4, 6, 8, 15, 11, 2]
summ(numbrs)
