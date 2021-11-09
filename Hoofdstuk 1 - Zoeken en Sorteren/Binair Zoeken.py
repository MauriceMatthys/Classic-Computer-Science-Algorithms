def zoekBinair(a: list, getal: int):
    n = len(a)
    l = 0
    r = n - 1

    while l != r:
        print(f"{l}, {r}")
        m = (l+r) // 2
        if a[m] < getal:
            l = m + 1
        else:
            r = m

    if a[l] == getal:
        return l
    else:
        return -1
