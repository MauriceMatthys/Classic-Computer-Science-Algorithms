getal = int(input())
# ans = ""
ans = 0

for i in range(getal // 2 + 1):
    som = 0
    reeks = ""
    j = i + 1
    while som < getal and (j <= getal // 2 + 1):
        som += j
        # reeks += f"{j} + "
        j += 1
    if som == getal and getal > 2:
        # ans += reeks[:-2] + "\n"
        ans += 1

# print(ans[:-1])
print(ans)