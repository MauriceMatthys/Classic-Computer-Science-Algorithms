import heapq
class AchtPuzzel:
    BUREN = {
        0: {("R", 1), ("O", 3)}, 1: {("L", 0), ("R", 2), ("O", 4)}, 2: {("L", 1), ("O", 5)},
        3: {("B", 0), ("R", 4), ("O", 6)}, 4: {("B", 1), ("L", 3), ("R", 5), ("O", 7)},
        5: {("B", 2), ("L", 4), ("O", 8)},
        6: {("B", 3), ("R", 7)}, 7: {("B", 4), ("L", 6), ("R", 8)}, 8: {("B", 5), ("L", 7)}
    }

    def __init__(self, bord="123456780"):
        self.bord = bord

    def __str__(self):
        return self.bord[:3] + "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):
        return f"AchtPuzzel(bord='{self.bord}')"  # f = formatted string.

    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False

    def __hash__(self):
        return hash(self.bord)

    def opvolgers(self):
        index_0 = self.bord.find('0')  # Lege vakje opzoeken met ingebouwde methoden.
        opv = set()
        for (actie, index) in AchtPuzzel.BUREN[index_0]:
            i1 = min(index_0, index)
            i2 = max(index_0, index)
            # i1 en i2 wisselen.
            nieuwe_puzzel = self.bord[:i1] + self.bord[i2] + self.bord[i1 + 1:i2] + self.bord[i1] + self.bord[i2 + 1:]
            opv.add((actie, AchtPuzzel(nieuwe_puzzel)))  # tupel toevoegen.
        return opv

    def aantal_verkeerd(self, other):  # h1 vanuit de cursus.
        aantal = 0
        for ind, char in enumerate(self.bord):
            if char != '0' and char != other.bord[ind]:
                aantal += 1
        return aantal

    def manhattan_heuristiek(self, other):
        totale_afstand = 0
        for i1, char in enumerate(self.bord):
            if char != '0':
                i2 = other.bord.find(char)  # correcte index opzoeken.
                totale_afstand += AchtPuzzel.manhattan_distance(i1, i2)
        return totale_afstand

    @staticmethod
    def manhattan_distance(i1, i2):
        x1, y1 = i1 // 3, i1 % 3
        x2, y2 = i2 // 3, i2 % 3
        return abs(x1 - x2) + abs(y1 - y2)


class Plan:
    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        self.toestand = toestand  # AchtPuzzel.
        self.voorganger = voorganger  # AchtPuzzel.
        self.actie = actie  # L | R | O | B
        self.kost = kost  # float
        self.h_waarde = h_waarde

    # Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        return self.kost + self.h_waarde < other.kost + other.h_waarde

    def geef_actie_sequentie(self):
        acties = []
        huidig = self
        while huidig.actie:
            acties.append(huidig.actie)
            huidig = huidig.voorganger
        return acties[::-1]


def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost=lambda s, a: 1):  # lambda functie (s,a) => 1
    open_lijst = []  # Bevat plannen.
    gesloten_lijst = set()  # Bevat toestanden.
    heapq.heappush(open_lijst, Plan(start_toestand))
    while len(open_lijst) > 0:
        huidig_plan = heapq.heappop(open_lijst)
        if is_doel(huidig_plan.toestand):
            return huidig_plan.geef_actie_sequentie(), huidig_plan.kost  # retourneert tupel
        else:
            if huidig_plan.toestand not in gesloten_lijst:
                gesloten_lijst.add(huidig_plan.toestand)
                for actie, opvolger in sorted(huidig_plan.toestand.opvolgers()):
                    nieuw_plan = Plan(toestand=opvolger, voorganger=huidig_plan, actie=actie,
                                      kost=huidig_plan.kost + kost(huidig_plan, actie), h_waarde=heuristiek(opvolger))
                    heapq.heappush(open_lijst, nieuw_plan)
    return None
