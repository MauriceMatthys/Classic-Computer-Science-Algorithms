def zeef(n):
    cijfers = [i for i in range(2, n + 1)]
    m = 2
    niet_priem = set()
    while pow(m, 2) < n:

        mult_m = m

        while mult_m < n:
            mult_m += m
            niet_priem.add(mult_m)

        m += 1

    return sorted(list(set(cijfers).difference(niet_priem)))
