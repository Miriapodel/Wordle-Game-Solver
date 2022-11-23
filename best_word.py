import copy

cuvinte = []
litere = [0] * 26
popularitate = []
cuvinte_sortate = []
cuvinte_sortate_entropie = []
cuvinte_dupa_entropie = []

l1 = [788, 712, 953, 503, 209, 467, 432, 323, 413, 212, 55, 529, 711, 349, 433, 815, 5, 568, 1118, 746, 360, 466, 10,
      21, 12, 244]
l2 = [2552, 87, 202, 107, 1319, 91, 81, 72, 1344, 17, 5, 458, 192, 229, 1591, 171, 1, 815, 151, 240, 1491, 120, 4, 52,
      7, 55]
l3 = [910, 355, 541, 423, 594, 217, 310, 125, 1135, 94, 9, 864, 460, 777, 323, 490, 2, 1197, 656, 835, 568, 191, 0, 91,
      5, 282]
l4 = [1736, 166, 465, 235, 1380, 74, 153, 50, 1878, 71, 4, 427, 260, 570, 628, 168, 0, 625, 392, 771, 1070, 116, 2, 6,
      3, 204]
l5 = [1989, 31, 331, 147, 1652, 32, 85, 22, 2716, 74, 6, 790, 490, 412, 146, 53, 0, 467, 424, 841, 474, 37, 1, 24, 17,
      193]


def citeste_cuvinte():
    with open("cuvinte_wordle.txt") as f:
        for linie in f:
            cuvinte.extend(linie.split())


def frecventa_litere():
    for cuvant in cuvinte:
        for c in cuvant:
            litere[ord(c) - ord("A")] += 1


def popularitate_cuvinte():
    for cuvant in cuvinte:
        scor = 0
        multime_litere = set(cuvant)
        for c in multime_litere:
            scor += litere[ord(c) - ord("A")]
        for i in range(len(cuvant)):
            if i == 0:
                scor += l1[ord(cuvant[i]) - ord("A")]
            if i == 1:
                scor += l2[ord(cuvant[i]) - ord("A")]
            if i == 2:
                scor += l3[ord(cuvant[i]) - ord("A")]
            if i == 3:
                scor += l4[ord(cuvant[i]) - ord("A")]
            if i == 4:
                scor += l5[ord(cuvant[i]) - ord("A")]
        popularitate.append(scor)


def sortare_cuvinte():
    global cuvinte, cuvinte_sortate
    cuvinte = sorted(cuvinte, key=lambda x: popularitate[cuvinte.index(x)], reverse=True)
    cuvinte_sortate = copy.deepcopy(cuvinte)


def sortare_cuvinte_entropie():
    global cuvinte_sortate_entropie
    while len(cuvinte) > 0:
        cuvinte_dupa_entropie.append(cuvinte[0])
        cuvinte.remove(cuvinte[0])
        cuvinte_sortate.remove(cuvinte_dupa_entropie[-1])
        poz = 0
        while poz < len(cuvinte):
            for c in cuvinte_dupa_entropie[-1]:
                if c in cuvinte[poz]:
                    cuvinte.remove(cuvinte[poz])
                    poz -= 1
                    break
            poz += 1
    cuvinte_dupa_entropie.extend(cuvinte_sortate)
    cuvinte_sortate_entropie = copy.deepcopy(cuvinte_dupa_entropie)


def primesteCuvant():
    return cuvinte_dupa_entropie[0]


def stergere_cuvinte_imposibile(cuvant_curent, rezultat):
    poz = 0
    stergere = False
    while poz < len(cuvinte_dupa_entropie):
        if cuvinte_dupa_entropie[poz] == cuvant_curent:
            cuvinte_dupa_entropie.remove(cuvinte_dupa_entropie[poz])
            stergere = True
        else:
            for i in range(0, len(rezultat)):
                if rezultat[i] == 'X' and cuvant_curent[i] in cuvinte_dupa_entropie[poz]:
                    cuvinte_dupa_entropie.remove(cuvinte_dupa_entropie[poz])
                    stergere = True
                    break
                if rezultat[i] == 'G' and cuvant_curent[i] == cuvinte_dupa_entropie[poz][i]:
                    cuvinte_dupa_entropie.remove(cuvinte_dupa_entropie[poz])
                    stergere = True
                    break
                if rezultat[i] == 'V' and cuvant_curent[i] != cuvinte_dupa_entropie[poz][i] and cuvinte_dupa_entropie[poz] != "SONUL":
                    cuvinte_dupa_entropie.remove(cuvinte_dupa_entropie[poz])
                    stergere = True
                    break
        poz += 1
        if stergere:
            poz -= 1
            stergere = False


def resetare_joc():
    global cuvinte_dupa_entropie
    cuvinte_dupa_entropie = copy.deepcopy(cuvinte_sortate_entropie)
