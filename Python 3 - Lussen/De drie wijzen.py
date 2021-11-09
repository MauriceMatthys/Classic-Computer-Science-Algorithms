from decimal import Decimal as d

t = int(d(input()) * 100)
a, b, c = 0, 0, 0

for i in range(3, int(t * 100)):
    c = t - i
    for j in range(t - c - 1, (t - c) // 2, -1):
        b = j
        a = t - b - c
        if a + b + c == (a * b * c) // 10000 == t and a * b * c % 10000 == 0:
            break
    if a + b + c == (a * b * c) // 10000 == t and a * b * c % 10000 == 0:
        break

a, b, c, t = a / 100, b / 100, c / 100, t / 100

print(f"${a:.2f} + ${b:.2f} + ${c:.2f} = ${a:.2f} x ${b:.2f} x ${c:.2f} = ${t:.2f}")
