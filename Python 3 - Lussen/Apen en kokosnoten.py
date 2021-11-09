p = int(input())
k = int(input())
a = k
for i in range(p):
    b = a // p
    c = a % p
    print(f"{a if a > 0 else 'geen'} {'noten' if a != 1 else 'noot'} = {b if b > 0 else 'geen'} {'noten' if b != 1 else 'noot'} voor piraat#{i+1} en {c if c > 0 else 'geen'} {'noten' if c != 1 else 'noot'} voor de aap")
    a -= b + c

d = a // p
e = a % p
print(f"elke piraat krijgt {d if d > 0 else 'geen'} {'noten' if d != 1 else 'noot'} en {e if e > 0 else 'geen'} {'noten' if e != 1 else 'noot'} voor de aap")
