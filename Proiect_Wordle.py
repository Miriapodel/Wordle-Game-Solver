import copy
import random

cuvinte = []
guess = ""
ghicit = False
pozitie = 0
litere = [0] * 26
popularitate = []
cuvinte_sortate = []
cuvinte_sortate_entropie = []
cuvinte_dupa_entropie = []
l1 = [0] * 26
l2 = [0] * 26
l3 = [0] * 26
l4 = [0] * 26
l5 = [0] * 26


class Wordle:

    def citire_cuvinte(self):
        with open("cuvinte_wordle.txt") as f:
            for linie in f:
                cuvinte.extend(linie.split())

    def alegere_cuvant(self):
        global pozitie, guess, ghicit
        pozitie = random.randrange(len(cuvinte))
        guess = cuvinte[pozitie]
        ghicit = False

    def joc(self):
        global ghicit, guess

        print("~Ghiceste cuvantul de 5 litere~")
        print()

        ghicit = False

        while not ghicit:
            print("Cuvantul: ", end="")
            incercare = jucator.primesteCuvant().upper()
            print(incercare)
            print("          ", end="")

            if incercare == guess:
                ghicit = True
                print("Felicitari! Ai ghicit cuvantul!")
            else:
                rezultat = ""
                for i in range(5):
                    if incercare[i] in guess:
                        if incercare[i] == guess[i]:
                            rezultat += "V"
                        else:
                            rezultat += "G"
                    else:
                        rezultat += "X"
                print(rezultat)
                jucator.stergere_cuvinte_imposibile(incercare, rezultat)
                print()


class Jucator:

    def __getitem__(self, items):
        return

    def frecventa_litere_dupa_aparitii(self):
        for cuvant in cuvinte:
            for c in cuvant:
                litere[ord(c) - ord("A")] += 1

    def frecventa_litere_dupa_pozitie(self):
        for cuvant in cuvinte:
            if len(cuvant) == 5:
                l1[ord(cuvant[0]) - ord("A")] += 1
                l2[ord(cuvant[1]) - ord("A")] += 1
                l3[ord(cuvant[2]) - ord("A")] += 1
                l4[ord(cuvant[3]) - ord("A")] += 1
                l5[ord(cuvant[4]) - ord("A")] += 1

    def popularitate_cuvinte(self):
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

    def sortare_cuvinte_dupa_popularitate(self):
        global cuvinte, cuvinte_sortate
        cuvinte = sorted(cuvinte, key=lambda x: popularitate[cuvinte.index(x)], reverse=True)
        cuvinte_sortate = copy.deepcopy(cuvinte)

    def sortare_cuvinte_entropie(self):
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

    def primesteCuvant(self):
        return cuvinte_dupa_entropie[0]

    def stergere_cuvinte_imposibile(self, cuvant_curent, rezultat):

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
                    if rezultat[i] == 'V' and cuvant_curent[i] != cuvinte_dupa_entropie[poz][i] and \
                            cuvinte_dupa_entropie[poz] != "SONUL":
                        cuvinte_dupa_entropie.remove(cuvinte_dupa_entropie[poz])
                        stergere = True
                        break
            poz += 1
            if stergere:
                poz -= 1
                stergere = False

    def resetare_joc(self):
        global cuvinte_dupa_entropie
        cuvinte_dupa_entropie = copy.deepcopy(cuvinte_sortate_entropie)


wordle = Wordle()
jucator = Jucator()

wordle.citire_cuvinte()
jucator.frecventa_litere_dupa_aparitii()
jucator.frecventa_litere_dupa_pozitie()
jucator.popularitate_cuvinte()
jucator.sortare_cuvinte_dupa_popularitate()
jucator.sortare_cuvinte_entropie()
wordle.citire_cuvinte()
wordle.alegere_cuvant()
wordle.joc()
