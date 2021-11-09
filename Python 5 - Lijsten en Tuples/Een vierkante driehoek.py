# import math
#
#
# def combination(n, r):
#     return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))
#
#
# def driehoek(rows):
#     if not isinstance(rows, int) or rows < 0:
#         raise AssertionError("ongeldig aantal rijen")
#     result = []
#     for count in range(rows):
#         row = []
#         for element in range(count + 1):
#             row.append(combination(count, element))
#         result.append(row)
#     return result
#
#
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
# def kwadraat(row, col):
#     numbers = zeshoek(row, col)
#
#     product = math.prod(numbers)
#     squarert = int(math.sqrt(product))
#
#     stringnumbers = [str(i) for i in numbers]
#
#     return f'{" x ".join(stringnumbers)} = {math.prod(numbers)} = {squarert} x {squarert}'

import math


def driehoek(height):
    if is_natural_number(height) == False:
        raise AssertionError("ongeldig aantal rijen")
    else:
        triangle = []
        row = []
        prev_row = []
        for i in range(0, height + 1):
            row = [j > 0 and j < i - 1 and i > 2 and prev_row[j - 1] + prev_row[j] or 1 for j in range(0, i)]
            prev_row = row
            triangle += [row]
        return triangle[1:]


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


def kwadraat(rij, kolom):
    getallen = zeshoek(rij, kolom)
    getal1 = getallen[0]
    getal2 = getallen[1]
    getal3 = getallen[2]
    getal4 = getallen[3]
    getal5 = getallen[4]
    getal6 = getallen[5]

    product = getal1 * getal2 * getal3 * getal4 * getal5 * getal6
    wortel = math.sqrt(product)

    uitkomst = "%d x %d x %d x %d x %d x %d = %d = %d x %d" % (
    getal1, getal2, getal3, getal4, getal5, getal6, product, wortel, wortel)

    return uitkomst