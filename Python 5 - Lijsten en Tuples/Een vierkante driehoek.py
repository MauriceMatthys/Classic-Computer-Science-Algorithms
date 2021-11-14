# import math

# def zeshoek(row, col):
#     row -= 1
#     col -= 1
#
#     if col < 1 or col > row - 1:
#         raise AssertionError("Ongeldige interne positie")
#
#     drieh = driehoek(row + 2)
#     numbers = [drieh[row-1][col-1],
#                drieh[row-1][col],
#                drieh[row][col+1],
#                drieh[row+1][col+1],
#                drieh[row+1][col],
#                drieh[row][col-1]
#                ]
#
#     return numbers
#
#

import math


def driehoek(rows):
    if not is_natural_number(rows):
        raise AssertionError("ongeldig aantal rijen")
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result


def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def is_natural_number(n):
    return isinstance(n, int) and n >= 0


def zeshoek(rij, kolom):
    nieuw = []
    if (rij == 2 and kolom == 1):
        raise AssertionError('ongeldige interne positie')
    try:
        hoek = driehoek(rij + 5)
        nieuw = [hoek[rij - 2][kolom - 2], hoek[rij - 2][kolom - 1], hoek[rij - 1][kolom], hoek[rij][kolom],
                 hoek[rij][kolom - 1], hoek[rij - 1][kolom - 2]]
    except IndexError:
        raise AssertionError("ongeldige interne positie")
    return nieuw


def kwadraat(row, col):
    numbers = zeshoek(row, col)

    product = math.prod(numbers)
    squarert = int(math.sqrt(product))

    stringnumbers = [str(i) for i in numbers]

    return f'{" x ".join(stringnumbers)} = {math.prod(numbers)} = {squarert} x {squarert}'