#%%

# BONUS
# Oppgave 1

from random import randint

tilfelfigTall = randint(1,100)
gittSvar = 0
forsok = 0

while gittSvar != tilfelfigTall:
    gittSvar = int(input('Hva er det hemmelige tallet?')) 

    if gittSvar == tilfelfigTall:
        print(f'Du gjettet riktig og brukte {forsok} på det!')
    elif gittSvar > tilfelfigTall:
        print(f'Du gjettet for høyt')
    else:
        print(f'Du gjettet for lavt')
    
    forsok += 1



#%%
test = "Radar"

def palindromTester(tekst):
    splitted = [*tekst.lower()]
    startIndex = 0
    endIndex = -1
    for x in range(round(len(splitted)/2)):
        if splitted[startIndex] == splitted[endIndex]:
            startIndex, endIndex = startIndex+1, endIndex-1
            continue
        else:
            print("Ordet er ikke et palindrom")
            return
    
    print("Ordet er et palindrom")
    return
        
         
palindromTester(test)