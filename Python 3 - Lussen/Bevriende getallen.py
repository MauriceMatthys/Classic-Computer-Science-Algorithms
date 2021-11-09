import math


def berekendelers(n):
    delers = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            delers.extend([i, n // i])
    delers.extend([n])
    return list(set(delers))


getal1 = int(input())
getal2 = int(input())
print(f"{getal1} en {getal2} zijn {'' if sum(berekendelers(getal1)) - getal1 == getal2 and sum(berekendelers(getal2)) - getal2 == getal1 else 'geen '}bevriende getallen")