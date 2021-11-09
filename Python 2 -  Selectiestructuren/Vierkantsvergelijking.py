from math import sqrt

a = float(input())
b = float(input())
c = float(input())

d = pow(b, 2) - 4 * a * c

if d > 0:
    x = (-b - sqrt(d)) / (2 * a)
    y = (-b + sqrt(d)) / (2 * a)

    print(f"twee wortels\n{min(x,y)}\n{max(y,x)}")

elif d == 0:
    x = (-b) / (2 * a)

    print(f'een wortel\n{x}')

else:
    print("geen wortels")