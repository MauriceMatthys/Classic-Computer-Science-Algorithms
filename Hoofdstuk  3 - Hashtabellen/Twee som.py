def twoSum(a, t):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] + a[j] == t:
                return [i, j]
    return None


def twoSumHash(a, t):
    h = {}
    for i, getal in enumerate(a):
        aj = t - getal
        if aj in h:
            j = h[aj]
            return [j, i]
        else:   
            h[getal] = i
    return None

print(twoSumHash([1, 4, 5, 7, 8, 9],10))