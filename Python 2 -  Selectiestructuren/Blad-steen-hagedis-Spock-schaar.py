win = {
    "blad": ("steen", "Spock"),
    "steen": ("schaar", "hagedis"),
    "hagedis": ("Spock", "blad"),
    "Spock": ("schaar", "steen"),
    "schaar": ("blad", "hagedis"),
}

s1 = input()
s2 = input()

print("gelijkspel" if s1 == s2 else "speler1 wint" if s2 in win[s1] else "speler2 wint")
