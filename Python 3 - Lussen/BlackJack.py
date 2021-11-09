card = int(input())
cardsum = card

while cardsum < 21 and card != 0:
    card = int(input())
    cardsum += card

if cardsum == 21:
    print("Gewonnen!")

elif cardsum > 21:
    print(f"Verbrand ({cardsum})")

else:
    print(f"Voorzichtig gespeeld ({cardsum})")