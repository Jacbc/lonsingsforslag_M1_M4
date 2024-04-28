#%%

# MODUL 4
# Oppgave 1

def hilsen(navn):
    print(f'Hei, hvordan går det {navn}!')


hilsen("Jacob")

#%%

# MODUL 4
# Oppgave 2

def CelsiusTilFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius_temp = 20  # 20 grader Celsius
fahrenheit_temp = CelsiusTilFahrenheit(celsius_temp)

print(f"{celsius_temp}°C er {fahrenheit_temp}°F")


#%%

# Oppgave 3

tekst = """
    Under den storslåtte sommerfestivalen vandret en entusiastisk festivalgjeng gjennom 
    mylderet med en gigantisk, flerfarget sukkerspinn i hånden, mens han beundret de 
    akrobatiske pseudohypoparat-showene på hovedscenen.
"""


def finnLengsteOrd(dinTekst):
    splittetTekst = dinTekst.split()
    ordOgLengde_stats = ["", 0]

    for ord in splittetTekst:
        ordLengde = len(ord)
        
        if ordLengde > ordOgLengde_stats[1]:
            ordOgLengde_stats[0] = ord
            ordOgLengde_stats[1] = ordLengde

    print(f'Det lengste ordet er "{ordOgLengde_stats[0]}", med en lengde på {ordOgLengde_stats[1]} tegn.')


finnLengsteOrd(tekst)


#%%

# Oppgave 4 - Mindre avansert - mindre effektiv

def genererePrimtall(primtallMindreEnnN):
    primtall = []
    for ytreTall in range(2, primtallMindreEnnN):
        delelig = 0
        for indreTall in range(2, primtallMindreEnnN):
            if  ytreTall % indreTall == 0: 
                delelig += 1
                if delelig >= 2: break
            
        if delelig == 1:
            primtall.append(ytreTall)
        
    return primtall
        
# Test funksjonen med et eksempel
n = 30
print(f"Primtall mindre enn {n}: {genererePrimtall(n)}")


#%%

# Oppgave 4 - Avansert

def er_primtall(num):
    """Returner True hvis num er et primtall, ellers False."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primtallsgenerator(n):
    """Returner en liste med alle primtall mindre enn n."""
    primtall_liste = []
    for num in range(2, n):
        if er_primtall(num):
            primtall_liste.append(num)
    return primtall_liste

# Test funksjonen med et eksempel
n = 30
print(f"Primtall mindre enn {n}: {primtallsgenerator(n)}")

