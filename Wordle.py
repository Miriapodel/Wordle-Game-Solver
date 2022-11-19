import random
import best_word as player



cuvinte = []
litere = [0] * 26
popularitate = []
medie_incercari = 0

player.citeste_cuvinte()
player.frecventa_litere()
player.popularitate_cuvinte()
player.sortare_cuvinte()

with open("cuvinte_wordle.txt") as f:
    for linie in f:
        cuvinte.extend(linie.split())

pozitie = random.randrange(len(cuvinte))
guess = cuvinte[pozitie]
ghicit = False

print("~Ghiceste cuvantul de 5 litere~")
print()


while not ghicit:
    print("Cuvantul: ", end="")
    incercare = player.primesteCuvand().upper()
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
                    print("V", end="")
                else:
                    rezultat += "G"
                    print("G", end="")
            else:
                rezultat += "X"
                print("X", end="")
        player.stergere_cuvinte_imposibile(incercare, rezultat)
        print()

