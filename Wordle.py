import random
import best_word as player

cuvinte = []
litere = [0] * 26
popularitate = []
medie_incercari = 0
guess = ""
ghicit = False
pozitie = 0

player.citeste_cuvinte()
player.frecventa_litere()
player.popularitate_cuvinte()
player.sortare_cuvinte()


def citire_cuvinte():
    with open("cuvinte_wordle.txt") as f:
        for linie in f:
            cuvinte.extend(linie.split())


def alegere_cuvant():
    global pozitie, guess, ghicit
    pozitie = random.randrange(len(cuvinte))
    guess = cuvinte[pozitie]
    ghicit = False


def joc():
    global ghicit
    print("~Ghiceste cuvantul de 5 litere~")
    print()

    while not ghicit:
        print("Cuvantul: ", end="")
        incercare = player.primesteCuvant().upper()
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
            player.stergere_cuvinte_imposibile(incercare, rezultat)
            print()


citire_cuvinte()
alegere_cuvant()
joc()
