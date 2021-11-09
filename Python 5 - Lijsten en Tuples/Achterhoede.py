def zien(volgorde):
    volgorde = list(volgorde)
    red_count = 0
    for i, hoed in enumerate(volgorde):

        if red_count % 2 == 0:
            if hoed == "R":
                red_count += 1
            volgorde[i] = "B"

        else:
            if hoed == "R":
                red_count += 1
            volgorde[i] = "R"

    return tuple(volgorde)


def zeggen(volgorde):
    volgorde = list(volgorde)
    said_red = 0
    opposite = {"R": "B", "B": "R"}

    volgorde = volgorde[::-1]
    for i, hoed in enumerate(volgorde):
        if said_red % 2 != 0:
            volgorde[i] = opposite[hoed]

        if volgorde[i] == "R":
            said_red += 1

    return tuple(volgorde[::-1])

