from math import floor


def maximale_blootstelling(db):
    max_tijd = 28800.0
    if db < 80:
        return -1.0
    if db == 80:
        return max_tijd
    return max_tijd / pow(2, floor((db - 80) / 3))
