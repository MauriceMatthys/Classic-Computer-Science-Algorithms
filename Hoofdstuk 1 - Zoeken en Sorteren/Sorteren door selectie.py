def selection_sort_vooraan(a):
    n = len(a)
    for i in range(n - 1):
        positie = i
        min = a[i]
        for j in range(i + 1, n):
            if a[j] < min:
                positie = j
                min = a[j]
        a[positie] = a[i]
        a[i] = min
        print(a)

a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)
