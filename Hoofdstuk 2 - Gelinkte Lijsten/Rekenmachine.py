def evalueer_postfix(expressie):
    stapel = []
    for symbool in expressie:
        if symbool.isnumeric():
            stapel.append(symbool)
        else:
            op1 = stapel.pop()
            op2 = stapel.pop()
            uitkomst = voerBewerkingUit(op1, op2, symbool)
            stapel.append(float(uitkomst))
    return stapel.pop()


def voerBewerkingUit(op1, op2, operator):
    op1 = float(op1)
    op2 = float(op2)

    if operator == "+":
        uitkomst = op1 + op2
    if operator == "-":
        uitkomst = op2 - op1
    if operator == "*":
        uitkomst = op1 * op2
    if operator == "/":
        uitkomst = op2 / op1
    return uitkomst


def infix_naar_postfix(expressie):
    uitvoer = []
    stapel = []
    for symbool in expressie:
        if symbool.isnumeric():
            uitvoer.append(symbool)
        elif symbool == ")":
            while stapel[-1] != "(":
                uitvoer.append(stapel.pop())
            stapel.pop()  # openend haakje van de stapel halen
        elif len(stapel) == 0 or prioriteit(symbool) > prioriteit(stapel[-1]) or symbool == "(":
            stapel.append(symbool)
        else:
            while len(stapel) > 0 and prioriteit(stapel[-1]) >= prioriteit(symbool):
                uitvoer.append(stapel.pop())
            stapel.append(symbool)
    while len(stapel) > 0:
        uitvoer.append(stapel.pop())
    return uitvoer


def prioriteit(operator):
    if operator in "*/":
        return 2
    elif operator in "+-":
        return 1
    return 0


def rekenmachine(infix_string):
    infix_tokens = infix_string.split()
    postfix = infix_naar_postfix(infix_tokens)
    uitkomst = evalueer_postfix(postfix)
    return uitkomst

