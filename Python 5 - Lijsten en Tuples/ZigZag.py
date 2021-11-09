def iszigzag(reeks):

    for i in range(0, len(reeks)-1):
        if i % 2 == 0 and reeks[i+1] > reeks[i]:
            return False

        elif i % 2 != 0 and reeks[i+1] < reeks[i]:
            return False

    return True


def zigzag_traag(reeks):
    reeks.sort()

    for i in range(1, len(reeks), 2):
        reeks[i], reeks[i-1] = reeks[i-1], reeks[i]


def zigzag_snel(reeks):
    for i in range(0, len(reeks), 2):
        if reeks[i] < reeks[max(i-1, 0)]:
            reeks[i], reeks[i-1] = reeks[i-1], reeks[i]

        if reeks[i] < reeks[min(i+1, len(reeks)-1)]:
            reeks[i], reeks[i+1] = reeks[i+1], reeks[i]
