vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"


def varkenswoord(word: str) -> str:
    latinword = ""
    index = first_vowel(word)

    if index == 0:
        latinword = word + "way"

    else:
        if word[0:2].lower() == "qu":
            index += 1

        if word[0] in consonants.upper() and word[index] not in vowels.upper():
            word = word[0].lower() + word[1:index] + word[index].upper() + word[index+1:]

        if len(word) > 1 and index is not None:
            latinword = word[index:] + word[0:index] + "ay"
        else:
            latinword = word + "ay"

    return latinword


def first_vowel(word: str) -> int:
    for index, char in enumerate(word):
        if char.lower() in vowels:
            return index


def varkenslatijn(sentence: str) -> str:
    latinsentence = ""
    word = ""
    for letter in sentence:
        if letter.isalpha():
            word += letter

        else:
            if word.isalpha():
                latinsentence += varkenswoord(word) + letter
                word = ""

            else:
                latinsentence += letter

    if latinsentence[-1].isspace():
        latinsentence += varkenswoord(word)

    return latinsentence
