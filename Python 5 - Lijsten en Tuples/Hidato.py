def eerste(veld):
    for index, reeks in enumerate(veld):
        if 1 in reeks:
            return index, reeks.index(1)


def opvolger(veld, r, k):
    waarde = veld[r][k]
    volgr, volgk = None, None

    for i, reeks in enumerate(veld):
        if waarde+1 in reeks:
            volgr, volgk = i, reeks.index(waarde+1)
            if 0 <= abs(volgr - r) <= 1 and 0 <= abs(volgk - k) <= 1:
                return volgr, volgk
            else:
                break

    return None, None


def laatste(veld):
    begin = eerste(veld)
    return laatsterecursief(veld, begin[0], begin[1])


def laatsterecursief(veld, r, k, ):
    nextpos = opvolger(veld, r, k)
    if nextpos[0] is None:
        return r, k

    return laatsterecursief(veld, nextpos[0], nextpos[1])


def hidato(veld):
    eind = laatste(veld)

    return veld[eind[0]][eind[1]] == (len(veld) * len(veld[0]))
