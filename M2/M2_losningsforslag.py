

#%%
# MODUL 2
# Oppgaver på dette er ikke etterspurt i oppsummeringsarket

# Henter funksjonen randint fra random biblioteket
from random import randint

# X er nå et tilfeldig tall
x = randint(1,50)
print(x)


# Demonsterere et input-felt  
svar = input("Det du skriver her lagre på variabelen svar")
print("Du skrev " + svar)



#%%

# ULIKE DATATYPER

# Liste eksempel
min_liste = [1, 2, 3, 35]
element_fra_liste = min_liste[3]*2
print("Element hentet fra liste:", element_fra_liste)

# Tuple eksempel
min_tuple = (1, 2, 3)
element_fra_tuple = min_tuple[1]
print("Element hentet fra tuple:", element_fra_tuple)

# Set eksempel
mitt_set = {1, 1, 2, 3}
element_fra_set = list(mitt_set)[0]
print("Et element hentet fra set (rekkefølge ikke garantert):", element_fra_set)

# Dictionary eksempel
min_dict = {'ett': 1, 'to': 2, 'tre': 3}
element_fra_dict = min_dict['tre']
print("Element hentet fra dict:", element_fra_dict)


#%%

# SVAR PÅ OPPGAVEN NEDERST I EKSEMPELET FRA MODUL 2


from random import randint

tall1 = randint(6, 10)
tall2 = randint(1, 10)

print('Hva er ' + str(tall1)+' * '+ str(tall2) + ' ?')

svar = input()

if int(svar) == tall1 * tall2:
    print('Ja, svaret er ' + svar)
else:
    print('Nei, svaret er ' + str(tall1 * tall2))


#%%

# Bedre måte å skrive samme koden på 

from random import randint

tall1 = randint(6, 10)
tall2 = randint(1, 10)

dittSvar = int(input(f'Hva er {tall1} * {tall2} ?: '))
rettSvar = tall1 * tall2

if dittSvar == rettSvar:
    print(f'Ja, svaret er {dittSvar}')
else:
    print(f'Nei, svaret er {rettSvar}')

