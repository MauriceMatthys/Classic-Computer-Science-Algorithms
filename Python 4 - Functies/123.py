def evenOneven(n):
    even = 0
    oneven = 0
    for char in str(n):
        if int(char) % 2 == 0:
            even += 1
        else:
            oneven += 1
    return even, oneven


def volgende(n):
    even, oneven = evenOneven(n)

    return int(str(even) + str(oneven) + str(len(str(n))))


def stappen(n):
    if n == 123:
        return 0

    return stappen(volgende(n)) + 1
