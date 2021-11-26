def precies_een_verschillend(woord1, woord2):
    if len(woord1) != len(woord2):
        return False
    aantalVerschil = 0
    for i in range(len(woord1)):
        if woord1[i] != woord2[i]:
            aantalVerschil += 1
    return aantalVerschil == 1

def maak_graaf(woorden):
    dict = {w1:set() for w1 in woorden}
    for i, w1 in enumerate(woorden):
        for j in range(i + 1, len(woorden)):
            w2 = woorden[j]
            if precies_een_verschillend(w1, w2):
                dict[w1].add(w2)
                dict[w2].add(w1)
    return dict

def kortste_pad(graaf, startWoord):
    D = {w : -1 for w in graaf}
    P = {w : None for w in graaf}
    D[startWoord] = 0
    P[startWoord] = startWoord
    Q = []
    Q.append(startWoord)
    while len(Q) > 0:
        v = Q.pop(0)
        for w in sorted(graaf[v]):
            if D[w] == -1:
            #if P[w] == None:
                D[w] = D[v]+1
                P[w] = v
                Q.append(w)
    return P

def geef_pad(voorgangers, doelWoord):
    pad = [doelWoord]
    huidigwoord = doelWoord
    voorganger = voorgangers[huidigwoord]
    while huidigwoord != voorganger:
        pad.insert(0, voorganger)
        huidigwoord = voorganger
        voorganger = voorgangers[huidigwoord]
    return pad
