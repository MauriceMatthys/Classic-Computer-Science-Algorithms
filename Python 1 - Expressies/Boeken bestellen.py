aantal_boeken = 60
kost_boek = 24.95
korting = 0.40

totaal = aantal_boeken * kost_boek - (aantal_boeken * kost_boek) * korting

prijs = totaal + 3 + 0.75 * (aantal_boeken - 1)

print(prijs)