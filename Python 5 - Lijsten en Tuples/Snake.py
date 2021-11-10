def beweeg(pos, richting):
    if richting == "<":
        return pos[0]-1, pos[1]

    elif richting == ">":
        return pos[0]+1, pos[1]

    elif richting == "^":
        return pos[0], pos[1]+1

    elif richting == "v":
        return pos[0], pos[1]-1


def teruggekeerd(lijst):
    foute = [{"v", "^"}, {"<", ">"}]

    if set(lijst) in foute:
        return True

    return False


def laatste_levende_positie(bewegingen):
    geldig = 0
    pos = 0, 0
    for i, richting in enumerate(bewegingen):
        if teruggekeerd(bewegingen[max(i-1, 0):i+1]):
            return geldig, pos[0], pos[1]

        pos = beweeg(pos, richting)
        geldig += 1

    return geldig, pos[0], pos[1]
