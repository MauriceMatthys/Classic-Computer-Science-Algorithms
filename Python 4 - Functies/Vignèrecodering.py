def codeer(orig, key):
    code = ""
    for i, char in enumerate(orig):
        keylet = (key[i % len(key)])

        if char.isalpha():
            code += chr((((ord(char) - 65) + (ord(keylet) - 65)) % 26) + 65)
        else:
            code += char

    return code


def decodeer(orig, key):
    code = ""
    for i, char in enumerate(orig):
        keylet = (key[i % len(key)])

        if char.isalpha():
            code += chr((((ord(char) - 65) - (ord(keylet) - 65)) % 26) + 65)
        else:
            code += char

    return code
