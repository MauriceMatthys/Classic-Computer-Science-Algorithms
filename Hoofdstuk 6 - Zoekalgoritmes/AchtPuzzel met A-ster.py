import heapq


class AchtPuzzel:
    BUREN = {0: {("R", 1), ("O", 3)}, 1: {("L", 0), ("R", 2), ("O", 4)}, 2: {("L", 1), ("O", 5)},
             3: {("B", 0), ("R", 4), ("O", 6)}, 4: {("B", 1), ("L", 3), ("R", 5), ("O", 7)},
             5: {("B", 2), ("L", 4), ("O", 8)},
             6: {("B", 3), ("R", 7)}, 7: {("B", 4), ("L", 6), ("R", 8)}, 8: {("B", 5), ("L", 7)}
             }

    def __init__(self, bord="123456780"):
        assert set(bord) == set("123456780"), "geen correct bord"
        self.bord = bord

    def __str__(self):
        return self.bord[:3] + "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):
        return f"AchtPuzzel(bord='{self.bord}')"

    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False

    def __hash__(self):
        return hash(self.bord)

    def opvolgers(self):
        result = set()
        positieVanHetGat = self.bord.find("0")
        setVanTupelMetActieEnNieuwePositie = AchtPuzzel.BUREN[positieVanHetGat]
        for actieEnPositie in setVanTupelMetActieEnNieuwePositie:
            actie = actieEnPositie[0]
            nieuwePositie = actieEnPositie[1]
            puzzelStukjeMetNr = self.bord[nieuwePositie]
            nieuwBord = self.bord.replace(puzzelStukjeMetNr, "9")
            nieuwBord = nieuwBord.replace("0", puzzelStukjeMetNr)
            nieuwBord = nieuwBord.replace("9", "0")
            result.add((actie, AchtPuzzel(nieuwBord)))
        return result

    def aantal_verkeerd(self, other):
        aantal = 0
        for i, puzzelStukje in enumerate(self.bord):
            if puzzelStukje not in ["0", other.bord[i]]:
                aantal += 1
        return aantal

    def manhattan_heuristiek(self, other):
        aantal = 0
        for i, puzzelStukje in enumerate(self.bord):
            if puzzelStukje not in "0":
                row = i // 3
                col = i % 3
                posInAnderePuzzel = other.bord.find(puzzelStukje)
                r = posInAnderePuzzel // 3
                c = posInAnderePuzzel % 3
                aantal += abs(row - r) + abs(col - c)
        return aantal


class Plan:

    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        self.toestand = toestand
        self.voorganger = voorganger
        self.actie = actie
        self.kost = kost
        self.h_waarde = h_waarde

    ## Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        return self.kost + self.h_waarde < other.kost + other.h_waarde

    def geef_actie_sequentie(self):
        result = []
        huidige = self
        while self.voorganger != None:
            result.append(huidige.actie)
            huidige = huidige.voorganger
        result.reverse()
        return result  # result[::-1]


def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost=lambda s, a: 1):
    wachtRij = []
    closed = set()
    heapq.heappush(wachtRij, Plan(start_toestand))
    while len(wachtRij) > 0:
        plan = heapq.heappop(wachtRij)
        toestand = plan.toestand
        if is_doel(toestand):  # doel bereikt
            return (plan.geef_actie_sequentie(), plan.kost)
        else:  # doel nog niet bereikt
            if toestand not in closed:
                closed.add(toestand)
                for opvolger in sorted(toestand.opvolgers()):
                    actie = opvolger[0]
                    nieuweToestand = opvolger[1]
                    heapq.heappush(wachtRij, Plan(nieuweToestand, plan, actie, plan.kost + kost(toestand, actie),
                                                  heuristiek(nieuweToestand)))
    return None