def bovensteboven(getal):
    getal = str(getal)
    if not getal.isnumeric():
        return False
    if any(char in ["2", "3", "4", "5", "7"] for char in getal):
        return False

    return getal[::-1] == getal.replace("6", "$").replace("9", "6").replace("$", "9")


def volgende(getal):
    getal = int(getal)
    getal += 1
    while not bovensteboven(str(getal)):
        getal += 1
    return getal
