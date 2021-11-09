def bepaling(v):
    waarde = {
                -25: "strongly underrated",
                -5: "underrated",
                5: "about equal",
                25: "overrated",
                26: "strongly overrated"
            }
    for key, value in waarde.items():
        if v <= key:
            return value
    return value


def appreciation(bmlok, wisselk):
    bm_vs = 4.07
    bm_wisselk = bmlok / bm_vs
    v = ((bm_wisselk - wisselk) / wisselk) * 100
    return bepaling(v)


def exchange_rate_analysis(bmlok, wisselk):
    formattedbmlok = bmlok.split()
    return f"The {' '.join(formattedbmlok[1:])} is {appreciation(float(formattedbmlok[0]), wisselk)} with regard to the dollar."
