from math import pi
def basel(i):
    som = 0
    for i in range(i):
        som += 1 / pow(i + 1,    2)
    return som


print(f"{basel(100):.11f}")

j = 1
waarde = abs(basel(j) - pow(pi, 2) / 6)
while waarde > 1 / 100:
    j += 1
    waarde = abs(basel(j) - pow(pi, 2) / 6)

print(j)

