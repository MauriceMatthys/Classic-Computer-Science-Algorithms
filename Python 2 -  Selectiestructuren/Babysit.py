u1 = int(input())
m1 = int(input())

u2 = int(input())
m2 = int(input())

ans = "invalid input"

u1 = u1 + m1 / 60
u2 = u2 + m2 / 60

if u1 >= 18 and u2 > u1:
    if u2 < 21.5:
        t1 = u2-u1
        t2 = 0

    elif u1 < 21.5:
        t1 = 21.5 - u1
        t2 = u2 - 21.5

    else:
        t2 = u2 - u1
        t1 = 0

    ans = 2 * t1 + 4 * t2

print(ans)