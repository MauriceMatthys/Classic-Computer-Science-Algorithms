max_y = int(input())
max_x = int(input())

pos = [0, 0]
step_y = 1
step_x = 1
start = True

pockets = {
    "[0, 0]": "linkeronderpocket",
    f"[{max_x}, 0]": "rechteronderpocket",
    f"[0, {max_y}]": "linkerbovenpocket",
    f"[{max_x}, {max_y}]": "rechterbovenpocket"
}

while str(pos) not in pockets or start:
    if not start:
        if pos[0] == max_x:
            step_x = -1
            print(f"rechterband ({pos[0]}, {pos[1]})")

        if pos[0] == 0:
            step_x = 1
            print(f"linkerband ({pos[0]}, {pos[1]})")

        if pos[1] == max_y:
            step_y = -1
            print(f"bovenband ({pos[0]}, {pos[1]})")

        if pos[1] == 0:
            step_y = 1
            print(f"onderband ({pos[0]}, {pos[1]})")

    start = False
    pos[0] += step_x
    pos[1] += step_y

print(f"{pockets[str(pos)]} ({pos[0]}, {pos[1]})")
