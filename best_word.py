cuvinte = []
litere = [0] * 26
popularitate = []
cuvinte_sortate = []


def citeste_cuvinte():
    with open("cuvinte_wordle.txt") as f:
        for linie in f:
            cuvinte.extend(linie.split())


def frecventa_litere():
    for cuvant in cuvinte:
        multime_litere = set(cuvant)
        for c in multime_litere:
            litere[ord(c) - ord("A")] += 1


def popularitate_cuvinte():
    for cuvant in cuvinte:
        scor = 0
        multime_litere = set(cuvant)
        for c in multime_litere:
            scor += litere[ord(c) - ord("A")]
        popularitate.append(scor)


def sortare_cuvinte():
    global cuvinte, cuvinte_sortate
    cuvinte = sorted(cuvinte, key=lambda x: popularitate[cuvinte.index(x)], reverse=True)
    cuvinte_sortate = cuvinte



def primesteCuvand():
    return cuvinte[0]

def stergere_cuvinte_imposibile(cuvant_curent, rezultat):
    poz = 0
    stergere = False
    while poz < len(cuvinte):
        if cuvinte[poz] == cuvant_curent:
            cuvinte.remove(cuvinte[poz])
            stergere = True
        else:
            for i in range(0, len(rezultat)):
                if rezultat[i] == 'X' and cuvant_curent[i] in cuvinte[poz]:
                    cuvinte.remove(cuvinte[poz])
                    stergere = True
                    break
                if rezultat[i] == 'G' and cuvant_curent[i] == cuvinte[poz][i]:
                    cuvinte.remove(cuvinte[poz])
                    stergere = True
                    break
                if rezultat[i] == 'V' and cuvant_curent[i] != cuvinte[poz][i]:
                    cuvinte.remove(cuvinte[poz])
                    stergere = True
                    break
        poz += 1
        if stergere:
            poz -= 1
            stergere = False

def resetare_joc():
    global cuvinte, cuvinte_sortate
    cuvinte = cuvinte_sortate

