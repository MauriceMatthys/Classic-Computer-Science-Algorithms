zijde = input()

if zijde == "waarde":
    getal = int(input())
    ans = input()

    is_correct = True if (getal % 2 == 0 and ans == "ja") or (getal % 2 != 0 and ans == "nee") else False

    if is_correct:
        print(f"Juist: kaarten met waarde {getal} moeten {'niet ' if ans == 'nee' else ''}gedraaid worden.")

    else:
        print(f"Fout: kaarten met waarde {getal} moeten {'niet ' if ans == 'ja' else ''}gedraaid worden.")

elif zijde == "kleur":
    kleur = input()
    ans = input()
    is_correct = True if (kleur != "rood" and ans == "ja") or (kleur == "rood" and ans == "nee") else False

    if is_correct:
        print(f"Juist: kaarten met kleur {kleur} moeten {'niet ' if ans == 'nee' else ''}gedraaid worden.")

    else:
        print(f"Fout: kaarten met kleur {kleur} moeten {'niet ' if ans == 'ja' else ''}gedraaid worden.")
