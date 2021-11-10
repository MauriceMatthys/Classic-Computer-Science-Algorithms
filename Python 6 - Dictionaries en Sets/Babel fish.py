def vertalingToevoegen(woord, vertaling, woordenboek: set):
    woordenboek[woord] = vertaling


def vertaling(woord, woordenboek):
    return "???" if woord not in woordenboek else woordenboek[woord]
