def afstand2(punt1, punt2):
    """ Gekwadrateerde Euclidische afstand tussen de twee tupels punt1 en punt2
    """
    # afstand = 0
    # for i,x1 in enumerate(punt1):
    #   x2 = punt2[i]
    #   afstand += (x1-x2)**2
    # return afstand
    return sum((x1 - x2) ** 2 for (x1, x2) in zip(punt1, punt2))


def index_dichtste(punt, centroids):
    """ Geef de index (vanaf 0) van de centroid die het dichtste bij punt gelegen is.
    """
    # minAfstand = float("inf")
    # minIndex = -1
    # for index,centroid in enumerate(centroids):
    #   afstand = afstand2(punt,centroid)
    #   if(afstand<minAfstand):
    #     minAfstand : afstand
    #     minIndex = index
    # return minIndex
    afstanden = [afstand2(punt, c) for c in centroids]
    return afstanden.index(min(afstanden))


def cluster_assignatie(punten, centroids):
    #  Geef geef voor elk punt de index van de dichtste centroÃ¯de(vanaf 0) van de centroide die het dichtste bij punt gelegen is.
    return [index_dichtste(p, centroids) for p in punten]


def bereken_centroid(punten):
    # bereken het zwaartepunt van de gegeven punten

    # if len(punten) == 0:
    #   raise ValueError("lege lijst voor bereken_centroid")
    #   ## voor de hand liggende implementatie
    # centroid = list(punten[0])
    # for punt in punten[1:]:
    #   for index, coord in enumerate(punt):
    #     centroid[index] += coord
    # centroid = [c / len(punten) for c in centroid]
    # return tuple(centroid)
    return tuple(sum(i) / len(i) for i in zip(*punten))


def update_centroids(punten, assignatie, aantal_clusters):
    # bepaal de nieuwe zwaartepunten gegeven de punten, de assignatie en het aantal clusters

    centroids = []
    for k in range(aantal_clusters):
        centroids.append(bereken_centroid([p for i, p in enumerate(punten) if assignatie[i] == k]))
    return centroids


def k_gemiddelden(punten, centroids):
    # implementeer het k-gemiddelden algoritme op een rij van punten en de centroides als argumenten. Retourneer de centroids nadat het algoritme geconvergeerd is
    assignatie = cluster_assignatie(punten, centroids)
    hasChanged = True
    while hasChanged:
        assignatie = cluster_assignatie(punten, centroids)
        nieuweCentroids = update_centroids(punten, assignatie, len(centroids))
        hasChanged = False
        for i, c in enumerate(centroids):
            if c != nieuweCentroids[i]:
                hasChanged = True or hasChanged
        centroids = nieuweCentroids
    return centroids