def weeg(coins, evenwicht):
    return coins[:len(coins)//3] if evenwicht == "rechts" else coins[len(coins)//3:len(coins)//3*2] if evenwicht == "links" else coins[len(coins)//3*2:]

coins = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in range(2):

    coins = weeg(coins, input())

print(f"muntstuk #{coins[0]} is vervalst")
