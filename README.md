# Proiect Wordle

## Echipa:
+ Antonescu Ionut-Andrei
+ Bobei Vlad-Serban
+ Epure-Tofanel Carlo

## Descriere

  Programul este impartit in doua clase: prima reprezinta jocul propriu-zis, iar cea de a doua este jucatorul care rezolva jocul.

### Clasa Wordle

  Prima clasa, Wordle, citeste toate cuvintele de 5 litere din limba romana si alege random unul dintre ele pentru a fi ghicit de catre jucator. 
  
  ```python
  
  def citire_cuvinte(self):
        with open("cuvinte_wordle.txt") as f:
            for linie in f:
                cuvinte.extend(linie.split())

    def alegere_cuvant(self):
        global pozitie, guess, ghicit
        pozitie = random.randrange(len(cuvinte))
        guess = cuvinte[pozitie]
        ghicit = False
  
  ```
  
  Dupa fiecare cuvant pe care jucatorul il introduce, se creeaza un sir de caractere prin care se transmite jucatorului rezultatul incercarii lui.
  
  ```python
  
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
  
  ```

### Clasa Jucator

  Clasa Jucator este responsabila de ghicirea cuvantului ales de joc. Pentru asta, mai intai determina frecventa fiecarei litere in toata lista de cuvinte, dar si posibilitatea ca o litera sa apara pe o anumita pozitie. 

```python

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


```

  Apoi, fiecarui cuvant ii este asociat un scor pe baza literelor care il formeaza dupa criteriile de mai sus. 

```python

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

```

  Cuvintele sunt sortate in prima faza dupa scorul obtinut, iar apoi in functie de cantitatea de informatie pe care o ofera.

```python

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

```

  Dupa fiecare cuvant ghicit, in functie de rezultatul trimis de joc, sunt eliminate cuvintele care nu mai pot reprezenta o solutie posibila.

```python

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

```

## Numar mediu de incercari
  4.53 cuvinte
