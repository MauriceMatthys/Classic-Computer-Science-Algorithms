appels = int(input())

kisten = appels // 20
appels %= 20

pallets = kisten // 35
kisten %= 35

print(pallets)
print(kisten)
print(appels)