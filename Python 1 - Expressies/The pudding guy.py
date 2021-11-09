aantal = int(input())
prijs = float(input())
kans = int(input())
mijlen_barcode = int(input())

kost = aantal * prijs
mijlen = (aantal // kans) * mijlen_barcode

print(f'Phillips spendeerde ${round(kost, 2)} voor {mijlen:d} frequent flyer mijlen.')
