def csom(getal):
    som = sum([int(number) for number in str(getal)])

    if len(str(getal)) != 1:
        som = csom(som)

    return som
