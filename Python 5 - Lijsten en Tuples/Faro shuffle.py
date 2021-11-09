def nieuw_kaartspel(kleuren, waarden):
    kaartspel = []
    kaart = ''

    for i in range(len(kleuren)):
        for j in range(len(waarden)):
            kaart = "{}{}".format(kleuren[i], waarden[j])
            kaartspel.append(kaart)

    return kaartspel


def splits_kaartspel(kaartspel):
    deel1 = []
    deel2 = []

    lengte_deel1 = len(kaartspel) // 2
    lengte_deel2 = len(kaartspel) - len(kaartspel) // 2

    for i in range(lengte_deel1):
        deel1.append(kaartspel[0])
        kaartspel.remove(kaartspel[0])

    for i in range(lengte_deel2):
        deel2.append(kaartspel[0])
        kaartspel.remove(kaartspel[0])

    return deel1, deel2


def faro_shuffle(deel1, deel2):
    faro_kaartspel = []

    for i in range(len(deel1)):
        faro_kaartspel.append(deel1[i])
        faro_kaartspel.append(deel2[i])

    if len(deel2) > len(deel1):
        faro_kaartspel.append(deel2[-1])

    return faro_kaartspel
