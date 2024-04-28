#%%


# MODUL 3

# Oppgave 1

innskudd = 1000
rente = 0.05

print(f"Etter ett år har du {innskudd*(1+rente)} kr")

#%%

# Oppgave 2

innskudd = 1000
rente = 0.05
antallAar = 10

# Metode 1
for aar in range(antallAar):
    innskudd += innskudd*rente
    print(f'I år {aar+1} har du {innskudd:.2f} kr.')


# # Metode 2
# for aar in range(antallAar+1):
#     # Metode 2
#     kontoBalanse = innskudd * ((1 + rente) ** aar)
#     print(f'I år {aar} har du {kontoBalanse} kr.')

#%%

# Oppgave 3 - forslag 1


innskudd = 1000
kontoMaal = innskudd * 2
rente = 0.05
antallAar = 0 

while innskudd <= kontoMaal:
    antallAar += 1
    innskudd += innskudd * rente
    if innskudd >= kontoMaal:
        print(f'Det tar {antallAar} år før du har det dobbelte, da har du {innskudd:.2f} kroner')
# %%

# Oppgave 3 - forslag 2

innskudd = 1000
kontoMaal = innskudd * 2
rente = 0.05

for aar in range(100):
    innskudd += innskudd * rente

    if innskudd >= kontoMaal:
        print(f'Det tar {aar + 1} år før du har det dobbelte, da har du {innskudd:.2f} kroner')
        break
# %%
