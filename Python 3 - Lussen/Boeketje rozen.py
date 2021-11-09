redwhite = int(input())
whiteblue = int(input())
comparator = input()  # red >< white

redcheck, bluecheck, whitecheck = 0, 0, 0

if comparator == "<":
    redcheck, whitecheck = 1, 2

else:
    redcheck, whitecheck = 2, 1

if redwhite < whiteblue:
    if redcheck < whitecheck:
        bluecheck = 3
    else:
        bluecheck = 2
        redcheck += 1

else:
    bluecheck = 1
    whitecheck += 1
    redcheck += 1

# if (bluecheck, whitecheck, redcheck) == (1,2,3):
#     pass
#
# elif (bluecheck, whitecheck, redcheck) == (3,2,1):
#     pass
#
# elif (bluecheck, whitecheck, redcheck) == (2,1,3):
#     pass
#
# elif (bluecheck, whitecheck, redcheck) == (2,1,3)

checks = [bluecheck, whitecheck, redcheck]
kleuren = [0, 0, 0]

# for index, check in enumerate(checks):
#     if check == 1:
#         kleuren[index] = 2
#

if checks[1] == 1:
    kleuren[0], kleuren[1], kleuren[2] = whiteblue - 2, 2, redwhite - 2

if checks[2] == 1:
    kleuren[0], kleuren[1], kleuren[2] = whiteblue - redwhite + 2, redwhite - 2, 2

if checks[0] == 1:
    kleuren[0], kleuren[1], kleuren[2] = 2, whiteblue - 2, redwhite - whiteblue + 2

print(f"{kleuren[0]}\n{kleuren[1]}\n{kleuren[2]}")