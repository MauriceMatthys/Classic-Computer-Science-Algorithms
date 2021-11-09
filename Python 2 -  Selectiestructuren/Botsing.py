x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

if x1 < x2:
    l1x = x1
    l1y = y2
    r1x = x2
    r1y = y1
    l2x = x3
    l2y = y4
    r2x = x4
    r2y = y3

else:
    l1x = x2
    l1y = y2
    r1x = x1
    r1y = y1
    l2x = x3
    l2y = y4
    r2x = x4
    r2y = y3

intersection = not ((l1x >= r2x or l2x >= r1x) or (r1y >= l2y or r2y >= l1y))

print(f"{'geen ' if not intersection else ''}botsing")



